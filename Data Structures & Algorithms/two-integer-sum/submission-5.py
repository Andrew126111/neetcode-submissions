class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check= {}
        for i,n in enumerate(nums):
            check[n]= i
        for i,n in enumerate(nums):
            diff = target - n
            for j in check:
                if diff in check and check[diff] != i:
                    return [i, check[diff]]
        return False
        