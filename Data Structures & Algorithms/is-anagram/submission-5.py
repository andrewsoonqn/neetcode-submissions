class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A = defaultdict(int)

        for sc in s:
            A[sc] += 1
        
        for tc in t:
            A[tc] -= 1

        for cnt in A.values():
            if cnt != 0:
                return False
            
        return True