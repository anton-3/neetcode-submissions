class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in indices_map:
                return [indices_map[complement], i]
            indices_map[num] = i
        raise ValueError('No solution found')