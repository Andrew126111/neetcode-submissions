class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedArr = sorted(nums)
        ress=[]
        for i in range(len(sortedArr)):
            if i>0 and sortedArr[i-1] == sortedArr[i]:
                continue
            left = i+1
            right = len(sortedArr)-1
            while left<right:
                res = sortedArr[i]+sortedArr[left]+sortedArr[right]
                if res> 0:
                    right-=1
                elif res<0:
                    left+=1
                else:
                    ress.append([sortedArr[i],sortedArr[left],sortedArr[right]])
                    left+=1
                    while left<right and sortedArr[left-1] == sortedArr[left]:
                        left+=1
        return ress
    
