class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        def searchRow(r):
            lo, hi = 0, cols - 1

            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if matrix[r][mid] == target:
                    return True
                elif matrix[r][mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            return False
        
        lo, hi = 0, rows - 1
        i = -1 # last true

        # TTTFFF
        # condition = first int is <= target
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] <= target:
                i = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return i != -1 and searchRow(i)
            

