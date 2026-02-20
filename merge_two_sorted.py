def merge(nums1,nums2):
    for i,j in zip(nums1,nums2):
            if i<j:
                index=nums1.index(i)
                nums1[index+1]=j
    return nums1
nums1=[1,3,5,7]
nums2=[2,4,6,8]
print(merge(nums1,nums2))