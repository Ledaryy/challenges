from typing import List


def test_for_solution() -> None:
    solution = Solution()
    answer = solution.reverseString(["h", "e", "l", "l", "o"])
    assert answer == ["o", "l", "l", "e", "h"]
    answer = solution.reverseString(["H", "a", "n", "n", "a", "h"])
    assert answer == ["h", "a", "n", "n", "a", "H"]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        return s


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
