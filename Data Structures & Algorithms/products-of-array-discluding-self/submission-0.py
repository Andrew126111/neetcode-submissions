class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        correct=[]
        for i in range(len(nums)):
            total = 1
            for indx, num in enumerate(nums):
                if indx != i or 0:
                    total *= num
                continue
            correct.append(total)
        return correct
                
                

