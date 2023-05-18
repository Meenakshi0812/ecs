# app.py

import datetime

def get_current_time():
    current_time = datetime.datetime.now()
    return str(current_time)

if __name__ == '__main__':
    print(f"The current time is: {get_current_time()}")
