class Solution:
    # delimiter const

    def encode(self, strs: List[str]) -> str:
        DEL = '#'
        msg = ""

        for s in strs:
            ns = len(s)
            msg += str(ns) + DEL + s
        
        print(f"{msg=}")
        return msg

    # ["Hello", "World"] -> "5#Hello5#World"
    def decode(self, s: str) -> List[str]:
        DEL = '#'
        ans = []
        p1 = 0
        p2 = 0

        while p1 < len(s):
            while s[p2] != DEL:
                p2 += 1

            ns = int(s[p1:p2])
            print(f"{ns=}") # 5

            p1 = p2 + 1 # to right of delimiter
            p2 += ns + 1 # to right of last letter

            si = ""
            while p1 != p2:
                si += s[p1]
                p1 += 1
            ans.append(si)

        return ans

        





