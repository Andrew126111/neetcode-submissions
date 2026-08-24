class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = []
        for i in nums:
            if i in newList:
                return True
            else:
                newList.append(i)
        return False