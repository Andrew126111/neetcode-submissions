class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupes=set()
        left = 0 
        res = 0
        for right in range(len(s)):
            while s[right] in dupes:
                dupes.remove(s[left])
                left +=1
            dupes.add(s[right])
            res = max(res, right - left +1)
        return res

