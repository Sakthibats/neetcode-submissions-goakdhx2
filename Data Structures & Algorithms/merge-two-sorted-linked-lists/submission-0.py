# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        finhead = fin = ListNode()
        while list1 or list2:
            if list1 and not list2:
                fin.next = list1
                list1=None
            elif list2 and not list1:
                fin.next = list2
                list2 = None
            elif list1.val<list2.val:
                temp = list1.next
                fin.next = list1
                fin =fin.next
                list1 = temp
            else:
                temp = list2.next
                fin.next = list2
                fin = fin.next
                list2 = temp
        return finhead.next
        