class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0

        while i < len(formula):
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                curr_map = stack.pop()
                i += 1
                multiplier = ""
                while i < len(formula) and formula[i].isdigit():
                    multiplier += formula[i]
                    i += 1
                if multiplier:
                    multiplier = int(multiplier)
                    for atom in curr_map:
                        curr_map[atom] *= multiplier
                
                for atom in curr_map:
                    stack[-1][atom] += curr_map[atom]
            
            else:
                curr_atom = formula[i]
                i += 1
                while i < len(formula) and formula[i].islower():
                    curr_atom += formula[i]
                    i += 1
                
                count = ""
                while i < len(formula) and formula[i].isdigit():
                    count += formula[i]
                    i += 1

                if count == "":
                    stack[-1][curr_atom] += 1
                else:
                    stack[-1][curr_atom] += int(count)

        final_map = dict(sorted(stack[0].items()))

        res = ""
        for atom in final_map:
            res += atom
            if final_map[atom] > 1:
                res += str(final_map[atom])

        return res