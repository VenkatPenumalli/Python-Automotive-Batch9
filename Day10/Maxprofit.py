class StockAnalyzer:
    def __init__(self, prices):
        self.prices = prices
    def calculate_max_profit(self):
        min_price = self.prices[0]
        max_profit = 0
        for price in self.prices[1:]:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
    def calculate_volatility_index(self):
        total_difference = 0
        for i in range(1, len(self.prices)):
            total_difference += abs(self.prices[i] - self.prices[i - 1])
        volatility = total_difference / (len(self.prices) - 1)
        return round(volatility, 2)

prices = list(map(int, input().split()))
analyzer = StockAnalyzer(prices)
print(f"Max Profit: {analyzer.calculate_max_profit()}")
print(f"Volatility Index: {analyzer.calculate_volatility_index():.2f}")
