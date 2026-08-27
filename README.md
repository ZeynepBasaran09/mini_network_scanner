# Mini Network Scanner

A lightweight TCP port scanner written in Python for learning network
programming and basic network reconnaissance concepts.

The project accepts an IP address or hostname, resolves hostnames to IP
addresses, scans a user-defined port range, and identifies open TCP ports.

## Features

- Accepts IPv4 addresses and hostnames
- Resolves hostnames to IPv4 addresses
- Scans custom TCP port ranges
- Detects open ports using TCP connections
- Configurable socket timeout
- Concurrent port scanning with `ThreadPoolExecutor`
- Displays common services associated with well-known ports
- Measures total scan duration
- Handles invalid/unresolvable hostnames

## Technologies

- Python 3
- `socket`
- `concurrent.futures`
- `time`

No external Python packages are required.

## How It Works

The scanner follows a simple workflow:

1. The user provides an IP address or hostname.
2. If a hostname is provided, it is resolved to an IPv4 address.
3. The user specifies the starting and ending ports.
4. The scanner attempts to establish TCP connections to each port.
5. Open ports are identified based on successful connections.
6. Multiple ports are scanned concurrently using `ThreadPoolExecutor`.
7. Common services are mapped to well-known port numbers.
8. The total scan duration is displayed.

### Scanning Workflow

```text
Target
  |
  v
Hostname / IP
  |
  v
DNS Resolution
  |
  v
Target IP
  |
  v
Port Range
  |
  v
Concurrent TCP Scanning
  |
  v
Open Ports
  |
  v
Common Service Mapping
