class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for _ in range(len(nums1) -1 - m):
            # nums1.pop()
        nums1.insert(m, float("inf"))
        print(nums1)
        while n > 0:
            x = nums2.pop(0)
            # print(x)
            # print(nums2)
            for i in range(len(nums1)):
                if x <=nums1[i]:
                    nums1.insert(i, x)
                    nums1.pop()
                    # print(nums1)
                    break;
            n -= 1
        nums1.pop()
        # print(nums1)
                    
        
        