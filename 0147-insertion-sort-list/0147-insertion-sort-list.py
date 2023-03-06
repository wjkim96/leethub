# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sent = ListNode(float("-inf"), head)
        v = head.next
        head.next = None
        s = sent
        while v:
            # print(v.val)
            tmp = v.next
            v.next = None
            s = sent
            while s:
                if v.val > s.val:
                    post = s
                    s = s.next
                else:
                    break
            post.next = v
            v.next = s
            v = tmp
        ans = sent.next
        return ans
        
        
        
            