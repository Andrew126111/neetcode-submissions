class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx, val in enumerate(nums):
            hashMap[val] = idx
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hashMap and hashMap[diff] != idx:
                return [idx, hashMap[diff]]
        return []
