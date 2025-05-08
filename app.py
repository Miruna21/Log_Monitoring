#!/usr/bin/env python3
import parsing
import processing
import reporting

LOGS_FILE = "./logs.log"
REPORT_FILE = "./report.out"

if __name__ == "__main__":
    logs_data = parsing.read_logs_data(LOGS_FILE)
    logs_status = processing.process_data(logs_data)
    reporting.write_report(logs_status, REPORT_FILE)
