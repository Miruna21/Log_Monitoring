#!/usr/bin/env python3
import parsing
import processing
import reporting

LOGS_FILE = "./logs.log"
REPORT_FILE = "./report.out"

if __name__ == "__main__":
    jobs_logs = parsing.read_logs_data(LOGS_FILE)
    jobs_status = processing.process_data(jobs_logs)
    bad_jobs_msg = processing.filter_data(jobs_status)
    reporting.write_report(bad_jobs_msg, REPORT_FILE)
