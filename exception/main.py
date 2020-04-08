import traceback
class CustomException(Exception):
    def __init__(self, cause, messages):
        self.cause = cause
        self.messages = messages

    def __str__(self):
        return " : ".join([self.cause, self.messages])






if __name__ == "__main__":

    try:
        result = 0
        if result :
            print(result)
        else:
            raise CustomException('Result Error', 'The result is {}'.format(result))

    except CustomException as e:
        print(e)

    except Exception as e:
        print(traceback.format_exc())