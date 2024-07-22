class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        max_array = []
        res = []
        rows = len(matrix)
        cols = len(matrix[0])

        # find the max of each column
        for col in range(cols):
            maximum = 0
            index = 0
            for row in range(rows):
                if matrix[row][col] > maximum:
                    maximum = matrix[row][col]
                    index = row
            max_array.append(index)
        # processing max_array and find the corresponding row
        for i in range(len(max_array)):
            row = max_array[i]
            minimum = min(matrix[row])
            if minimum == matrix[row][i]:
                res.append(matrix[row][i])
        return res
        