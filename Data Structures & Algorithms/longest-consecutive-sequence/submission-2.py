class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create nums set
        # find all unique nums n in that set where n-1 is NOT in the set
        # (the previous doesn't exist, so it's the start of a new sequence)
        # then step through each of those sequences with a while loop for each
        # track longest
        nums_set = set(nums)
        seq_starts = []
        for num in nums_set:
            if num - 1 not in nums_set:
                seq_starts.append(num)
        
        answer = 0

        for num in seq_starts:
            n = num
            while n + 1 in nums_set:
                n += 1
            answer = max(answer, n - num + 1)
        
        return answer