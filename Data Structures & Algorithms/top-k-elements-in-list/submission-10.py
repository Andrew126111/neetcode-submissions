class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: count (you already wrote this)
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        # Step 2: sort pairs biggest-count first (fix your line from before)
        sorted_pairs = sorted(count.items(),key=lambda x: x[1], reverse=True)

        # Step 3: keep the first k
        top_pairs = sorted_pairs[:k]

        # Step 4: pull out just the numbers
        result = []
        for p in top_pairs:
            result.append(p[0])
        return result
        