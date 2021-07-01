# Array_Manipulation_HackerRank_Python
The array manipulation problem from HackerRank solved in Python.

Given a list of queries and the amount of values in the array to manipulate (values starting at 0), manipulate the array based on said queries.

Each query has an a, b, and k in an array in that order. The variables a and b represent the start and end of the range of values to manipulate, and k is the value to add to those indices.

Given these indices, find the maximum value of the resulting array.

The simplest solution would be to add the value to each index in the array as needed, but that does not scale well at higher levels. That implementation would take O(n^2) time, given that using a loop to go through each query and then add values to the array based on how many indices are specified in the query.

The better way to to this is to keep track of the slope so to speak. At the start of the range you add the value, because that is where the increase starts, and then you subtract the value from the element after the range because the increase stops there. Instead of keeping track of values you keep track of slope in this case, while this means you will need to go through the array of values and add the slopes for each element to find the maximum, it does ultimately save time by cutting the first loop down to O(n) time.
