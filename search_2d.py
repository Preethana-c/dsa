def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    print(rows)
    print(cols)

    low = 0
    high = rows * cols - 1

    while low <= high:
        mid = (low + high) // 2

        row = mid // 2
        col = mid //2

        mid_element = matrix[row][col]

        if mid_element == target:
            return True
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


print(search_matrix([[1,2,3],[4,5,6],[7,8,9]], 0))
print(search_matrix([[1,2,3],[4,5,6,],[7,8,9],[10,11,12]], 5))




    

