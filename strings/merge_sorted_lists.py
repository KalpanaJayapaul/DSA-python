"""
Problem: Merge Two Sorted Linked Lists
Approach:
- Use dummy node
- Compare nodes and merge step by step

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    # Attach remaining nodes
    current.next = l1 if l1 else l2

    return dummy.next
