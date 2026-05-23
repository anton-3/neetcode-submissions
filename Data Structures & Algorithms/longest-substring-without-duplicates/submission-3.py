class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 0
        substr_counts = defaultdict(int)
        substr_counts[s[0]] += 1
        result = 1
        while True:
            right += 1
            if right >= len(s):
                break
            substr_counts[s[right]] += 1
            while substr_counts[s[right]] > 1 and left < right:
                substr_counts[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result