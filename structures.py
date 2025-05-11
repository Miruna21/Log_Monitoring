#!/usr/bin/env python3
"""
Module for LogData and Job data structures.
"""
from datetime import datetime
from dataclasses import dataclass

@dataclass
class LogData:
    """
    Log entry data structure.
    """
    def __init__(self, timestamp, description, status, pid):
        self.timestamp = timestamp
        self.description = description
        self.status = status
        self.pid = pid

    def __str__(self):
        return str(self.timestamp) + " " + self.description + " " + self.status + " " + self.pid

class Job:
    """
    Execution unit data structure.
    """
    pid = -1
    description = ""
    minutes_duration = 0
    start = None
    stop = None

    def __init__(self, pid):
        self.pid = pid

    def set_description(self, description):
        """Sets the description for the execution unit"""
        self.description = description

    def set_start_timestamp(self, start_timestamp):
        """Sets the start timestamp for the execution unit"""
        self.start = start_timestamp

    def set_stop_timestamp(self, stop_timestamp):
        """Sets the stop timestamp for the execution unit"""
        self.stop = stop_timestamp

    def calculate_duration(self):
        """Calcutates the duration of the execution unit"""
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
        return (
                self.pid + " " + self.description + " " +
                str(self.start) + " " + str(self.stop) + " " + str(self.minutes_duration)
            )
