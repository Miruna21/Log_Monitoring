#!/usr/bin/env python3

def write_report(bad_jobs_msg, report_file):
    with open(report_file, 'a') as file:
        for job_msg in bad_jobs_msg:
            file.write(job_msg)
            file.write('\n')
