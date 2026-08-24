class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Cor = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sum = nums[i]+nums[j]
                if i==j:
                    continue
                if sum == target:
                    Cor.append(i)
                    Cor.append(j)
                
        return Cor


        