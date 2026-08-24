class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        res=[]
        for indx, val in enumerate(arr):
            if indx>0 and  val == arr[indx-1]:
                continue
            l=indx+1
            r= len(arr)-1
            while l<r:
                threesum = val + arr[l] + arr[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([val,arr[l],arr[r]])
                    l+=1
                    while arr[l] == arr[l-1] and l<r:
                        l+=1
        return res