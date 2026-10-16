class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ok(k):
            total = 0
            for p in piles:
                total += (p + k - 1) // k
            
            return total <= h

        # find first true
        # FFFTTT
        lo, hi = 1, max(piles)
        first_true = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if ok(mid):
                first_true = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return first_true