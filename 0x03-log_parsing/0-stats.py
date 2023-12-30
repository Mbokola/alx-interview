#!/usr/bin/python3
""" 0-stats module parses log files """
import sys

total_file_size = 0
status_codes = []

try:
    for count, line in enumerate(sys.stdin, start=1):
        try:
            status_code = line.split()[-2]
        except IndexError:
            status_code = ""
        try:
            file_size = line.split()[-1]
        except IndexError:
            file_size = "0"
        try:
            total_file_size += int(file_size)
        except ValueError:
            pass
        status_codes.append(status_code)
        if count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in ["200", "301", "400", "401", "403", "404", "405",
                         "500"]:
                if status_codes.count(code):
                    print(f"{code}: {status_codes.count(code)}")

except KeyboardInterrupt:
    pass

finally:
    print(f"File size: {total_file_size}")
    for code in ["200", "301", "400", "401", "403", "404", "405", "500"]:
        if status_codes.count(code):
            print(f"{code}: {status_codes.count(code)}")
