import datetime

class printHello:

    #constructor
    def __init__(self, date=""):
        self._date = date

    def set_date(self, x):
        self._date = x

    def get_date(self):
        return self._date
    
if __name__ == '__main__':
    obj1 = printHello()

    obj1.set_date(datetime.datetime.now())

    print("Hello World! Today's date and time is ", obj1.get_date())