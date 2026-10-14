class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        st = set()
        n = len(board)
        
        for row in board:
            for x in row:
                if x in st:
                    return False
                if x != ".":
                    st.add(x)
            st.clear()
        
        for c in range(n):
            for row in board:
                x = row[c]
                if x in st:
                    return False
                if x != ".":
                    st.add(x)    
            st.clear()
        
        def checkGrid(i, j):
            nonlocal st
            for r in range(3):
                for c in range(3):
                    x = board[i + r][j + c]
                    print(f"{i+r=} {j+c=} {x=} {st=}")
                    if x in st:
                        return False
                    if x != ".":
                        st.add(x)
            st.clear()
            return True

        for i in range(0, n - 1, 3):
            for j in range(0, n - 1, 3):
                if checkGrid(i, j):
                    continue
                return False
        
        return True
        
