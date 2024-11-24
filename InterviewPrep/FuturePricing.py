class FuturePricing:
    def __init__(self, S, dividends):
        """
        Initialize the FuturePricing object.
        
        :param S: Current stock price (integer)
        :param dividends: List of tuples, where each tuple (A, D) represents
                          the amount of dividend and the day it is paid.
        """
        self.S = S
        self.dividends = dividends  # List of tuples (A, D)

    def UpdateDividend(self, i, A, D):
        """
        Update the i-th dividend to a new amount and day.
        
        :param i: Index of the dividend to update (1-based index)
        :param A: New amount of the dividend
        :param D: New day of the dividend
        """
        self.dividends[i - 1] = (A, D)

    def CalculateFuturePrice(self, F):
        """
        Calculate the future price of the stock on day F.
        
        :param F: The day for which the future price is to be calculated
        :return: The future price of the stock on day F
        """
        future_price = self.S
        for A, D in self.dividends:
            if D <= F:
                future_price -= A
        return future_price
