class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        res=[]
        for i in range(len(nums)):
            if i>0 and arr[i] == arr[i-1]:
                continue
            r= len(nums)-1
            l=i+1
            while l<r:
                threesum = arr[i] + arr[r] + arr[l]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([arr[i], arr[l], arr[r]])
                    l+=1
                    while l<r and arr[l] == arr[l-1]:
                        l+=1
        return res
