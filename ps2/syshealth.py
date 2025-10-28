import psutil
import logging
from datetime import datetime

# ---------------- CONFIGURATION ----------------
CPU_THRESHOLD = 80       # percent
MEMORY_THRESHOLD = 80    # percent
DISK_THRESHOLD = 90      # percent

LOG_FILE = "system_health.log"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- HEALTH CHECK FUNCTIONS ----------------
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {disk_usage}%")
    return disk_usage

def check_processes():
    running_processes = len(psutil.pids())
    logging.info(f"Running processes count: {running_processes}")
    return running_processes

# ---------------- MAIN FUNCTION ----------------
def main():
    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()
    processes = check_processes()

    print(f"System Health Report ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print(f"Running Processes: {processes}")
    print("-" * 50)

    logging.info(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%, Processes: {processes}")

# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    main()