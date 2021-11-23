# Solution 2 - Passed all tests
def containsCloseNums(nums, k):
    check = {}
    for i in range(len(nums)):
        if nums[i] in check:
            if check[nums[i]] != i and abs(check[nums[i]] - i) <= k:
                return True
        check[nums[i]] = i
       
    return False

# Solution 1 - 23/24 test cases, timed out
def containsCloseNums(nums, k):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if i != j and nums[i] == nums[j] and abs(i-j) <= k:
                return True
    return False


#######################---QUESTION---#######################

# Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

# Example

# For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
# containsCloseNums(nums, k) = true.

# There are two 2s in nums, and the absolute difference between their positions is exactly 3.

# For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
# containsCloseNums(nums, k) = false.

# The absolute difference between the positions of the two 2s is 3, which is more than k.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer nums

# Guaranteed constraints:
# 0 ≤ nums.length ≤ 55000,
# -231 - 1 ≤ nums[i] ≤ 231 - 1.

# [input] integer k

# Guaranteed constraints:
# 0 ≤ k ≤ 35000.

# [output] boolean