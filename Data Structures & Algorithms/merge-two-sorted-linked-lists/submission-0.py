# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        
        head = ListNode()
        last = head

        ptr1 = list1
        ptr2 = list2
        while ptr1 != None and ptr2 != None:
            print('comparing: ptr1.val(' + str(ptr1.val) + ') AND ptr2.val(' + str(ptr2.val) + ')')
            if ptr1.val <= ptr2.val:
                last.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                last.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            last = last.next

        #check if any trailing remains to append
        if ptr1 != None:
            last.next = ptr1
        if ptr2 != None:
            last.next = ptr2
        
        return head.next