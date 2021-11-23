# SOLUTION 1
def reverse_string(str1):
    str1 = list(str1)
    if str1 == None:
      return None
    i = 0
    j = len(str1) - 1
    while i < j:
      temp = str1[i]
      str1[i] = str1[j]
      str1[j] = temp
      i += 1
      j -= 1
    return "".join(str1)
 
# SOLUTION 2
def reverse_string(string):
  new_string = ''
  for i in range(len(string)-1, -1):
    new_string += string[i]
  return new_string
  
  
# Method 3
def reverse_string(s):
    s1 = ""
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1


# Method 4
def reverse_string(s):
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


# Method 5
def reverse_string(s):
    tmp = ""
    for char in s:
        tmp = char + tmp
    return tmp
