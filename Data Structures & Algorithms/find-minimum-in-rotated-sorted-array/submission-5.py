class Solution:
    def findMin(self, nums: List[int]) -> int:
        # edge case: un-rotated array
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        result = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            mid = (left + right) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return result