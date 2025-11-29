# network-dashboard

A simple Python-based network traffic dashboard.  
This project reads a CSV file containing basic network traffic metrics and prints a summary report to the terminal.

It was developed as a mini project to demonstrate foundational monitoring, data processing and automation logic for network-related use cases.

---

## Features

- Reads network traffic data from a CSV file  
- Calculates total and average incoming/outgoing traffic  
- Counts total error events  
- Identifies peak traffic times (highest in/out values)  
- Produces a clear, terminal-based summary report  
- Uses only Python standard libraries (no external dependencies)

---

## Project Structure

```
network-dashboard/
│
├── dashboard.py      # Main script: loads CSV, analyzes data, prints summary
├── network_data.csv  # Sample network traffic dataset
└── README.md         # Project documentation
```

---

## How It Works

1. `dashboard.py` loads the CSV file using Python's built-in `csv` module.  
2. Each row includes:
   - `timestamp`
   - `traffic_in`
   - `traffic_out`
   - `errors`
3. The script:
   - Sums traffic values  
   - Computes averages  
   - Tracks total errors  
   - Detects the timestamp with highest `traffic_in` and `traffic_out`
4. Prints a structured report to the terminal.

This replicates the basic behavior of lightweight monitoring dashboards used in network operations.

---

## Running the Project

From the project folder:

```bash
python3 dashboard.py
```

Ensure `dashboard.py` and `network_data.csv` are in the same directory.

---

## Author

Elif Aydın  
GitHub: https://github.com/elfynme22
