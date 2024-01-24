import sys


def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name {file_name}\
    line number {exc_tb.tb_lineno} error message {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

''' 
Following is to test the exception file:

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)
# logging.basicConfig(
#     filename = os.path.join(logs_path,LOG_FILE),
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )
    
# if __name__=='__main__':

#     try:
#         a = 1/0
#     except ZeroDivisionError as error:
#         logging.info("division by zero")
#         raise CustomException(error,sys)
'''   