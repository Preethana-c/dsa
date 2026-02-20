def duplicates(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    max_count=0
    max_element=None
    for x in nums:
            if freq[x]>max_count:
                 max_count=freq[x]
                 max_element=x
    return max_element        

nums=[1,2,3,1,2,2,3,4,5,5,5,5]
print(duplicates(nums))
        