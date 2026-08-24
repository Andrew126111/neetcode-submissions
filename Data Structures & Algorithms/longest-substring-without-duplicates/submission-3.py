class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupes = set()
        left = 0
        res = 0

        for r in range(len(s)):
            while s[r] in dupes:
                dupes.remove(s[left])
                left +=1
            res = max(res, r - left + 1)
            dupes.add(s[r])
        return res
