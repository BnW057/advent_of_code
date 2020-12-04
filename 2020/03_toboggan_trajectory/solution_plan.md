# Breakdown

For this problem, there is basically a map with a repeating pattern through which I have to travel in a straight line, and I have to make sure to get the least amount of hits on "trees". The path with the least amount of obstacles in it is the correct answer.

## Strategy

I can use mod and a carry-on counter to wrap around every time I hit an end of line. Modular will take care of not going beyond array limits, and the carry on will take care of how much to move after resetting the position. It's basically traversing an array, but just doing this as I read the file should be enough.
