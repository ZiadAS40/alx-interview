#!/usr/bin/python3
"""make the log parsing logic"""
import sys
import signal


total_size = 0
line_count = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
valid_status_codes = set(status_codes_count.keys())


def print_stats():
    """Print the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handle the keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 9:
                continue

            file_size = parts[-1]
            status_code = parts[-2]

            try:
                file_size = int(file_size)
                total_size += file_size
            except ValueError:
                continue

            if status_code in valid_status_codes:
                status_codes_count[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except Exception as e:
            continue

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
