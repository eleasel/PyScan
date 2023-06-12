import socket
import concurrent.futures

TARGET = "myjoyonline.com"
PORT_RANGE = [(1, 1000)]  # Add more port ranges if needed


def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((TARGET, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "Unknown"
        print(f"Port {port} is open. Service: {service}")
    sock.close()


def scan_ports(port_range):
    print(f"Scanning ports on {TARGET}...\n")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        scan_tasks = [executor.submit(scan_port, port) for port in range(port_range[0], port_range[1] + 1)]
        for task in concurrent.futures.as_completed(scan_tasks):
            pass


def main():
    print("Port Scanner")
    print("-------------\n")

    # Perform multi-threaded scanning for each port range
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(scan_ports, PORT_RANGE)

    print("\nScanning completed.")


if __name__ == '__main__':
    main()
