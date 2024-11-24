from collections import deque

class LogServer:
    def __init__(self, m):
        """
        Initialize the log server with a maximum number of logs 'm' to return in getLogs().
        """
        self.m = m  # Maximum number of logs to return in getLogs()
        self.logs = []  # Store logs as (logId, timestamp) tuples

    def recordLog(self, logId, timestamp):
        """
        Records a new log with the given logId and timestamp.
        Ignore logs with timestamps earlier than the latest recorded log.
        """
        self.logs.append([logId, timestamp])
        print(self.logs)
        while self.logs and self.logs[0][1] <= self.logs[-1][1] - 3600:  # Remove logs older than an hour
                self.logs.pop(0)

    def getLogs(self):
        """
        Returns a comma-separated string of up to 'm' log IDs from the last hour.
        """
        # After removing invalid logs, take the last `m` logs in order
        valid_logs = list(self.logs)[-self.m:]
        return ",".join(str(log[0]) for log in valid_logs)

    def getLogCount(self):
        """
        Returns the total number of logs received in the last hour.
        """
        return len(self.logs)


def processQueries(m, queries):
    logServer = LogServer(m)
    results = []

    for query in queries:
        parts = query.split()
        if parts[0] == "RECORD":
            logId, timestamp = int(parts[1]), int(parts[2])
            logServer.recordLog(logId, timestamp)
        elif parts[0] == "GET_LOGS":
            results.append(logServer.getLogs())
        elif parts[0] == "COUNT":
            results.append(str(logServer.getLogCount()))

    return results


m = 100
queries = [
    "RECORD 1 0",
    "RECORD 2 300",
    "GET_LOGS",
    "COUNT",
    "RECORD 3 1200",
    "RECORD 1 1800",
    "GET_LOGS",
    "COUNT",
    "RECORD 4 3900",
    "GET_LOGS"
]

results = processQueries(m, queries)
print("\n".join(results))

