from typing import List


def test_for_solution():
    solution = Solution()
    answer = solution.removeDuplicates([1, 1, 2])
    # assert answer == [1,2]
    assert answer == 2
    answer = solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    # assert answer == [0,1,2,3,4]
    assert answer == 5


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return len(set(nums))


if __name__ == "__main__":
    try:
        test_for_solution()
        print("All tests passed")
    except Exception as e:
        raise e
