def test_for_solution():
    solution = Solution()
    answer = solution.isValid("()")
    assert answer is True
    answer = solution.isValid("()[]{}")
    assert answer is True
    answer = solution.isValid("(]")
    assert answer is False


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")" or char == "]" or char == "}":
                if len(stack) == 0:
                    return False
                if char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    try:
        test_for_solution()
        print("All tests passed")
    except Exception as e:
        print(e)
