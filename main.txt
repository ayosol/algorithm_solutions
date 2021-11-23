# ***MAIN.PY***

from cell import *

x1 = int(input('Enter the x (first) coordinate for the source cell\n'))
y1 = int(input('Enter the y (second) coordinate for the source cell\n'))
x2 = int(input('Enter the x (first) coordinate for the destination cell\n'))
y2 = int(input('Enter the y (second) coordinate for the source cell\n'))

distance = isWhite(x1, y1, x2, y2) * isDiagonal(x1, y1, x2, y2) * getLength(y1, y2)
print("The length of a diagonal path from ( {} , {} ) to ( {} , {} ) is : {}".format(x1, y1, x2, y2, distance))