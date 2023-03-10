# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        while node:
            if node.val == 'v':
                return True
            else:
                node.val = 'v'
                node = node.next
        return False
                