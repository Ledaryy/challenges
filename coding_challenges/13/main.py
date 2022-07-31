from typing import List


def test_for_solution() -> None:
    solution = Solution()
    answer = solution.fizzBuzz(3)
    assert answer == ["1", "2", "Fizz"]
    answer = solution.fizzBuzz(5)
    assert answer == ["1", "2", "Fizz", "4", "Buzz"]
    answer = solution.fizzBuzz(15)
    assert answer == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(f"{i}")

        return result


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
