# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def merged(listt):
            curr = 0
            count = 0
            while listt:
                curr += listt.val*(10**count)
                listt = listt.next
                count+=1
            return curr
        
        final = str(merged(l1) + merged(l2))
        newhead = new = ListNode()
        for i in final[::-1]:
            new.next = ListNode(int(i))
            new = new.next
        return newhead.next

        
