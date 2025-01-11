import sys
import logging

def err_msg_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error in the script name [{0}] in line [{1}], error message [{2}]".format(
        filename, exc_tb.tb_lineno, str(error))
    return error_msg

class CustomException(Exception):
    def __init__(self, error_msg, error_detail: sys):
        super().__init__(error_msg)
        # Use `err_msg_detail` to process the error message
        self.error_msg = err_msg_detail(error_msg, error_detail)

    def __str__(self):
        return self.error_msg

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Division by zero")
        raise CustomException(e, sys)
