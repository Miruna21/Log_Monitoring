#!/usr/bin/env python3
from datetime import datetime

class Log_Data:
    def __init__(self, timestamp, description, status, pid):
        self.timestamp = timestamp
        self.description = description
        self.status = status
        self.pid = pid

    def __str__(self):
        return str(self.timestamp) + " " + self.description + " " + self.status + " " + self.pid

class Job:
    minutes_duration = 0
    start = None
    stop = None

    def __init__(self, pid):
        self.pid = pid

    def set_start_timestamp(self, start_timestamp):
        self.start = start_timestamp

    def set_stop_timestamp(self, stop_timestamp):
        self.stop = stop_timestamp

    def calculate_duration(self):
        if not self.start:
            self.minutes_duration = -1
            return

        if not self.stop:
            self.minutes_duration = -2
            return

        time_pattern = "%H:%M:%S"
        t1 = datetime.strptime(self.start, time_pattern)
        t2 = datetime.strptime(self.stop, time_pattern)

        t_diff = t2 - t1
        self.minutes_duration = int(t_diff.total_seconds() / 60)

    def __str__(self):
        return self.pid + " " + str(self.start) + " " + str(self.stop) + " " + str(self.minutes_duration)

