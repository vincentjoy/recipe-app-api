# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution(object):
    def maxProfit(self, prices):
        # Edge case: if array has less than 2 elements, no profit possible
        if len(prices) < 2:
            return 0

        min_price = prices[0]  # Track minimum price seen so far
        max_profit = 0         # Track maximum profit possible

        for current_price in prices:
            # Update minimum price if we find a lower price
            min_price = min(min_price, current_price)

            # Calculate potential profit if we sell at current price
            potential_profit = current_price - min_price

            # Update maximum profit if current potential profit is greater
            max_profit = max(max_profit, potential_profit)

        return max_profit