class Solution:
    # Option 1: Brute Force
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False
    
    # Option 2 : One pass
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cosecutiveOdds = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                cosecutiveOdds += 1
            else:
                cosecutiveOdds = 0
            
            if cosecutiveOdds == 3:
                return True
            
        return False