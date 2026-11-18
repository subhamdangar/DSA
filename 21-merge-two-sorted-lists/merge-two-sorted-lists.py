# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        curr = ListNode(0)
        head = curr
        while((list1 != None) and (list2 != None)):
            if(list1.val <= list2.val):
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next

        while(list1 is not None):
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        while(list2 is not None):
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        
        return head.next