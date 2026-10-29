# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Create a gap of n nodes between slow and fast
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast falls off the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Skip the target node
        slow.next = slow.next.next

        return dummy.next