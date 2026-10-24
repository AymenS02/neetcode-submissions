# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while curr:
            nxt = curr.next   # save the rest of the list
            curr.next = prev  # flip the pointer backwards
            prev = curr       # move prev forward
            curr = nxt        # move curr forward

        return prev  # prev ends on the old tail, which is the new head