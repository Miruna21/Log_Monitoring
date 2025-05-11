# Log Monitoring Application

This is a **Log Monitoring Application** in Python that parses and analyzes system logs to detect long-running execution units.

## Files

* **`app.py`**: The main file that starts the entire application.
* **`structures.py`**: Contains data structures for logs and execution units (LogData and Job).
* **`parsing.py`**: Module for extracting execution unit logs from log files.
* **`processing.py`**: Module for processing and filtering execution unit data.
* **`reporting.py`**: Module for writing a report to a file.
* **`logs.log`**: Log file example.
* **`report.out`**: Report file.

## Modules and Functionality

### 1. **Log Monitoring**

* Parses system logs to identify long-running execution units.

### 3. **Data Structures**

* **LogData**: Represents log entry data.
* **Job**: Represents an execution unit and calculates its duration.

### 2. **Parsing Module**

* Parses a file and returns a dictionary with PIDs as keys and lists of log entries as values.

### 4. **Processing Module**

* Iterates through a dictionary of logs, where PID is the key and returns a list of execution units along with their corresponding durations.
* Iterates through a list of execution units and returns a list of warning or error messages if an execution unit exceeds a certain threshold.

### 5. **Reporting Module**

* Iterates through a list of warnings and errors for faulty execution units and writes these messages to a file.

## Installation

```bash
git clone <repository_url>
cd <repository_folder>
```

## Usage

```bash
python3 app.py
```
