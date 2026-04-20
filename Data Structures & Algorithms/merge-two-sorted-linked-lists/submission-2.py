# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = head = ListNode(0)

        while list1 and list2:
            if list1.val>list2.val:
                temp = list2.next
                head.next = list2
                list2 = temp
                head = head.next
            else:
                temp = list1.next
                head.next = list1
                list1 = temp
                head = head.next
        if list1:
            head.next = list1
        if list2:
            head.next = list2
        return new.next
                
        