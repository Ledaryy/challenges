import re


def test_for_solution():
    solution = Solution()
    answer = solution.lengthOfLongestSubstring("abcabcbb")
    assert answer == 3
    answer = solution.lengthOfLongestSubstring("bbbbb")
    assert answer == 1
    answer = solution.lengthOfLongestSubstring("pwwkew")
    assert answer == 3
    answer = solution.lengthOfLongestSubstring("dvdf")
    assert answer == 3
    answer = solution.lengthOfLongestSubstring(" ")
    assert answer == 1


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        output = 0
        
        for right, curr in enumerate(s):
            if curr in seen:
                left = max(left, seen[curr] + 1)
            output = max(output, right - left + 1)
            seen[curr] = right

        return output


if __name__ == "__main__":
    try:
        test_for_solution()
        print("All tests passed")
    except Exception as e:
        raise e
