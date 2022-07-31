from typing import List


def test_for_solution() -> None:
    solution = Solution()
    answer = solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    assert answer == [1, 2, 2, 3, 5, 6]
    answer = solution.merge([1], 1, [], 0)
    assert answer == [1]
    answer = solution.merge([0], 0, [1], 1)
    assert answer == [1]


# Not a merging..
class SolutionOne:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        merged_array = sorted(nums1[:m] + nums2[:n])

        return merged_array


# Unoptimazed
class SolutionTwo:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        clear_nums1 = nums1[:m]

        for i in range(n + m):

            value_from_nums1 = min(clear_nums1 + [float("inf")])
            value_from_nums2 = min(nums2 + [float("inf")])

            if value_from_nums1 < value_from_nums2:
                nums1[i] = value_from_nums1
                clear_nums1.remove(value_from_nums1)
            else:
                nums1[i] = value_from_nums2
                nums2.remove(value_from_nums2)

        return nums1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i + m] = nums2[i]

        nums1.sort()

        return nums1


# # Time complexity

# Result: O(n^2)

# # Space complexity
# The input and output generally do not count towards the space complexity.

# Result: O(n)


if __name__ == "__main__":
    try:
        test_for_solution()
        print("All tests passed")
    except Exception as e:
        raise e
