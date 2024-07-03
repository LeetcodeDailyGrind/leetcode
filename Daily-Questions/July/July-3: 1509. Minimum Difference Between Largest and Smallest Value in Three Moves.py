class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        # Step 1: sorting
        nums.sort()

        minimum = float('inf')  # Integer.MAX_VALUE in java
        right = -4
        # left go from index 0 to 3
        for left in range(4):
            diff = nums[right] - nums[left]
            minimum = min(minimum, diff)
            right += 1
        
        return minimum