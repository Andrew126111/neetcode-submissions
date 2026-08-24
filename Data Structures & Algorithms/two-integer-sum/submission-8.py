class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, val in enumerate(nums):
            hash_map[val] = idx
        for idx, val in enumerate(nums):
            curr = target - val
            if curr in hash_map and hash_map[curr] != idx:
                return [idx, hash_map[curr]]
        return []

