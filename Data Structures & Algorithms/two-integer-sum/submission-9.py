class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for idx, val in enumerate(nums):
            hashy[val] = idx
        for idx, val in enumerate(nums):
            curr = target - val
            if curr in hashy and hashy[curr] != idx:
                return [idx, hashy[curr]]
        return []
