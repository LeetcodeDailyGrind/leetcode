class Solution:
    # Approach 1: Brute force
    def passThePillow(self, n: int, time: int) -> int:
        count = 1
        front = True  # direction check
        while time > 0:
            if count == 1:
                front = True
            if count == n:
                front = False
            
            if front:
                count += 1
            else: 
                count -= 1
            
            time -= 1
        
        return count 

    # Approach 2: Math
    def passThePillow(self, n: int, time: int) -> int:
        number_of_turns = time // (n-1)

        if number_of_turns % 2 == 0:
            return 1 + time % (n-1)
        else: 
            return n - (time % (n-1))