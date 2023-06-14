#!/usr/bin/python3


"""The Log parsing Module"""

import sys

""" Initialize variables for metrics """
total_file_size = 0
status_code_counts = {}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        """Split the line based on the specified format"""
        parts = line.strip().split(' ')
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        """Update total file size"""
        total_file_size += file_size

        """Update status code counts"""
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1

        """Print metrics every 10 lines"""
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_counts):
                count = status_code_counts[code]
                print(f"{code}: {count}")

except KeyboardInterrupt:
    """Print final metrics on keyboard interruption (CTRL + C)"""
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts):
        count = status_code_counts[code]
        print(f"{code}: {count}")
