# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
        
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     stack = []
    #     while head.next:
    #         stack.append(head.val)
    #         head = head.next
    #     start = head
    #     while stack:
    #         head.next = ListNode(val=stack.pop())
    #         head = head.next
    #     return start