class Solution:
    # Approach 1: sort both arrays and use pointer
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]:
            return []

        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        
        return res
    
    # Approach 2: use a freq map
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        for num in nums1:
            map[num] = map.get(num, 0) + 1
        
        res = []
        for num in nums2:
            if num in map.keys() and map.get(num) > 0:
                res.append(num)
                map[num] -= 1
        
        return res
