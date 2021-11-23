# Solution 4 - All tests passed
def almostIncreasingSequence(sequence):
    count = 0
    c = 0
    for i in range(len(sequence) - 1):
        if (sequence[i+1] <= sequence[i]):
            count += 1
        if (i+2 < len(sequence) and sequence[i+2] <= sequence[i]):
            c += 1
                  
    return count < 2 and c < 2


# Solution 3 - 34/38 tests passed
def almostIncreasingSequence(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        if (sequence[i+1] <= sequence[i]):
            count += 1
        if (i+2 < len(sequence) and sequence[i+2] <= sequence[i]):
            count += 1
                  
    return count <= 2


# Solution 2 - 32/38 tests passed
def almostIncreasingSequence(sequence): 
    count = 0
    for i in range(len(sequence) - 1):
        if (sequence[i+1] <= sequence[i]):
            count += 1
            if count > 1:
                return False
             
    return True



# Solution 1 - Not optimal
def almostIncreasingSequence(sequence):
    count = 0
    for i in range(len(sequence)-1):
        j = i+1
        if (sequence[i] < sequence[j]):
            while(j+1 < len(sequence)):
                if (not((sequence[j] < sequence[j+1]) and (sequence[j] > sequence[i]))):
                    count += 1
                j += 1
        else:
            count += 1
             
    if count == 1: 
        return True
    else: 
        return False


#######################---QUESTION---#######################

# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

# Example

# For sequence = [1, 3, 2, 1], the output should be
# almostIncreasingSequence(sequence) = false.

# There is no one element in this array that can be removed in order to get a strictly increasing sequence.

# For sequence = [1, 3, 2], the output should be
# almostIncreasingSequence(sequence) = true.

# You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

# Input/Output
    
# [execution time limit] 4 seconds (py3)

# [input] array.integer sequence

# Guaranteed constraints:
# 2 ≤ sequence.length ≤ 105,
# -105 ≤ sequence[i] ≤ 105.

# [output] boolean

# Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.