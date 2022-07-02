def test_for_converter():
    solution = Solution()
    number = solution.romanToInt("XXIV")
    assert number == 24


class Solution:
    def romanToInt(self, s: str) -> int:
        assert len(s) > 0

        roman_settings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        integer_numbers_list = list(s)

        for num, char in enumerate(integer_numbers_list):
            integer_numbers_list[num] = roman_settings[char]

        # [10, 10, 1, 5]
        for i in range(len(integer_numbers_list) - 1):
            if integer_numbers_list[i] < integer_numbers_list[i + 1]:
                integer_numbers_list[i + 1] = (
                    integer_numbers_list[i + 1] - integer_numbers_list[i]
                )
                integer_numbers_list[i] = 0

        return sum(integer_numbers_list)


if __name__ == "__main__":
    test_for_converter()
    print("All tests passed")
