class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if y > x:
            high = "ba"  #high[0] and high[1]
            high_score = y
            # low = "ab"
            low_score = x
        else:
            high = "ab"
            high_score = x
            low_score = y
        
        stack = []
        for c in s:
            if c == high[1] and stack and stack[-1] == high[0]:
                res += high_score
                stack.pop()
            else:
                stack.append(c)
        
        new_stack = []
        for c in stack:
            if c == high[0] and new_stack and new_stack[-1] == high[1]:
                res += low_score
                new_stack.pop()
            else:
                new_stack.append(c)

        return res
