# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next

        res = [-1, -1]
        if curr.next is None:
            return res

        index = 1
        prev_critical_index = 0
        first_index = 0
        min_distance = float("inf")

        while curr.next:
            if (curr.val < prev.val and curr.val < curr.next.val) or (curr.val > prev.val and curr.val > curr.next.val):
                if prev_critical_index == 0:
                    first_index = index
                    prev_critical_index = index
                else: 
                    # we are here the second time
                    min_distance = min(min_distance, index - prev_critical_index)
                    prev_critical_index = index

            index += 1
            prev = prev.next
            curr = curr.next

        # case to deal with edge case, if we only have 1 critical point 
        # when we have 2 or more critical points
        if min_distance != float("inf"):
            max_distance = prev_critical_index - first_index
            res = [min_distance, max_distance]
        
        return res