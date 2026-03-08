import argparse
import re
from collections import Counter
def parse_arguments():
    parser = argparse.ArgumentParser(description="Log Analyzer")

    parser.add_argument("file", help="Path to log file")
    return parser.parse_args()

args = parse_arguments()

file_path = args.file

pattern = r'(\d+\.\d+\.\d+\.\d+).*\[(.*?)\]\s+"(\w+)\s+([^ ]+).*"\s+(\d{3})'
errors = []

request_counter = Counter()
ip_counter = Counter()
endpoint_counter = Counter()
status_counter = Counter()

with open(file_path, 'r') as file:
    for line in file:
        clean_line = line.strip()
        if not clean_line:
            continue
        match = re.search(pattern, clean_line)

        if not match:
            continue

        ip_address = match.group(1)
        timestamp = match.group(2)
        method = match.group(3)
        endpoint = match.group(4)
        status = match.group(5)
        if status.startswith('5') or status.startswith('4'):
            errors.append(clean_line)

        request_counter[line] += 1
        ip_counter[ip_address] += 1
        endpoint_counter[endpoint] += 1
        status_counter[status] += 1

def printing():
    print(f"Total Requests: {sum(request_counter.values())}\n")
    print(f"Unique IPs: {len(set(ip_counter))}")
    print(f"Unique Endpoints: {len(set(endpoint_counter))}")
    print(f"Unique Status Codes: {len(set(status_counter))}\n")
    print(f"Top 5 IPs: {ip_counter.most_common(5)}")
    print(f"Top 5 Endpoints: {endpoint_counter.most_common(5)}")
    print(f"Top 5 Status Codes: {status_counter.most_common(5)}")
    print(f"Errors: {len(errors)}")
    print(f"Errors Details:")
    for error in errors:
        print(f"  {error}")
printing()

    