from typing import Optional


def test_for_solution() -> None:
    solution = Solution()
    answer = solution.test_task()
    assert answer == ""
    answer = solution.test_task()
    assert answer == ""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        current_node = head
        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next

        return values == values[::-1]


# # Time complexity

# Result: O(n)

# # Space complexity
# The input and output generally do not count towards the space complexity.

# Result: O(1)


if __name__ == "__main__":
    try:
        test_for_solution()
        print("All tests passed")
    except Exception as e:
        raise e
