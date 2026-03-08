import argparse
import re

def parse_arguments():
    parser = argparse.ArgumentParser(description="Log Analyzer")

    parser.add_argument("file", help="Path to log file")
    return parser.parse_args()

args = parse_arguments()

file_path = args.file

with open(file_path, 'r') as file:
    for line in file:
        clean_line = line.strip()
        if not clean_line:
            continue
        ip_address, time, method, endpoint, request, status = re.split(r'["\-\[\]\s]+', clean_line)
        print(f"IP: {ip_address}, Time: {time}, Method: {method}, Endpoint: {endpoint}, Request: {request}, Status: {status}")