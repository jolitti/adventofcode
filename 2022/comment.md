# Comments on AOC 2022

(spoilers!)  

## Day 11
Probably like the majority of the participants, 
I tried to solve part 2 by brute force. The goal was 10k 
iterations, but my caveman-like approach barely 
surpassed 300.  
Then I took a closer look at the input data. The 
divisibility checks were all prime numbers! 
That had to mean something.  
My immediate intuition was to modulo the throw count 
by their product for each iteration. I didn't concretely 
prove it to myself, but I knew that a modulo for x 
doesn't change the divisibility by x, so the same should 
be true for the modulo of x\*y and their individual divisibility.  
This works for non-prime numbers too, but the author probably 
wanted to ease the solver into the realization.

Anyway, I quickly threw together an implementation of this 
principle and fearfully launched the program. 
It worked! I'm so happy I don't have to spend another hour 
figuring out a more rigorous approach.

---

## Day 12
Part 2: 
Spent more that I care to admit before realizing there are 
areas of "a"s surrounded by unclimbable ledges.  
Applied a very brute force approach iterating through all 
candidates, but if I coded a finer solution the time save 
would probably not have been worth it.  
Very fun day nonetheless, hopefully tomorrow I have time 
to solve tomorrow's before the next comes out.

Now that I think about it, I could've solved part 2 
by starting from the top and exploring until i found an "a"

---

## Day 13
Decided to save the input to avoid eval() exploits if 
somehow a hacker gains control of the aoc server. Solved the 
comparison function on paper, the implementation was fairly quick.  
Took a hot second to find a way to enforce it as a sort comparison 
function for python

---

## Day 14
Finally got back to solving after pausing for an exam.  
This day was really fun to solve, up until the last part when I had a 
rare off-by-two error. I'm sad I don't have the time to understand why it happened, 
I got lucky by incrementing my answer by one a couple times because I had the feeling I 
was close to the solution. Still, I always love a puzzle where the visualization comes 
free with the solution.

---

## Day 15
Due to a combination of laziness and business, I'm really 
unsatisfied with my solution to this one.  
First of all, I got stuck two times on the first part because 
I kept trying naive approaches, hoping they would be sufficient. 
A kind stranger on reddit helped me realize I was counting a 
single beacon three times. The second part was easier thanks to 
the `shapely` library which allowed me to plot the beacon areas and 
the missing coverage inside the bounding area. I didn't even check if 
the blind spot contained more than one integer coordinate pair, I 
just entered the exact middle point of the area.  
Overall a humbling experience which I've thankfully overcome. 
I need to get better at geometry computation.

---

## Day 16
I'm still too busy studying to complete this, but I'm mentally 
refining my approach. The first instinct was to make an 
exploration tree for each room with two possible actions: move 
or open valve, but it scales too quickly to be feasible.  
So I tried to collapse the room graph eliminating all the "corridor" 
rooms with 0 flow and two exits, but it wasn't enough even for the 
example problem: the steps where the imaginary player was running around 
never opening any valve were too numerous. A partial solution was to 
fuse together the two actions (it's easy enough to compute the 
minimum distance between any two nodes, even if I made the grave 
mistake to repeat it for each iteration). Unfortunately, this is 
still agonizingly slow and gives the wrong answer for the actual 
input.  
My next attempt will involve a complete rewrite where I'll precompute 
the minimum distance between every node with flows (and AA) and an 
iteration over every permutation of the rooms. For my input set, 
this is an iteration of almost 40 million elements, but the calculations 
themselves are pretty quick. Also it assumes that every visit route 
can be done in less than 30 minutes, but it's easy to test that 
hypothesis. Will update this log when I actually implement this approach.  

Finished most of the exams, went back to take a look. 
Turns out the iteration over every room combination is even slower. 
I'll sleep on it and think of a new approach tomorrow. 

Ok, I've tried dynamic programming to perform a BFS of the possible 
traversals and it runs surprisingly fast. I've had a moment of 
desperation when the algorithm solved the sample data but not the 
real one, but then I realized the solution it outputted landed on 
the last room and opened the valve right as the clock hit 0, so the 
last action was entirely pointless. Adding a check to skip moves that 
commit that error yielded a new solution that I typed wrong in the 
webpage's box, so I'll have to wait a couple of minutes.

Typed it wrong again.

The solution was correct and was pretty easy to reuse for part 2. 
I used the cartesian product to generate every binary partition of the room 
set and assigned one for each actor, maximising the sum of the resulting 
explorations. The run time was pretty slow, so I added a `print()` 
to get notified every time a better score was achieved and stopped the 
program after a couple of minuted of no new records. This proved to be the 
correct answer, luckily.

All in all, I'm not super proud of this solution, but I'm happy I managed 
to implement some aspects of dynamic programming and partitioning.

---

## To be continued
