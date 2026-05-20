class Solution:
    def calculateEatingTime(self, piles: List[int], k: int):
        if k <= 0:
            return float('inf')
        eatingTime = 0
        for pile in piles:
            eatingTime += math.ceil(pile / k)
        return eatingTime

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find eating rate k such that the hours it takes is at most h,
        # but for slightly slower rate k-1, it exceeds h
        left = 1
        right = max(piles)
        while left <= right:
            k = left + (right - left) // 2
            eatingTime = self.calculateEatingTime(piles, k)
            print(left, right, k, eatingTime)
            if eatingTime <= h:
                right = k - 1
            else:
                left = k + 1
        return left
