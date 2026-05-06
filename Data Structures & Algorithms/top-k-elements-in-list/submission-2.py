class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in freqs:
            buckets[freqs[num]].append(num)
        result = []
        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result
        raise ValueError('invalid k, must be <= number of distinct elts in nums')