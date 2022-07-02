
def test_for_solution():
    solution = Solution()
    answer = solution.test_task()
    assert answer == ""
    answer = solution.test_task()
    assert answer == ""


class Solution:
    def test_task(self) -> str:
        return ""


if __name__ == "__main__":
    try:
        test_for_solution()
        print("All tests passed")
    except Exception as e:
        raise e
