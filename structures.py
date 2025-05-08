#!/usr/bin/env python3

class Timestamp:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return self.hours + ":" + self.minutes + ":" + self.seconds


class Log_Data:
    def __init__(self, timestamp, description, status, pid):
        self.timestamp = timestamp
        self.description = description
        self.status = status
        self.pid = pid

    def __str__(self):
        return str(self.timestamp) + " " + self.description + " " + self.status + " " + self.pid

class Job:
    duration = 0

    def __init__(self, pid):
        self.pid = pid

    def set_start_timestamp(self, start_timestamp):
        self.start = start_timestamp

    def set_stop_timestamp(self, stop_timestamp):
        self.start = stop_timestamp

    def calculate_duration(self):
        pass

    def __str__(self):
        return str(self.timestamp) + " " + self.description + " " + self.status + " " + self.pid

