#!/usr/bin/env python3
"""
Module for processing and filtering execution unit data.
"""
import structures

def process_data(jobs_logs):
    """
    Iterates through a dictionary of logs, where PID is the key
    and returns a list of execution units along with their corresponding durations.
    """
    all_jobs_status = []

    for pid, logs in jobs_logs.items():
        job = structures.Job(pid)

        for log in logs:
            job.set_description(log.description)

            if log.status == " START":
                job.set_start_timestamp(log.timestamp)
            if log.status == " END":
                job.set_stop_timestamp(log.timestamp)

        job.calculate_duration()
        all_jobs_status.append(job)

    return all_jobs_status

def filter_data(jobs_status):
    """
    Iterates through a list of execution units and returns a list of
    warning or error messages if an execution unit exceeds a certain threshold.
    """
    bad_jobs_msg = []

    for job in jobs_status:
        msg_type = None
        limit = None

        if job.minutes_duration > 10:
            msg_type = "ERROR"
            limit = 10
        elif job.minutes_duration > 5:
            msg_type = "WARNING"
            limit = 5

        if msg_type and limit:
            bad_jobs_msg.append(f"{msg_type}: Execution Unit with PID={job.pid} and "
                                f"description=\"{job.description}\""
                                f" took longer than {limit} mins({job.minutes_duration} mins)")

    return bad_jobs_msg
