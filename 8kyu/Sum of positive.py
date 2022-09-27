"""
DESCRIPTION:
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""

# Original solution

def positive_sum(arr):
    sum = 0
    for a in arr:
        if a > 0:
            sum += a
        if a <= 0:
            continue
    return sum