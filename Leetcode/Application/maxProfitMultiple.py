#TODO: Redo this problem 
#Instructions: You are given an array prices where prices[i] is the price of a given stock on the ith day. Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times). Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
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