# Log Analyzer (Python)

A simple command-line tool for analyzing web server log files.
The program parses log entries, extracts useful information, and generates statistics about requests, endpoints, IP addresses, and errors.

## Features

* Parse web server logs using **regular expressions**
* Count total requests
* Detect **unique IP addresses**
* Analyze **most requested endpoints**
* Track **HTTP status codes**
* Identify **4xx and 5xx errors**
* Show **top error-generating endpoints**
* Command line interface using **argparse**

## Technologies Used

* Python 3
* argparse
* regex
* collections.Counter

## Example Log Format

The program expects logs similar to the Apache/Nginx combined log format:

```
192.168.1.10 - - [10/Oct/2025:13:55:36 +0000] "GET /api/users?id=10 HTTP/1.1" 200 532
192.168.1.15 - - [10/Oct/2025:13:55:37 +0000] "POST /api/login HTTP/1.1" 401 210
192.168.1.20 - - [10/Oct/2025:13:55:38 +0000] "GET /api/products HTTP/1.1" 500 1024
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/log-analyzer.git
cd log-analyzer
```

No additional dependencies are required.

## Usage

Run the script from the command line and provide a log file path:

```bash
python log_analyzer.py logs.txt
```

Example output:

```
Total Requests: 150

Unique IPs: 23
Unique Endpoints: 12
Unique Status Codes: 5

Top 5 IPs:
192.168.1.10 -> 15
192.168.1.20 -> 11
...

Top 5 Endpoints:
/api/users -> 32
/api/products -> 28
...

Top 5 Status Codes:
200 -> 120
404 -> 20
500 -> 10

Errors: 30

Top Error Endpoints:
/api/login -> 12
/api/products -> 10
```

## Project Structure

```
log-analyzer/
│
├── log_analyzer.py
├── sample_logs.txt
└── README.md
```

## What the Analyzer Extracts

From each log entry the program extracts:

* IP address
* Timestamp
* HTTP method
* Endpoint
* Status code

Query parameters are automatically removed so endpoints like:

```
/api/users?id=10
/api/users?id=20
```

are grouped as:

```
/api/users
```

## Possible Future Improvements

* Export results to **CSV or JSON**
* Add **visual charts (matplotlib)**
* Detect **suspicious IP activity**
* Add **log filtering options**
* Process **very large logs with multiprocessing**

## License

This project is open source and available under the MIT License.
