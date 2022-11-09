from collections import deque
import hashlib

ROW = 4
COL = 4
 
# To store matrix cell coordinates
class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y
 
# A data structure for queue used in BFS
class queueNode:
    def __init__(self,pt: Point, input: str):
        self.pt = pt  # The coordinates of the cell
        self.input = input  # Cell's distance from the source
 
# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)
 
# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [0, 1, 0, -1]
colNum = [-1, 0, 1, 0]
 
# Function to find the shortest path between
# a given source cell to a destination cell.
def BFS(src: Point, dest: Point, fn: int, input: str):
     
    # check source and destination cell
    # of the matrix have value 1
    # if mat[src.x][src.y]!=1 or mat[dest.x][dest.y]!=1:
    #     return -1
    longest = 0
     
    visited = [[False for i in range(COL)]
                       for j in range(ROW)]
     
    # Mark the source cell as visited
    visited[src.x][src.y] = True
     
    # Create a queue for BFS
    q = deque()
     
    # Distance of source cell is 0
    s = queueNode(src, input)
    q.append(s) #  Enqueue source cell
     
    # Do a BFS starting from source cell
    while q:
 
        curr = q.popleft() # Dequeue the front cell
         
        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            if len(curr.input[len(input):]) > longest:
                longest = len(curr.input[len(input):])
            curr = q.popleft()

        print(curr.input)
        md5 = hashlib.md5(curr.input.encode()).hexdigest()
        print(md5[:4])
        # Otherwise enqueue its adjacent cells
        for i in range(4):
            add = ""
            if i == 0:
                add = 'U'
                if md5[0].isdigit() or md5[0] == 'a':
                    continue
            elif i == 1:
                add = 'R'
                if md5[3].isdigit() or md5[3] == 'a':
                    continue
            elif i == 2:
                add = 'D'
                if md5[1].isdigit() or md5[1] == 'a':
                    continue
            elif i == 3:
                add = 'L'
                if md5[2].isdigit() or md5[2] == 'a':
                    continue

            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            if row == 3 and col == 3:
                options = 0
                for j in range(4):
                    if not md5[j].isdigit() or md5[2] != 'a':
                        options += 1

                if options > 1:
                    if len((curr.input + add)[len(input):]) > longest:
                        longest = len((curr.input + add)[len(input):])
                    continue
            
             
            # if adjacent cell is valid, has path 
            # and not visited yet, enqueue it.
            if (isValid(row,col)): # and not visited[row][col]
                visited[row][col] = True
                Adjcell = queueNode(Point(row,col), curr.input + add)
                q.append(Adjcell)
     
    # Return -1 if destination cannot be reached
    return longest
 
# Driver code
def main():
    input = "njfxhljp"
    source = Point(0,0)
    dest = Point(3, 3)
     
    dist = BFS(source, dest, 1358, input)
     
    if dist!=0:
        print("Longest Path is",dist)
    else:
        print("Path doesn't exist", dist)
main()