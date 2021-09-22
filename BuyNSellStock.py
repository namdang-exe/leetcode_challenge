prices = [7, 6, 4, 3, 1]


# prices = [7, 1, 5, 3, 6, 4]


# Optimize
def maxProfit(prices):
    max_profit = 0
    profit = 0
    min_price_idx = 0
    for i in range(len(prices)):
        if prices[i] < prices[min_price_idx]:
            min_price_idx = i
        profit = prices[i] - prices[min_price_idx]
        if max_profit < profit:
            max_profit = profit

    return max_profit


print(maxProfit(prices))
