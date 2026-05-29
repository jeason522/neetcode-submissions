class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            hours = 0
            m = l + (r - l) // 2
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours <= h:
                r = m
            else:
                l = m + 1
        return l