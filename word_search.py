def word_search(matrix,word):
    rows=len(matrix)
    cols=len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]