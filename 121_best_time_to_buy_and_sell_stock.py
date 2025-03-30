"""
🔵 LeetCode 121: Best Time to Buy and Sell Stock

You are given an array 'prices' where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

-----------------------------------
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profitable transaction is possible, so the output is 0.

-----------------------------------
Constraints:
    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^4
"""

from typing import List

def max_profit(prices: List[int]) -> int:
    """
    Optimal Two-Pointer Approach (Using left and right pointers)

    Approach:
      - Initialize two pointers: 'l' (buy day) and 'r' (sell day), with l = 0 and r = 1.
      - As we iterate, if prices[l] is less than prices[r], compute the profit (prices[r] - prices[l])
        and update the maximum profit.
      - If prices[l] is not less than prices[r], then a new potential buy day is found, so update l to r.
      - Increment r until the end of the list.
      - Return the maximum profit found.

    Time Complexity: O(n), where n is the number of days (length of prices).
    Space Complexity: O(1), constant space usage.

    Parameters:
        prices (List[int]): List of stock prices on consecutive days.
    
    Returns:
        int: The maximum profit that can be achieved.
    """
    l, r = 0, 1
    max_profit_val = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit_val = max(max_profit_val, profit)
        else:
            l = r
        r += 1
    return max_profit_val

    # if not prices:
        # return 0

    # min_price = float('inf')
    # max_profit_val = 0

    # for price in prices:
        # if price < min_price:
            # min_price = price  # Update minimum price so far
        # else:
            # max_profit_val = max(max_profit_val, price - min_price)  # Update maximum profit

    # return max_profit_val

# Sample Test Cases
if __name__ == "__main__":
    # Example 1:
    prices1 = [7, 1, 5, 3, 6, 4]
    print("Example 1 Output:", max_profit(prices1))  # Expected: 5

    # Example 2:
    prices2 = [7, 6, 4, 3, 1]
    print("Example 2 Output:", max_profit(prices2))  # Expected: 0

# ------------------------------------------------
# ✅ Time Complexity: O(n), where n is the number of days.
# ✅ Space Complexity: O(1)
