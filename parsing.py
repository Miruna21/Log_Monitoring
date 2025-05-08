#!/usr/bin/env python3
import csv
import structures

def read_logs_data(logs_file):
    all_jobs_logs = {}

    with open(logs_file, mode='r', encoding='UTF-8') as file:
        logs = list(csv.reader(file))

        for log in logs:
            job_log = structures.Log_Data(timestamp=log[0], description=log[1],
                            status=log[2], pid=log[3])
            all_jobs_logs.setdefault(job_log.pid, []).append(job_log)

    return all_jobs_logs