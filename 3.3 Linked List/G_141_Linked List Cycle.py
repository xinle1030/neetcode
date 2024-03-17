from typing import Optional

"""
Detect loop in a linked list using Floyd’s Cycle-Finding Algorithm:
It uses two pointers one moving twice as fast as the other one. 
- The faster one is called the faster pointer.
- The other one is called the slow pointer.

Time Complexity: O(N)
Space Complexity: O(1)

why this algo works: https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/

Similar to Leetcode 142_LinkedList Cycle II

References: https://youtu.be/gBTe7lFR3vc?si=BuD7JOQotMOZ8F_X
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # iterative
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head

        # if fast_pointer catch up with slow pointer, there is a cycle
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer is fast_pointer:
                return True
        
        return False
    
    # recursive
    def hasCycle(self, head):
        def detect_cycle(slow, fast):
            if not fast or not fast.next:
                return False
            if slow == fast:
                return True
            return detect_cycle(slow.next, fast.next.next)

        if not head or not head.next:
            return False

        return detect_cycle(head, head.next)
