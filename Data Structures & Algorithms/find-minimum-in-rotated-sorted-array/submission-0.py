class Solution:
    def findMin(self, nums: List[int]) -> int: #we compare is to the mid values to check for a dip
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left+right) //2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
