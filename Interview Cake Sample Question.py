# Interview Cake Sample Question - https://www.interviewcake.com

# My explanation in iPad Notes
def get_max_profit(stock_prices):
    
    # Calculate the max profit
    if not stock_prices or len(stock_prices) == 1:
        raise
    
    # profit = float('-inf')
    buy = stock_prices[0]
    sell = stock_prices[1]
    pros_buy = min(buy, sell)

    for price in stock_prices[2:]:
        if price - pros_buy > sell - buy:
            sell = price
            buy = pros_buy
        
        pros_buy = min(pros_buy, price)

    return sell-buy