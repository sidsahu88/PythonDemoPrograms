class Stock:    
    def __init__(self, name, shares, prices):
        self.name = name
        self.shares = shares
        self.prices = prices

    def addShares(self, n_shares):
        self.shares += n_shares
    
    def reduceShares(self, n_shares):
        self.shares -= n_shares


class StockTransaction:
    def __init__(self, name, buyOrSell, shares):
        self.name = name
        self.buyOrSell = buyOrSell
        self.shares = shares

    def buyStock(self, stock: Stock, n_shares: int):
        self.shares = n_shares
        stock.addShares(n_shares)
        return stock 

    def sellStock(self, stock: Stock, n_shares: int):
        self.shares = n_shares
        stock.reduceShares(n_shares)
        return stock


def compute_moving_average(data, window_size):
    if window_size <= 0:
        raise ValueError("Window size must be positive")
    if window_size > len(data):
        raise ValueError("Window size must not be larger than data length")
    
    moving_avg = []
    for i in range(len(data) - window_size + 1):
        avg = sum(data[i:i+window_size]) / window_size
        moving_avg.append(round(avg, 2))

    return moving_avg


def printTransactions(m, k, d, stocks_data):
    stock_lists = []

    for i in range(0, k):
        data = stocks_data[i].split()
        stock = Stock(data[0], int(data[1]), list(map(float, data[2:])))
        stock_lists.append(stock)

    transactions = []

    curr_day = 1

    while(curr_day <= d):
        curr_day += 1
        for stock in stock_lists:
            prices = stock.prices
            curr_stock_price = prices[-1]
            moving_average = compute_moving_average(prices[:-1], 4)
            trans = StockTransaction(stock.name, "BUY", 0)

            if moving_average[-1] < curr_stock_price and curr_stock_price < d:
                shares_to_buy = int(m // curr_stock_price)
                m -= (shares_to_buy * curr_stock_price)
                stock = trans.buyStock(stock, shares_to_buy)
            elif moving_average[-1] > curr_stock_price:
                shares_to_sell = stock.shares
                m += (shares_to_sell * curr_stock_price)
                trans.buyOrSell = "SELL"
                stock = trans.sellStock(stock, shares_to_sell)
            else:
                continue
            transactions.append(trans)

    for stock_trans in transactions:
        print(stock_trans.name, stock_trans.buyOrSell, stock_trans.shares)


if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().splitlines()
    m, k, d = map(int, input_data[0].split())
    printTransactions(m, k, d, input_data[1:])
