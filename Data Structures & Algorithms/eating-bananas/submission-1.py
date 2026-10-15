class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ok(k: int) -> bool:
            time = 0
            for size in piles:
                time += math.ceil(size / k)
            
            return time <= h
        
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo if ok(lo) else -1