import logging
import os
from datetime import datetime

try:
    print(f"Current Working Directory: {os.getcwd()}")  # Print the current directory

    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
except Exception as e:
    print(f"Error occurred: {e}")
