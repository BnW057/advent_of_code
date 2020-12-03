# Breakdown

There is a list of values which are to be tested as valid passwords. The passwords must follow a set of rules to be valid. Based on the provided passwords along with the rules, I must find the correct password.

## Strategy

The list is comprised of two numbers separated by a hyphen, followed by a single letter, and lastly, a string. The two numbers represent a range. The single letter is the one that must be within the range provided. The third one is the string in which the policy has to be tested. Based on this, I must probably try to map the values into an integer/char/string tuple. Actually, I don't even need to store the values. I think that is the wrong direction in which to lead my efforts. I could simply read line by line, and then create a set of rules to extract the range value, test value, and sample to validate. It will be a better approach for this part of the problem.

## Second Part

For the second part, it is explained that the numbers are not a range, but positional indeces. The indeces must contain the target value once only, not in both positions. It doesn't matter how many there are as long as the repetition does not occur in the provided ranges. Since my regular expression separates all of the values, it is an easy solve from here.
