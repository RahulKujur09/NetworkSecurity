import sys
from networksecurity.logging.logger import logging

class NetworkSecurityException(Exception):
    def __init__(self,error_message, error_details):
        super().__init__(error_message)

        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return ("Error occurred in the python script [{0}] in line number [{1}] and the error is [{2}]").format(self.file_name, self.lineno, self.error_message)
    
if __name__ == "__main__":
    try:
        logging.info("Entered the try block")
        a=1/0
        print("this will not be printed", a)
    except Exception as e:
        logging.info("Entered the except block")
        raise NetworkSecurityException(e, sys)