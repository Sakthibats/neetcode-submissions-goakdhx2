# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        #1->2->3
        #prev = none. curr = 1 (head)
        #temp = 1.next (2)
        #curr.next = prev (1.next = none)
        #prev = 1, curr = 2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        return prev