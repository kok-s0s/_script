# Created by: kok-s0s
# Last Modified at: Wed Dec 27 14:10:40 2023
# File Name: get_system_info.py

import platform
import socket
import psutil


def get_system_info():
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    return system_info


def get_network_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    network_info = {"Host Name": host_name, "IP Address": ip_address}
    return network_info


def get_cpu_info():
    cpu_info = {
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "CPU Usage": psutil.cpu_percent(interval=1),
    }
    return cpu_info


def get_memory_info():
    memory_info = {
        "Total Memory": round(
            psutil.virtual_memory().total / (1024**3), 2
        ),  # Convert to GB
        "Available Memory": round(psutil.virtual_memory().available / (1024**3), 2),
    }
    return memory_info


def get_disk_info():
    disk_info = {
        "Total Disk Space": round(
            psutil.disk_usage("/").total / (1024**3), 2
        ),  # Convert to GB
        "Free Disk Space": round(psutil.disk_usage("/").free / (1024**3), 2),
    }
    return disk_info


if __name__ == "__main__":
    system_info = get_system_info()
    print("System Information:\n")
    for key, value in system_info.items():
        print(f"{key}: {value}")

    network_info = get_network_info()
    print("\nNetwork Information:\n")
    for key, value in network_info.items():
        print(f"{key}: {value}")

    cpu_info = get_cpu_info()
    print("\nCPU Information:\n")
    for key, value in cpu_info.items():
        print(f"{key}: {value}")

    memory_info = get_memory_info()
    print("\nMemory Information:\n")
    for key, value in memory_info.items():
        print(f"{key}: {value}")

    disk_info = get_disk_info()
    print("\nDisk Information:\n")
    for key, value in disk_info.items():
        print(f"{key}: {value}")