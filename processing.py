#!/usr/bin/env python3
import structures

def process_data(jobs_logs):
    all_jobs = []

    for pid, logs in jobs_logs.items():
        job = structures.Job(pid)

        for log in logs:
            job.set_description(log.description)

            if log.status == " START":
                job.set_start_timestamp(log.timestamp)
            if log.status == " END":
                job.set_stop_timestamp(log.timestamp)

        job.calculate_duration()
        all_jobs.append(job)
        print(job)

    return all_jobs

def filter_data(jobs_status):
    bad_jobs_msg = []

    for job in jobs_status:
        if job.minutes_duration > 10:
            bad_jobs_msg.append("ERROR: Job " + job.pid + " took longer than 10 minutes")
        elif job.minutes_duration > 5:
            bad_jobs_msg.append("WARNING: Job " + job.pid + " took longer than 5 minutes")

    print(bad_jobs_msg)
    return bad_jobs_msg