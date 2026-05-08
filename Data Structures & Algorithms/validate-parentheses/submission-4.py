class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []

        for char in s:
            if char in bracketsMap.values():
                # if left bracket
                stack.append(char)
            elif char in bracketsMap:
                # if right bracket
                if not stack or stack.pop() != bracketsMap[char]:
                    return False
            else:
                raise ValueError('invalid character')

        return len(stack) == 0