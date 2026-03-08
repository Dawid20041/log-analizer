import argparse
import re
from collections import Counter
def parse_arguments():
    parser = argparse.ArgumentParser(description="Log Analyzer")

    parser.add_argument("file", help="Path to log file")
    return parser.parse_args()

args = parse_arguments()

file_path = args.file

ip_counter = []
endpoint_counter = []
status_counter = []

with open(file_path, 'r') as file:
    for line in file:
        clean_line = line.strip()
        if not clean_line:
            continue
        ip_address, time, method, endpoint, request, status = re.split(r'["\-\[\]\s]+', clean_line)

        ip_counter.append(ip_address)
        endpoint_counter.append(endpoint)
        status_counter.append(status)

        print(f"IP: {ip_address}, Time: {time}, Method: {method}, Endpoint: {endpoint}, Request: {request}, Status: {status}")
    print(f"Unique IPs: {len(set(ip_counter))}")
    print(f"Unique Endpoints: {len(set(endpoint_counter))}")
    print(f"Unique Status Codes: {len(set(status_counter))}\n")
    print(f"Top 5 IPs: {Counter(ip_counter).most_common(5)}")
    print(f"Top 5 Endpoints: {Counter(endpoint_counter).most_common(5)}")
    print(f"Top 5 Status Codes: {Counter(status_counter).most_common(5)}")