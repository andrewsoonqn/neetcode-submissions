class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A = [0] * 26

        for sc in s:
            A[ord(sc) - ord('a')] += 1
        
        for tc in t:
            A[ord(tc) - ord('a')] -= 1

        for cnt in A:
            if cnt != 0:
                return False
            
        return True