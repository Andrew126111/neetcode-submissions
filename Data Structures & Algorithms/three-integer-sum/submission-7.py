class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sorted_arr = sorted(nums)
        for i in range(len(sorted_arr)):
            if i>0 and sorted_arr[i] == sorted_arr[i-1]:
                continue
            left=i+1
            right = len(sorted_arr) - 1
            while left < right:
                threeSum = sorted_arr[i] + sorted_arr[left] + sorted_arr[right]
                if threeSum < 0:
                    left+=1
                elif threeSum > 0:
                    right-=1
                else:
                    res.append([sorted_arr[i],sorted_arr[left],sorted_arr[right]])
                    left+=1
                    while left<right and sorted_arr[left]==sorted_arr[left-1]:
                        left+=1
        return res