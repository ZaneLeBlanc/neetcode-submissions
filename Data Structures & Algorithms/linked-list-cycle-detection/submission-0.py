# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False
        
        cur = head
        double = cur.next
        while cur and double:
            if cur == double:
                return True
            elif double.next == None:
                return False
            else:
                cur = cur.next
                double = double.next.next
        return False
        