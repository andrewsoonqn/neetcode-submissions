class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        def searchRow(r: int) -> bool:
            # print(f"{matrix[r]=}")
            lo, hi = 0, cols - 1

            while lo < hi:
                mid = lo + (hi - lo) // 2
                if matrix[r][mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            
            if lo < cols and matrix[r][lo] == target:
                return True
            
            return False
        
        lo, hi = 0, rows

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] > target:
                hi = mid
            else:
                lo = mid + 1

        if lo > 0 and searchRow(lo - 1):
                return True
        
        return False
        