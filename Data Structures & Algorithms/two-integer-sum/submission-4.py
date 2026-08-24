class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        for i,n in enumerate(nums):
            check[n]=i
        #after adding to the map we want to loop again and check the map
        for i,n in enumerate(nums):
            diff = target - n
            if diff in check and check[diff] != i:
                return [i,check[diff]]
        return []
        