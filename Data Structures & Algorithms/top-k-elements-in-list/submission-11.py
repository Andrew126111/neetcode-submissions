class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: count (same as before)
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        # Step 2: make n + 1 empty buckets
        buckets = [[] for i in range(len(nums) + 1)]

        # Step 3: put each number into the bucket at index = its count
        for num, c in count.items():
            buckets[c].append(num)

        # Step 4: walk buckets from the end, collect numbers until you have k
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        