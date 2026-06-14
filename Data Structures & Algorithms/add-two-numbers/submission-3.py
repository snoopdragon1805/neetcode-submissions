# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = res = ListNode()
        carry=0
        while l1 and l2:
            val1 = l1.val + l2.val + carry
            if val1>9:
                carry = val1//10
                val1 = val1%10
            else:
                carry=0
            t1 = ListNode(val1)
            res.next = t1
            res = res.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            val1 = l1.val+carry
            if val1>9:
                carry = val1//10
                val1%=10
            else:
                carry=0
            res.next = ListNode(val1)
            res = res.next
            l1 = l1.next
        while l2:
            val1 = l2.val+carry
            if val1>9:
                carry = val1//10
                val1%=10
            else:
                carry=0
            res.next = ListNode(val1)
            res = res.next
            l2 = l2.next

        
        if carry>0:
            res.next = ListNode(carry)
            res = res.next
        return temp.next
