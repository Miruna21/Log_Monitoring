#!/usr/bin/env python3
import structures

def process_data(jobs_logs):
    all_jobs = []

    for pid, logs in jobs_logs.items():
        job = structures.Job(pid)

        for log in logs:
            if log.status == " START":
                job.set_start_timestamp(log.timestamp)
            if log.status == " END":
                job.set_stop_timestamp(log.timestamp)

        job.calculate_duration()
        all_jobs.append(job)
        print(job)

    return all_jobs

def filter_data(jobs_status):
    pass