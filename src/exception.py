import sys
import logging
from src.logger import *  # logger sozlamalarini chaqirib olayapti

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"\nError occured in script: [{file_name}]\n"
        f"Line number: [{exc_tb.tb_lineno}]\n"
        f"Error message: {str(error)}"
    )
    
    # Log faylga yozamiz
    logging.error(error_message)

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
