"""
References: https://www.youtube.com/watch?v=q6IEA26hvXc

Do binary search on the list with smaller length
O(log(min(m, n)))
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        totalLen = len(A) + len(B)
        half = totalLen // 2

        # A: smaller list, B: larger list
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            a_mid = (l + r) // 2
            # a_mid + 1 = number of elements in left partition
            # -1 shift index for 0-indexed
            b_mid = half - (a_mid + 1) - 1

            a_left = A[a_mid] if a_mid >= 0 else float('-infinity')
            a_right = A[a_mid + 1] if (a_mid + 1) < len(A) else float('infinity')
            b_left = B[b_mid] if b_mid >= 0 else float('-infinity')
            b_right = B[b_mid + 1] if (b_mid + 1) < len(B) else float('infinity')

            if a_left <= b_right and b_left <= a_right:
                # if odd length
                if totalLen % 2 == 1:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = a_mid - 1
            else:
                l = a_mid + 1

        