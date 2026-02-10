"""
Problem: Best Time to Buy and Sell Stock
Approach:
- Track minimum price and maximum profit in one pass

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


if __name__ == "__main__":
    print(max_profit([7,1,5,3,6,4]))  # 5
