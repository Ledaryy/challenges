from typing import List


def test_for_solution() -> None:
    solution = Solution()
    answer = solution.test_task()
    assert answer == ""
    answer = solution.test_task()
    assert answer == ""


class Solution:
    def test_task(self) -> str:
        return ""


# # Time complexity

# Result: O()

# # Space complexity
# The input and output generally do not count towards the space complexity.

# Result: O()


if __name__ == "__main__":
    try:
        test_for_solution()
        print("All tests passed")
    except Exception as e:
        raise e
