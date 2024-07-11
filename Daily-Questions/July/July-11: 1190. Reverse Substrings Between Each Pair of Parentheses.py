class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = deque()
        res = []

        for c in s:
            if c == "(":
                stack.append(len(res))
            elif c == ")":
                start = stack.pop()
                res[start:] = res[start:][::-1]
            else:
                res.append(c)
            
        return "".join(res)