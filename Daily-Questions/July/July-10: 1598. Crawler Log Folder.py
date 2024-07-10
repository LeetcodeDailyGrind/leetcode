class Solution:
    def minOperations(self, logs: List[str]) -> int:
        further_away = 0

        for log in logs:
            if log == "../" and further_away == 0:
                continue
            if log == './':
                continue
            if log == "../":
                further_away -= 1
            else:
                further_away += 1

        return further_away