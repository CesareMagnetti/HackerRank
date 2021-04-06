# Artificial Intelligence practice questions on HackerRank

## requirements
No special requirements other than taht python 3.8.2 was used.

## BotSavesPrincess
Not really an AI question, more of a problem solving/coding interview question.

**run as:** 
```python 
python BotSavesPrincess.py
```

**example input:**
3
---
-m-
p--

**example output:**
DOWN
LEFT

**Brief Explanation**
1. get the location of the princess and of the bot, this was done looping through the 2D input and checking for keyword compatibility, retrieving indeces. You could use numpy where if you want to use additional libraries

2. since you can only move horizontally and vertically simply subtract the coordinates of the bot from the coordinates of the princess to get the total amount of horizontal and vertical movement to do. If negative we need to move either UP or LEFT, if positive we move DOWN or RIGHT (i.e. the origin is at the top left).

3. you now know how many times to move both horizontally and vertically, i.e. you already solved the question. You could interlace your moves or leave them as they are, it won't metter since you can only move along the grid the distance will be the same either way.
