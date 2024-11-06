import platform
import psutil
import socket
import subprocess
import os

def get_system_info():
    # Collecting basic system information
    info = {}
    
    # System and OS details
    info['System'] = platform.system()
    #Hier andere Infos über Computer und System einfügen

    # Windows-specific details
    if info['System'] == 'Windows':
        info['Windows Version'] = platform.win32_ver()[0]
    
    # MAC address
    hostname = socket.gethostname()
    info['IP Address'] = socket.gethostbyname(hostname)
    try:
        info['MAC Address'] = ':'.join(['{:02x}'.format((psutil.net_if_addrs()['Ethernet'][0].address)).upper()])
    except KeyError:
        info['MAC Address'] = "Could not retrieve MAC Address"

    # Memory (RAM)
    info['Total RAM'] = f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"
    info['Available RAM'] = f"{round(psutil.virtual_memory().available / (1024 ** 3), 2)} GB"

    # Disk usage
    disk_usage = psutil.disk_usage('/')
    info['Total Disk Space'] = f"{round(disk_usage.total / (1024 ** 3), 2)} GB"
    #Ergänze infos über Speicher 

    # Returning all gathered information
    return info

def save_info_to_file(info, file_path):
    # Saving information to the specified file
    with open(file_path, 'w') as f:
        for key, value in info.items():
            f.write(f"{key}: {value}\n")

def run_list_files_script():
    # Running list_files.py located in C:\Python
    list_files_script = r"<path to s_list_all>\s_list_all.py"
    target_directory = r"<path zu Ordner den wir durchsuchen möchten>"  # Example directory
    if os.path.exists(list_files_script):
        subprocess.run(["python", list_files_script, target_directory], shell=True)
    else:
        print(f"{list_files_script} not found. Ensure it exists in C:\Python.")

if __name__ == "__main__":
    # Collect system information
    system_info = get_system_info()
    
    # Define the file path for saving information
    info_file_path = "info.txt"
    
    # Save the system information to info.txt
    save_info_to_file(system_info, info_file_path)
    print(f"System information saved to {info_file_path}")
    
    # Run list_files.py
    run_list_files_script()
