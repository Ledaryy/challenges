def test_for_solution():
    solution = Solution()
    answer = solution.validPalindrome("aba")
    assert answer == True
    answer = solution.validPalindrome("abca")
    assert answer == True
    answer = solution.validPalindrome("abc")
    assert answer == False


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    try:
        test_for_solution()
        print("All tests passed")
    except Exception as e:
        raise e
