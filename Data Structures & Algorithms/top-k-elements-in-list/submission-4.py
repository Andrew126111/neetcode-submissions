class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq =[[] for i in range(len(nums)+1)]
        for i in nums:
            map[i] = map.get(i,0)+1
        
        for n,v in map.items():
            freq[v].append(n)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
            


        