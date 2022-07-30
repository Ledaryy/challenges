from typing import Optional


def test_for_solution() -> None:
    solution = Solution()
    answer = solution.getIntersectionNode()
    assert answer == ""
    answer = solution.getIntersectionNode()
    assert answer == ""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Bruteforce
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while headA is not None:
            pB = headB
            while pB is not None:
                if headA == pB:
                    return headA
                pB = pB.next
            headA = headA.next

        return None


# # Time complexity

# Result: O(headA * headB)

# # Space complexity
# The input and output generally do not count towards the space complexity.

# Result: O(1)


if __name__ == "__main__":
    try:
        test_for_solution()
        print("All tests passed")
    except Exception as e:
        raise e
