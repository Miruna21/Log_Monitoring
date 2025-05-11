#!/usr/bin/env python3
"""
Parsing module for extracting execution unit data from log files.
"""
import csv
import structures

def read_logs_data(logs_file):
    """
    Parses a file and returns a dictionary
    with PIDs as keys and lists of log entries as values.
    """
    all_jobs_logs = {}

    with open(logs_file, mode='r', encoding='UTF-8') as file:
        logs = list(csv.reader(file))

        for log in logs:
            job_log = structures.LogData(timestamp=log[0], description=log[1],
                            status=log[2], pid=log[3])
            all_jobs_logs.setdefault(job_log.pid, []).append(job_log)

    return all_jobs_logs
