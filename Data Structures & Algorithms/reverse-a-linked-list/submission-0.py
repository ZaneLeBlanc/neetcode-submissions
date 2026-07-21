# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next == None:
            return head

        stk = []
        cur = head
        while cur is not None:
            stk.append(cur)
            cur = cur.next

        newHead = stk.pop()
        cur = newHead
        
        while stk:
            nextt = stk.pop()
            cur.next = nextt
            cur = cur.next
        cur.next = None
        
        return newHead

            
