# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=node=ListNode()
        L1=list1
        L2=list2
        while L1 and L2:
            if L1.val<L2.val:
                node.next=L1
                L1=L1.next
            else:
                node.next=L2
                L2=L2.next
            node=node.next
        node.next=L1 or L2
        return dummy.next


        