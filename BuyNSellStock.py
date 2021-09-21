prices = [1, 5, 3, 2, 8, 9]


def maxProfit(prices):
    max_profit = 0
    profit = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            profit = prices[j] - prices[i]
            if max_profit < profit:
                max_profit = profit

    return max_profit


print(maxProfit(prices))
