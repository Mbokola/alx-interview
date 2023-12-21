#!/usr/bin/python3
""" 0-stats module """

import sys
import re

log_entry_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$')

total_file_size = 0
status_codes = []

try:
    for count, line in enumerate(sys.stdin, start=1):
        line = line.strip()
        match = log_entry_pattern.match(line)

        if match:
            ip_address, date, status_code, file_size = match.groups()
            total_file_size += int(file_size)
            status_codes.append(status_code)

        if count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in ["200", "301", "400", "401", "403", "404", "405",
                         "500"]:
                if status_codes.count(code):
                    print(f"{code}: {status_codes.count(code)}")
            total_file_size = 0
            status_codes = []

except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in ["200", "301", "400", "401", "403", "404", "405", "500"]:
        print(f"{code}: {status_codes.count(code)}")
