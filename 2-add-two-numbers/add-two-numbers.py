# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            curr = head
            prev = None
            after = None
            while curr is not None:
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after

            return prev

        rev_l1 = reverse(l1)
        rev_l2 = reverse(l2)
        curr1 = rev_l1
        curr2 = rev_l2
        st1 = ''
        st2 = ''
        while curr1 is not None:
            st1 = st1 + str(curr1.val)
            curr1 = curr1.next

        while curr2 is not None:
            st2 = st2 + str(curr2.val)
            curr2 = curr2.next

        num = int(st1) + int(st2)
        num1 = str(num)
        num1 = num1[::-1]

        dummy = ListNode(0)
        curr = dummy
        for ch in num1:
            curr.next = ListNode(int(ch))
            curr = curr.next

        return dummy.next
        

        