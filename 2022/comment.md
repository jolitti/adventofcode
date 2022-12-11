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

---

## To be continued
