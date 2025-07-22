import sys
import logging


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in Python script [{0}] at line [{1}]: [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Optional: set up logging format
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero error caught.")
        raise CustomException(e, sys)
