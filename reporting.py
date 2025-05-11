#!/usr/bin/env python3
"""
Module for writing a report to a file.
"""

def write_report(bad_jobs_msg, report_file):
    """
    Iterates through a list of warnings and errors for faulty execution units
    and writes these messages to a file.
    """
    with open(report_file, mode='a', encoding='UTF-8') as file:
        for job_msg in bad_jobs_msg:
            file.write(job_msg)
            file.write('\n')
