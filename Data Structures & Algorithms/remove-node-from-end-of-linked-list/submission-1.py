# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Count the length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Target is at index (length - n) from the start
        target = length - n

        # Removing the head has no prev
        if target == 0:
            return head.next

        prev = None
        curr = head
        for _ in range(target):
            prev = curr
            curr = curr.next

        # Your unlink logic
        temp = curr.next
        curr.next = None
        prev.next = temp

        return head