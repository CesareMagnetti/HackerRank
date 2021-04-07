# Artificial Intelligence practice questions on HackerRank

## requirements
No special requirements other than taht python 3.8.2 was used.

## BotSavesPrincess
Not really an AI question, more of a problem solving/coding interview question. The princess is located somewhere in grid, the bot somewhere else, find the moves the bot should make to reach the princess.

**run as:** 
```python 
python BotSavesPrincess.py
```

**example input:**<br>
3<br>
---<br>
-m-<br>
p--<br>

**example output:**<br>
DOWN<br>
LEFT<br>

**Brief Explanation**
1. get the location of the princess and of the bot, this was done looping through the 2D input and checking for keyword compatibility, retrieving indeces. You could use numpy where if you want to use additional libraries

2. since you can only move horizontally and vertically simply subtract the coordinates of the bot from the coordinates of the princess to get the total amount of horizontal and vertical movement to do. If negative we need to move either UP or LEFT, if positive we move DOWN or RIGHT (i.e. the origin is at the top left).

3. you now know how many times to move both horizontally and vertically, i.e. you already solved the question. You could interlace your moves or leave them as they are, it won't metter since you can only move along the grid the distance will be the same either way.

## BotClean

To run this exercise go to https://www.hackerrank.com/challenges/botclean/problem and copy and paste the code in ```BotClean.py``` to see the bot moving.

**Brief Explanation**
You have a grid world where dirt spots are marked as ```d``` and bot location is marked as ```b```. Since everithing is deterministic and you know in advance where all dirt spots are, this is again not an AI question and can be solved simply moving towards the closest dirt spot each time. There is not really a need to use dynamic programming to solve this because the environments where relatively small, but one could use DP for this exercise as well.

1. extract locations of each dirt ("d") spot on the grid. a simple list comprehention where you match keyword "d" will do the job.

2. find distances (in this case L1 norm as we can only move along the grid cells) of the bot from each dirt spot.

3. choose the dirt spot closest to the current bot location as a target destination.

4. subtract the bot's coordinates from the target coordinates to know how much to move, choose the direction where we need to move the most in. If the difference between the target location and bot location is positive we need to move ```RIGHT/DOWN``` else we move ```LEFT/UP``` (i.e. origin at the top left). if both differences are zero we are already on the dirt spot, hence we output ```CLEAN```

## BotCleanStochastic

To run this exercise go to https://www.hackerrank.com/challenges/botcleanr?hr_b=1 and copy and paste the code in ```BotCleanStochastic.py``` to see the bot moving.

This exercise was essentially the same as **BotClean** but even easier: you just have one dirt location per time step so you don't even have to choose, simply move towards it and you are done.
