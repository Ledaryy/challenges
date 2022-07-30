from typing import List


def test_for_solution() -> None:
    solution = Solution()
    answer = solution.maxProfit([7, 1, 5, 3, 6, 4])
    assert answer == 5
    answer = solution.maxProfit([7, 6, 4, 3, 1])
    assert answer == 0


class UnOptimasedSolution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            bought_at_price = prices[i]
            for curr_price in prices[i + 1 :]:
                curr_profit = curr_price - bought_at_price
                if curr_profit > profit:
                    profit = curr_profit

        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


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
