#!/usr/bin/env python3
import csv
import structures

def read_logs_data(logs_file):
    all_logs_data = []

    with open(logs_file, mode='r', encoding='UTF-8') as file:
        logs = list(csv.reader(file))

        for log in logs:
            timestamp_components = log[0].split(':')
            timestamp = structures.Timestamp(hours=timestamp_components[0],
                            minutes=timestamp_components[1], seconds=timestamp_components[2])
            log_data = structures.Log_Data(timestamp=timestamp, description=log[1],
                            status=log[2], pid=log[3])
            all_logs_data.append(log_data)