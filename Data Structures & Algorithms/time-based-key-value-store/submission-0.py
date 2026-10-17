class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list) # key: (timestamp, value)[]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.hm[key]
        lo, hi = 0, len(lst) - 1
        # print(lo, hi)

        # cond: <= timestamp
        # TTTFFF
        # FFFFFF
        while lo < hi:
            mi = lo + (hi - lo + 1) // 2
            if lst[mi][0] <= timestamp:
                lo = mi
            else:
                hi = mi - 1
        
        if lst and lst[lo][0] <= timestamp:
            return lst[lo][1]
        return ""