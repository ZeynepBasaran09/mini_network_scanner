import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(target, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.1)

    result = sock.connect_ex((target, port))

    sock.close()

    return result

def scan_single_port(target, port):
    result = scan_port(target, port)

    if result == 0:
        return port

    return None

COMMON_SERVICES = {
    20: "FTP-data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-Proxy"
}

target = input("Target: ").strip()

try:
    target_ip = socket.gethostbyname(target)
    print(f"Resolved IP: {target_ip}")
except socket.gaierror:
    print("Could not resolve target.")
    exit()

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print("\nScanning...\n")

start_time = time.time()

with ThreadPoolExecutor(max_workers=50) as executor:

    futures = [
        executor.submit(scan_single_port, target_ip, port)
        for port in range(start_port, end_port + 1)
    ]

    for future in as_completed(futures):
        port = future.result()

        if port is not None:
          service = COMMON_SERVICES.get(port, "Unknown")
          print(f"{port:<5} OPEN   {service}")

        

end_time = time.time()        

print(f"\nScan completed in {end_time - start_time:.2f} seconds.")