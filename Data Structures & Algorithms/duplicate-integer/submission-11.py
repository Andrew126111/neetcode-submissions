class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0)+1
        for j in hashmap:
            if hashmap.get(j) > 1:
                return True
        return False