class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = list(range(n))  # n = 5, indices=[0, 1, 2, 3, 4]
        indices.sort(key = lambda x:positions[x])
        # [4, 3, 2, 1, 0]

        res = []
        stack = []

        for index in indices:
            if directions[index] == 'R':
                stack.append(index)
            else:
                while stack and healths[index] > 0:
                    top_index = stack.pop()

                    if healths[top_index] > healths[index]:
                        healths[top_index] -= 1
                        healths[index] = 0
                        stack.append(top_index)
                    elif healths[top_index] < healths[index]:
                        healths[index] -= 1
                        healths[top_index] = 0
                    else:
                        healths[index] = 0
                        healths[top_index] = 0

        for index in range(n):
            if healths[index] > 0:
                res.append(healths[index])
        return res