from collections import deque
ROW = 100
COL = 100
 
# To store matrix cell coordinates
class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y
 
# A data structure for queue used in BFS
class queueNode:
    def __init__(self,pt: Point, dist: int):
        self.pt = pt  # The coordinates of the cell
        self.dist = dist  # Cell's distance from the source
 
# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)
 
# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]
 
# Function to find the shortest path between
# a given source cell to a destination cell.
def BFS(mat, src: Point, dest: Point, fn: int):
     
    # check source and destination cell
    # of the matrix have value 1
    # if mat[src.x][src.y]!=1 or mat[dest.x][dest.y]!=1:
    #     return -1

    a = (src.y*src.y + 3*src.y + 2*src.y*src.x + src.x + src.x*src.x) + fn
    if a % 2 != 0:
        return -1
    a = (dest.y*dest.y + 3*dest.y + 2*dest.y*dest.x + dest.x + dest.x*dest.x) + fn
    a = bin(a).split('b')[1].count('1')
    if a % 2 != 0:
        return -1
     
    visited = [[False for i in range(COL)]
                       for j in range(ROW)]
     
    # Mark the source cell as visited
    visited[src.x][src.y] = True
     
    # Create a queue for BFS
    q = deque()
     
    # Distance of source cell is 0
    s = queueNode(src,0)
    q.append(s) #  Enqueue source cell
     
    # Do a BFS starting from source cell
    while q:
 
        curr = q.popleft() # Dequeue the front cell
         
        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist
         
        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            c = 0
            a = (col*col + 3*col + 2*col*row + row + row*row) + fn
            a = bin(a).split('b')[1].count('1')
            if a % 2 == 0:
                c = 1
             
            # if adjacent cell is valid, has path 
            # and not visited yet, enqueue it.
            if (isValid(row,col) and
               c == 1 and
                not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row,col),
                                    curr.dist+1)
                q.append(Adjcell)
     
    # Return -1 if destination cannot be reached
    return -1
 
# Driver code
def main():
    mat = [[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
           [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 1 ],
           [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
           [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
           [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 0 ],
           [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
           [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
           [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
           [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]
    source = Point(1,1)
    dest = Point(39, 31)
     
    dist = BFS(mat,source,dest,1358)
     
    if dist!=-1:
        print("Shortest Path is",dist)
    else:
        print("Shortest Path doesn't exist")
main()