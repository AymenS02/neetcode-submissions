# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1          # keep the nodes, not the values
        curr2 = list2

        dummy = ListNode()
        tail = dummy

        while curr1 and curr2:             # stop when either runs out
            if curr1.val <= curr2.val:     # compare values
                tail.next = curr1          # attach the smaller one
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next               # move tail forward

        tail.next = curr1 if curr1 else curr2   # attach the leftover

        return dummy.next                  # skip the placeholder