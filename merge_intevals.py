def merge_intervals(arr):
    arr.sort()
    result=[]
    for i in arr:
        for j in range(i+1,len(arr)):
            if arr[i][0]<=arr[j][1] and arr[j][0]<=arr[i][1]:
                arr[i][0]=min(arr[i][0],arr[j][0])
                arr[i][1]=max(arr[i][1],arr[j][1])
        if arr[i] not in result:
            result.append(arr[i])
    return result








'''def merge_intervals(arr):
    result=[]
    for i in arr:
        for j in i:
            for k in arr:
                if k[0][1]<=j<=k[1][0] and k[0][0]<=i[0][0]<=k[1][1]:
                       i[0]=min(i[0],k[0])
                       i[-1]=max(i[-1],k[-1])
        if i not in result:
            result.append(i) 
    return result'''
           
            
            