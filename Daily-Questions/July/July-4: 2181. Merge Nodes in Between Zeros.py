# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        temp = head
        while curr:
            # we know first will be 0
            value = 0
            while curr.val != 0:
                value += curr.val
                curr = curr.next

            temp.val = value
            temp.next = curr.next
            temp = temp.next

            curr = curr.next
        
        return head