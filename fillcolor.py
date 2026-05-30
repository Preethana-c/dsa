from numpy import matrix


def fillcolor(matrix, x,y,color):
    rows=len(matrix)
    cols=len(matrix[0])
    visited = set()
    islands = 0

    prev_color=matrix[x][y]
    matrix[x][y]=color
    queue = []
    queue.append((x, y))
    visited.add((x, y))
    if color==prev_color:
        return matrix
         
    while queue:
            print("size", len(queue))

            i, j = queue.pop(0)
            if i-1 >= 0 and matrix[i-1][j] == prev_color:
                matrix[i-1][j]=color
                queue.append((i-1, j))
                visited.add((i-1, j))

                
            if i+1 < rows and matrix[i+1][j] == prev_color:
                matrix[i+1][j]=color
                queue.append((i+1, j))
                visited.add((i+1, j))

                
            if j-1 >= 0 and matrix[i][j-1] == prev_color:
                matrix[i][j-1]=color
                queue.append((i, j-1))
                visited.add((i, j-1))

                
            if j+1 < cols and matrix[i][j+1] == prev_color:
                matrix[i][j+1]=color
                queue.append((i, j+1))
                visited.add((i, j+1))
    return matrix

print(fillcolor([[0,0,0],[0,0,0]],0,0,0)) 
