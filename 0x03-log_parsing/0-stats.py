#!/usr/bin/python3
'''A script to analyze HTTP request logs and track metrics.
'''
import re


def parse_log_line(log_line):
    '''Parses an HTTP log line and extracts relevant metrics.

    Args:
        log_line (str): A single line from the log.

    Returns:
        dict: A dictionary containing the status code and file size.
    '''
    regex_patterns = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_format = '{}\\-{}{}{}{}\\s*'.format(*regex_patterns)
    match = re.fullmatch(log_format, log_line)
    result = {'status_code': 0, 'file_size': 0}

    if match is not None:
        result['status_code'] = match.group('status_code')
        result['file_size'] = int(match.group('file_size'))

    return result


def display_metrics(file_size_sum, status_counts):
    '''Displays the current metrics: total file size and status code counts.

    Args:
        file_size_sum (int): The sum of all file sizes processed so far.
        status_counts (dict): A dictionary with the counts of each status code.
    '''
    print(f"File size: {file_size_sum}", flush=True)
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}", flush=True)


def update_metrics_from_line(log_line, file_size_sum, status_counts):
    '''Updates the file size and status code counts from a single log line.

    Args:
        log_line (str): The log line to process.
        file_size_sum (int): Current sum of file sizes.
        status_counts (dict): Current counts of each status code.

    Returns:
        int: The updated file size sum.
    '''
    log_data = parse_log_line(log_line)
    status_code = log_data['status_code']

    if status_code in status_counts:
        status_counts[status_code] += 1

    return file_size_sum + log_data['file_size']


def log_parser():
    '''Runs the main log parser that reads from input and tracks metrics.
    '''
    lines_processed = 0
    total_file_size = 0
    status_code_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }

    try:
        while True:
            log_line = input()
            total_file_size = update_metrics_from_line(
                log_line,
                total_file_size,
                status_code_counts
            )
            lines_processed += 1

            if lines_processed % 10 == 0:
                display_metrics(total_file_size, status_code_counts)
    except (KeyboardInterrupt, EOFError):
        display_metrics(total_file_size, status_code_counts)


if __name__ == '__main__':
    log_parser()
