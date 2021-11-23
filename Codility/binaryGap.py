# SOLUTION 1

def solution(N):
    # Convert the number to binary representation
    # Map out all indexes of 1 and return the ons with the largest differences
    num_rep = generateBinary(N)
    prev = 0
    current = 0
    diff = 0
    ans = 0
    no_gap = False
    for i in range(len(num_rep)):
        prev = current
        prev_diff = diff
        if num_rep[i] == '1':
            no_gap = True
            current = i
            diff = current - prev
            ans = max(prev_diff, diff)
        else:
            no_gap = False
    
    return ans - 1 if no_gap else 0



def generateBinary(N):
    #ans = bin(N)
    ans = []
    while N > 0:
        ans.append(str(N%2))
        N = N//2
    ans = ans[::-1]
    return "".join(ans)

SCORE: 53%
CORRECTNESS: 53%

#  SOLUTION 2




# ****************************************************

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
