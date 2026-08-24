class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums): #[index,value]
            hashmap[n] = i
        #we added all values and indexs to the map
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap and hashmap.get(diff) != i:
                return [i, hashmap.get(diff)]
        return []

        