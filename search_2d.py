def Search_matrix(matrix,target):
    rows=len(matrix)
    cols=len(matrix[0])
    low=0
    high=rows*cols-1
    mid_elemeent=matrix[mid_rows][mid_cols]
    midrows=0
    midcols=0
    while low<=high:
        mid_rows=rows//2
        mid_cols=cols//2
        mid_elemeent=matrix[mid_rows][mid_cols]
        if mid_elemeent==target:
            return True
        elif mid_elemeent<target:
            mid_rows=mid_rows-1
            mid_cols=mid_cols-1
        else:
            mid_rows=mid_rows+1
            mid_cols=mid_cols+1
    return False   

Search_matrix([[1,2,3],[4,5,6],[7,8,9]],5)

    

