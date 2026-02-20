#Given an integer array nums, return true if any value appears at least twice in the array and return false if every elemetn is distinct
def duplicates(nums):
    freq={}
    nums2=[]
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in nums:
        for key,value in freq.items():
            if value==2:
                for j in range(2):
                    nums2.append(key)
            else:
                for j in range(value):
                    nums2.append(key)
    return nums2
nums=[1,1,2,2,2,3,3,4,4,4,4]
print(duplicates(nums))
                    
    
    

