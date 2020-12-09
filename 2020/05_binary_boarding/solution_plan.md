# Breakdown

This problem involves binary space partitioning. Based on a series of inputs, I have to track by process of elimination all of the occuppied seats, to find mine.

## Strategy

For this problem, I might be able to use an upper and a lower limit, making changes according to the input sequence. Then, I could probably store the numbers in a list that holds all the possible values, maybe as a dictionary in which the value has a boolean attached to it. This way, I can both make sure that I get no repetitions (if the value has already been visited, which shouldn't happen in the first place), or if the value hasn't been traversed (which would result in a False value that I can afterwards search for in the dictionary).

## Second part

Also already solved this one, but since I simply had to find an empty seat between two other seats, I used a list as a queue and simply traversed the occupied seats one by one, updating a three-boolean queue. If the elements in the queue were True-False-True, that meant that the middle seat was empty, and since my seat was the only empty one, it had to be mine. One simple index shift to account for the current loop index and I would extract that middle seat.
