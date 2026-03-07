def queue_insert(queue_a, element):
    queue_a.append(element)
    return queue_a

def rotten_orange(matrix, queue_a):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    time = 0


    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                count += 1
            if matrix[i][j] == 2:
                queue_insert(queue_a, (i, j))

 
    while queue_a and count> 0:
        size = len(queue_a)

        for _ in range(size):
            i, j = queue_a.pop(0)

            if i-1 >= 0 and matrix[i-1][j] == 1:
                matrix[i-1][j] = 2
                queue_insert(queue_a, (i-1, j))
                count -= 1

            if i+1 < rows and matrix[i+1][j] == 1:
                matrix[i+1][j] = 2
                queue_insert(queue_a, (i+1, j))
                count -= 1

            if j-1 >= 0 and matrix[i][j-1] == 1:
                matrix[i][j-1] = 2
                queue_insert(queue_a, (i, j-1))
                count -= 1

            if j+1 < cols and matrix[i][j+1] == 1:
                matrix[i][j+1] = 2
                queue_insert(queue_a, (i, j+1))
                count -= 1

        time += 1

    if count > 0:
        return -1

    return time
print(rotten_orange([[2,1,1],[1,1,0],[0,1,1]], []))
                
                





'''def orangesRotting(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    time=0
    for i in range(rows):
        for j in range(cols):
            print(i)
            print(j)
            if matrix[i][j]==2:  
                if i-1>=0 and matrix[i-1][j]==1:
                    matrix[i-1][j]=2 # this will not execute for 0,0
                if i+1<rows and matrix[i+1][j]==1: # 
                    matrix[i+1][j]=2
                if j-1>=0 and matrix[i][j-1]==1:
                    matrix[i][j-1]=2        
                if j+1<cols and matrix[i][j+1]==1:
                    matrix[i][j+1]=2
                time+=1 #this is for non border elements
     # if i-1=0 or i+1>rows or j-1=0 or j+1>cols then this block will give indentation that is wy that check 
                
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==1:
                    return -1
                else:
                    return time
                    
x=(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print("time taken for all oranges to rot is ",x)'''
    
    

         
                
                

                 










'''0     1      2
0  0,0  0,1   0,2
1 1,0   1,1   1,2
2 2,0   2,1   2,2



i,j rotten element
i-1,j left element
i+1,j right element
i,j-1 top element
i,j+1 bottom element

'''

   

    