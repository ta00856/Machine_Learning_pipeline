import logging
import os
from datetime import datetime

# This should just be the directory path, not including the file
logs_directory = os.path.join(os.getcwd(), "logs")
# Ensure the directory exists
os.makedirs(logs_directory, exist_ok=True)

# Now specify the file name and path correctly
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# if __name__ == '__main__':
#     logging.info('logging has started')