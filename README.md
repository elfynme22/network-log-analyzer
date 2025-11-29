# network-log-analyzer

A simple Python-based tool for analyzing network log files.  
It processes a raw log file and reports:
- Total number of errors  
- Total number of warnings  
- Total number of user connection events  

This project demonstrates fundamental log parsing, text processing, and automation concepts often used in network operations and monitoring teams.

---

## Features

- Reads and processes log files line by line  
- Detects:
  - `"ERROR"` occurrences  
  - `"WARNING"` occurrences  
  - `"connected"` user connection events  
- Generates a clean summary report  
- Lightweight and runs entirely locally  
- No external dependencies (pure Python)

---

## Project Structure

```
network-log-analyzer/
│
├── analyzer.py          # Main analysis script
├── network_logs.txt     # Sample log file used for testing
└── README.md            # Documentation
```

---

## How It Works

The script includes a function named `analyze_logs()` which:

1. Opens the log file  
2. Iterates through each line  
3. Increments counters based on keywords:
   - `"ERROR"` → error counter  
   - `"WARNING"` → warning counter  
   - `"connected"` → user connection counter  
4. Prints a clear formatted summary:

```
===== Log Analysis Report =====
Total Errors: X
Total Warnings: Y
User Connections: Z
```

This workflow reflects basic log analysis pipelines commonly used in:
- Network automation  
- Monitoring systems  
- Troubleshooting workflows  

---

## Example Log File

Sample `network_logs.txt` includes various log entries such as:

```
[2025-11-29 10:15:23] INFO User123 connected from 192.168.1.10
[2025-11-29 10:16:01] WARNING High latency detected
[2025-11-29 10:17:05] ERROR Failed to reach server
```

---

## Running the Program

### 1. Navigate to the project folder:

```bash
cd network_log_analyzer
```

### 2. Run the Python script:

```bash
python3 analyzer.py
```

### Expected Output:

```
===== Log Analysis Report =====
Total Errors: 2
Total Warnings: 2
User Connections: 3
```

---

## Purpose of the Project

This mini project demonstrates:

- Basic text processing  
- Foundational log analysis  
- Automation logic in Python  
- Hands-on understanding of network monitoring workflows  
- Ability to build simple tools used in real network operation environments  

It is especially suitable for applications to roles such as:

- AI Automation Intern  
- Network Automation Intern  
- Software Engineering Intern  
- Python Developer Intern  

---

## Technologies Used

- Python 3  
- Terminal environment  
- Text-based log processing  

---

## Author

Elif Aydın  
GitHub: https://github.com/elfynme22  

---

## License

This project is open-source for educational and demonstrational purposes.
