def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    print(rows)
    print(cols)

    low = 0
    high = rows * cols - 1

    while low <= high:
       

        row=-(rows//2)
        col=-(cols//2)

        mid_element = matrix[row-1][col-1]

        if mid_element == target:
            return True
        elif mid_element >target:
            row=-(row//2)
            col=-(col//2)
        else:
            row=row*2
            col=col*2
            

    return False


print(search_matrix([[1,2,3],[4,5,6],[7,8,9]], 0))
print(search_matrix([[1,2,3],[4,5,6,],[7,8,9],[10,11,12]], 5))




    

