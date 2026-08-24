class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for idx,val in enumerate(nums):
            hashmap[val] = idx
        for idx,val in enumerate(nums):
            diff = target - val
            if diff in hashmap and hashmap[diff] !=idx:
                return [idx, hashmap[diff]]
        return []
