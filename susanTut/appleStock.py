def solution(stock_prices_yesterday):
    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy /and/ sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be /negative/--we'd return 0!
        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit

def get_max_value(stock):
    if len(stock) <= 1:
        return 0
    else:
        max_profit = 0
        min_price = stock[0]
    for i in range(len(stock)):
        if stock[i] < min_price:
            min_price = stock[i]
        elif stock[i] > min_price:
            max_profit = max(max_profit, stock[i]-min_price)
    if min_price != stock[0] and max_profit==0:
        return -1
    return max_profit

if __name__ == '__main__':
    assert solution([1,2,3,4,5,6,7,8]) == get_max_value([1,2,3,4,5,6,7,8])
    assert solution([8,7,6,5,4,3,2,1]) == get_max_value([8,7,6,5,4,3,2,1])
    assert solution([12,43,5,8,34,2,6,8,34,34,6,23,6,23,1,4,63,8,73,68,42,12,4,4,5]) \
           == get_max_value([12,43,5,8,34,2,6,8,34,34,6,23,6,23,1,4,63,8,73,68,42,12,4,4,5])
    assert solution([1,1,1,1,1,1]) == get_max_value([1,1,1,1,1,1])
    print("All tests passed")