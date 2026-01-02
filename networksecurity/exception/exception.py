import sys
from networksecurity.logging.logger import logging


"""
This module defines a custom exception class used across the Network Security
application to provide detailed and structured error reporting.

The `NetworkSecurityException` class captures contextual information about an
exception, including the file name and line number where the error occurred,
making debugging and logging more informative and consistent across the project.

Args:
    error_message (_type_): The original exception message.
    error_details (_type_): System exception details obtained using the `sys` module.

Returns:
    _type_: Formatted exception message with file name, line number, and error details.
"""


class NetworkSecurityException(Exception):
    def __init__(self,error_message, error_details):
        super().__init__(error_message)

        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return ("Error occurred in the python script [{0}] in line number [{1}] and the error is [{2}]").format(self.file_name, self.lineno, self.error_message)
    
# if __name__ == "__main__":
#     try:
#         logging.info("Entered the try block")
#         a=1/0
#         print("this will not be printed", a)
#     except Exception as e:
#         logging.info(NetworkSecurityException(e, sys))
#         raise NetworkSecurityException(e, sys)