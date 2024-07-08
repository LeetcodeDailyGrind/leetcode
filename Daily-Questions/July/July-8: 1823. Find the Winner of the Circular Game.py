class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        start = 0  # index
        # [1, 2, 3, 4, 5]
        while len(arr) > 1:
            index_to_leave = (start + k - 1) % len(arr)
            del arr[index_to_leave]
            # index_to_leave -> 1
            # [1, 3, 4, 5]
            start = index_to_leave

        return arr[0]