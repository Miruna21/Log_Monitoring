#!/usr/bin/env python3
import csv
import structures

def read_logs_data(logs_file):
    all_jobs_logs = {}

    with open(logs_file, mode='r', encoding='UTF-8') as file:
        logs = list(csv.reader(file))

        for log in logs:
            timestamp_components = log[0].split(':')
            timestamp = structures.Timestamp(hours=timestamp_components[0],
                            minutes=timestamp_components[1], seconds=timestamp_components[2])
            job_log = structures.Log_Data(timestamp=timestamp, description=log[1],
                            status=log[2], pid=log[3])
            all_jobs_logs.setdefault(job_log.pid, []).append(job_log)

    return all_jobs_logs