def shapeArea(n):
    if n == 1:
        return 1
       
    odds = [] 
    ans = 0
    # create n number of odd 
    adder = 1
    while len(odds) < n:
        odds.append(adder)
        adder += 2
    
    # Add odd numbers twice except the last one
    for i in range(len(odds) - 1):
        ans += 2 * odds[i]
    
    ans += odds[len(odds) - 1]
    
    return ans

# A better Solution
def shapeArea(n):
    return n**2 + (n-1)**2

def shapeArea(n):
    return 2*n*(n-1)+1




#######################---QUESTION---#######################


# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.
         #
#       ###
         #

# Example

# For n = 2, the output should be
# shapeArea(n) = 5;
# For n = 3, the output should be
# shapeArea(n) = 13.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer n

# Guaranteed constraints:
# 1 ≤ n < 104.

# [output] integer

# The area of the n-interesting polygon.