class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        count={}
        
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            
            
