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

