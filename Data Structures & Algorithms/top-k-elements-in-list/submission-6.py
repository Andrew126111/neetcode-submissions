class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        current = Counter(nums)
        heap =[]

        for num, val in current.items():
            if len(heap) < k:
                heapq.heappush(heap, (val,num))
            else:
                heapq.heappushpop(heap, (val,num))
        return [h[1] for h in heap]