# ***CELL.PY***

# checks if two cells are white
# if they are, sumOfCoordinates mod 2 should be 0
# returns 1 if both are even, returns 0 otherwise
def isWhite(x1, y1, x2, y2): 
  isCellOneWhite = (x1+y1) % 2
  isCellTwoWhite = (x2+y2) % 2
  areBothWhite = isCellOneWhite | isCellTwoWhite 

  return int(areBothWhite == 0)
  
# uses slope of a straight of 2 cells to determine diagonal
# slope of diagonal points on 45 degree line wrt to origin is always 1(change in y coordinate/change in X coordinate is constant)
def isDiagonal(x1, y1, x2, y2): 
    return int((y2 - y1)/(x2 -x1) == 1)

# takes coordinates of 2 cells
# returns positive distance between them
# if cells are on a diagonal, distance is difference between any 2 corresponding coordinates |x1 - x2| or |y1 - y2|
def getLength(y1, y2):
  return  abs(y2-y1) # if I wanted to be thorough, I could have said (|x1 - x2| + |y1 - y2|)/2 but there is really no difference
