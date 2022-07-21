def test_for_solution():
    solution = Solution()
    answer = solution.longestCommonPrefix(["flower", "flow", "flight"])
    assert answer == "fl"
    answer = solution.longestCommonPrefix(["dog", "racecar", "car"])
    assert answer == ""
    answer = solution.longestCommonPrefix([""])
    assert answer == ""
    answer = solution.longestCommonPrefix(["a"])
    assert answer == "a"
    answer = solution.longestCommonPrefix(["", ""])
    assert answer == ""
    answer = solution.longestCommonPrefix(["", "b"])
    assert answer == "b"


class Solution:
    def longestCommonPrefix(self, strs) -> str:

        common_prefix = ""

        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return common_prefix
            common_prefix += strs[0][i]
        return common_prefix


if __name__ == "__main__":
    test_for_solution()
    print("All tests passed")
