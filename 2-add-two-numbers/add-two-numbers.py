# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        t1 = l1
        t2 = l2
        carry = 0
        dummy = ListNode(-1)
        curr = dummy
        sum = 0
        while(t1 != None or t2 != None):
            sum = carry
            if(t1):
                sum = sum + t1.val
                t1 = t1.next
            if(t2):
                sum = sum + t2.val
                t2 = t2.next

            new_node = ListNode(sum % 10)
            carry = sum // 10

            curr.next = new_node
            curr = curr.next

            # if(t1):
            #     t1 = t1.next
            # if(t2):
            #     t2 = t2.next
        
        if carry != 0:
            new_node = ListNode(carry)
            curr.next = new_node

        return dummy.next


        

            
        