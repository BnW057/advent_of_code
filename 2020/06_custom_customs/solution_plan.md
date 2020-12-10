# Breakdown

For this problem I have to count the total number in which a certain character appears per grouping. Regardless of if there are duplicates in the same grouping, each character amounts to only 1 point per group. I have to find out how many characters appear at least once per group.

## Strategy

I'm not sure how to tackle this one, but I definitely need a list that adds elements to it once per group. I don't think I'd need a 2D array, but the moment one element is added to the list, I have to make sure that it does not mess with another group's validation. If I add 'a' for one group, and then avoid adding more 'a's, the second that I check another group and get an 'a' it would fail if I do not manage to account for the 'a' belonging to another group. Maybe use two separate lists? One I can clear and add elements to check per group, and another one that only adds an occurrence once. After that, I can probably simply count the length of the list because I'd be certain that there would be only repeated elements when they belonged to different groups, and all we care about is the total, so the total of elements would be the answer for the first part of the problem.
