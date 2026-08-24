class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for i in hashset:
            length = 0
            if (i-1) in hashset:
                continue
            while i+length in hashset:
                length +=1
            longest = max(longest, length)
        return longest
        
                    
