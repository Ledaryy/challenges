from typing import List


def test_for_solution() -> None:
    solution = Solution()
    answer = solution.containsDuplicate([1, 2, 3, 1])
    assert answer is True
    answer = solution.containsDuplicate([1, 2, 3, 4])
    assert answer is False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False


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
