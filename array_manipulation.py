#!/bin/python3

# Imports
import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    
    length = len(queries) # Getting how many queries there are
    
    arr = [0 for i in range(n)] # Creating the array of values, each initialized to 0
    
    for i in range(length): # This implementation doesn't add the value to each individual element each time, it just keeps track of increases/decreases
        
        a = queries[i][0] # Start of range (indices start at 1)
        b = queries[i][1] # End of range (inclusive)
        k = queries[i][2] # Value to add
            
        arr[a-1] += k # Adding the value to the start of the range
        
        if(b!=n): # Subtracting the value from the next element if it exists
            arr[b] -= k
            
    maximum = 0
    current = 0
    
    for i in range(n): # For each element in the array of values
        
        current += arr[i] # Add the increase/decrease in value associated with that index
        
        if(current>maximum): # Check if the current number is greater than the maximum
            
            maximum = current # Update the maximum if needed
            
    return maximum # Return the maximum

# Main function for HackerRank
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
