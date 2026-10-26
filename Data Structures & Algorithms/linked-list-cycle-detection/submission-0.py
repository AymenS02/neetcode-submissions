# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr1 = head
        hasher = set()

        while curr1:

            if curr1 in hasher:
                return True
            
            hasher.add(curr1)
            curr1 = curr1.next



        return False