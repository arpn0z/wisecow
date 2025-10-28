import requests
import logging
from datetime import datetime

# Config
URL = "https://github.com/"      
TIMEOUT = 5                      
LOG_FILE = "app_health.log"

# log
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Status checker
def check_application_health(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        status_code = response.status_code

        if status_code == 200:
            print(f"Application is UP - Status Code: {status_code}")
            logging.info(f"Application is UP - Status Code: {status_code}")
        else:
            print(f"Application is DOWN - Status Code: {status_code}")
            logging.warning(f"Application is DOWN - Status Code: {status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN - Error: {e}")
        logging.error(f"Application is DOWN - Error: {e}")


if __name__ == "__main__":
    print(f"Checking health of {URL} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
    check_application_health(URL)