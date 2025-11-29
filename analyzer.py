import re

def analyze_logs(log_file):
    error_count = 0
    warning_count = 0
    user_connects = 0

    with open(log_file, "r") as f:
        for line in f:
            if "ERROR" in line:
                error_count += 1
            if "WARNING" in line:
                warning_count += 1
            if "connected" in line:
                user_connects += 1

    print("===== Log Analysis Report =====")
    print(f"Total Errors: {error_count}")
    print(f"Total Warnings: {warning_count}")
    print(f"User Connections: {user_connects}")


if __name__ == "__main__":
    analyze_logs("network_logs.txt")


