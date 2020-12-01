# Breakdown

There is a list of values that can be paired to equal 2020. Only one pair of values yield that result in their sum. The values are written in the puzzle input [file](./puzzle_input.txt) included in the current directory.

## Strategy

This puzzle suggests loops. I have to first sort the values from highest to lowest and then make sure they do not repeat. If they do not repeat, I could use a hash table for a quicker lookup of unique values. If values repeat, I could simply remove the duplicates and do the same. For the lookup, I'd subtract a chosen value from 2020, and then plug that key into the hash table. If the key does not return a "true" value value (which will be given by default to all keys) then it is not on the list, and the sum cannot occur. This saves me time from having to actually calculate the entire list for a match wastefully. If I already know what the expected pair should be, all I need is to make sure that it is inside the list, after all. After a complete pair is found, the numeric value of the keys is multiplied together and that is the answer.
