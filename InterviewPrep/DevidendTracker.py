from collections import defaultdict

class DividendTracker:
    def __init__(self):
        self.dividends = defaultdict(list)  # Store dividends as {stockId: [(day, amount), ...]}

    def addDividend(self, stockId: int, day: int, amount: int):
        """
        Add a dividend for the given stock ID to be paid on a specific day.
        :param stockId: The stock ID
        :param day: The day the dividend is paid
        :param amount: The dividend amount
        """
        self.dividends[stockId].append((day, amount))

    def queryDividend(self, stockId: int, startDay: int, endDay: int) -> int:
        """
        Return the total dividend payment for the given stock ID in the date range [startDay, endDay].
        :param stockId: The stock ID
        :param startDay: The start day of the query range
        :param endDay: The end day of the query range
        :return: The total dividend payment in the range
        """
        return sum(amount for day, amount in self.dividends[stockId] if startDay <= day <= endDay)
