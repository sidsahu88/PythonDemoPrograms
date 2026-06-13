def find_max_profit(prices: list) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for i in prices:
        # if i < min_price:
        #     min_price = i
        # elif i - min_price > max_profit:
        #     max_profit = i - min_price
        min_price = min(min_price, i)
        max_profit = max(max_profit, i - min_price)

    return max_profit


if __name__ == "__main__":
    prices_1 = [7, 1, 5, 3, 6, 4]
    print(find_max_profit(prices_1))  # Output: 5

    prices_2 = [7, 6, 4, 3, 1]
    print(find_max_profit(prices_2))

    prices_3 = [1, 2]
    print(find_max_profit(prices_3))

    prices_4 = [2, 1, 3, 4, 1]
    print(find_max_profit(prices_4))
