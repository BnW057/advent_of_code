# Breakdown

For this problem, I'm supposed to make sure that some unordered groupings of data have a certain number of fields. If it does not have all the required fields, the data for that section is categorized as invalid. One of the fields, cid, is optional.

## Strategy

Initially due to the structure of the data in the file, I was simply going to make a string search with some booleans for the categories, since some of the groups have multiple lines for a single cohesive item. This might prove inconvenient if in the second part I have to filter fields based on some condition that requires reading their values. Regardless, a singular new line separates items from each other, so if a line only contains a new line, it is a good place to stop looking for matches. I'll go with key value pairs that are updated as information is found, but if it doesn't match a validation check, it does not count as a valid passport, and the values are reset for the next test. I'll probably have to use regular expressions.
