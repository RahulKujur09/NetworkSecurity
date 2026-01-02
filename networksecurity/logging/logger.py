import logging
import os
import sys
from datetime import datetime

"""
This module configures application-wide logging by creating a timestamped log file
inside a dedicated `logs` directory. It ensures the log directory exists, generates
a uniquely named log file based on the current date and time, and initializes the
logging configuration with a standardized format for consistent logging output.

The logger captures informational messages and above, including timestamps, log level,
module name, source filename, line number, and the log message.

Args:
    file_path (_type_): N/A

Returns:
    _type_: None
"""


LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(),"logs")

os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s"
)