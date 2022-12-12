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

## To be continued
