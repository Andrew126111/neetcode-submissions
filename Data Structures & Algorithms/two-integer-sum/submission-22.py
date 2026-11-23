class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for idx, num in enumerate(nums):
            res[num] = idx
        for idx, num in enumerate(nums):
            sums = target - num
            if sums in nums and res[sums] != idx:
                return [idx, res[sums]]
        return []