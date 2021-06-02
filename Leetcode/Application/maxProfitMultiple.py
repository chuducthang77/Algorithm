#TODO: Redo this problem 
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    
    valley = 0
    peak = 0
    i = 0
    length = len(prices)
    profit = 0
    while i < length - 1:
        while i < length -1 and prices[i] <= prices[i+1]:
            i += 1
        peak = prices[i]
        while i < length -1 and prices[i] >=  prices[i+1]:
            i += 1
        valley = prices[i]
        profit += peak - valley
    
    return profit