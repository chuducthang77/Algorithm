# Problem #121: Easy

# TODO: Analyze why the solution belows is better than the first solution, why the analyze why maxProfit2 does not work

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    minPrice = 99999999999
    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > profit:
            profit = prices[i] - minPrice

    return profit

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    for i in range(len(prices) - 1):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
    return profit

def maxProfit2(prices):
    minPrice = 99999999
    for price in prices:
        if price < minPrice:
            minPrice = price
        
    profit = 0
    for price in prices:
        if price - minPrice > profit:
            profit = price - minPrice
                    
    return profit

print(maxProfit2([7,1,5,3,6,4]))