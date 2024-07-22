class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)

        curr_row_sum = [0] * rows
        curr_col_sum = [0] * cols

        res = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                res[i][j] = min(rowSum[i]  - curr_row_sum[i], colSum[j] - curr_col_sum[j])
                curr_row_sum[i] += res[i][j]
                curr_col_sum[j] += res[i][j]
        
        return res
