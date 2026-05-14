class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_s_list = []
        for char in s:
            if char.isalnum():
                processed_s_list.append(char.lower())
        processed_s = ''.join(processed_s_list)
        left = 0
        right = len(processed_s) - 1
        while left < right:
            if processed_s[left] != processed_s[right]:
                return False
            left += 1
            right -= 1
        return True