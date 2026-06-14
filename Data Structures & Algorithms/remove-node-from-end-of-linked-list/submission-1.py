# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        temp = head
        while(temp):
            l+=1
            temp = temp.next
        temp = head
        prev=None
        for i in range(l-n):
            prev = temp
            temp = temp.next
        if prev == None:
            return head.next
        prev.next = temp.next
        temp.next = None
        return head