# Solution 2- passed all test cases

def areFollowingPatterns(strings, patterns):
    strToPatt = {}
    pattToStr = {}
    for i in range(len(strings)):
        if strings[i] in strToPatt:
            if strToPatt[strings[i]] != patterns[i]:
                return False
        else:
            strToPatt[strings[i]] = patterns[i]
        
        if patterns[i] in pattToStr:
            if pattToStr[patterns[i]] != strings[i]:
                return False
        else:
            pattToStr[patterns[i]] = strings[i]
    
    return True


# Solution 1- passed 22/23 tests
def areFollowingPatterns(strings, patterns):
    i = 0
    while (i + 1) < len(strings):
        if strings[i] == strings[i+1] and patterns[i] != patterns[i+1]:
            return False 
        if strings[i] != strings[i+1] and patterns[i] == patterns[i+1]:
            return False 
        i += 1
        
    return True


# Not my Solution - best on the site
def areFollowingPatterns(strings, patterns):
    return len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns)))

#######################---QUESTION---#######################

# Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

# Example

# For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
# areFollowingPatterns(strings, patterns) = true;
# For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
# areFollowingPatterns(strings, patterns) = false.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.string strings

# An array of strings, each containing only lowercase English letters.

# Guaranteed constraints:
# 1 ≤ strings.length ≤ 105,
# 1 ≤ strings[i].length ≤ 10.

# [input] array.string patterns

# An array of pattern strings, each containing only lowercase English letters.

# Guaranteed constraints:
# patterns.length = strings.length,
# 1 ≤ patterns[i].length ≤ 10.

# [output] boolean

# Return true if strings follows patterns and false otherwise.