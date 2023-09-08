import datetime as dt
import time


alarm = input("Enter alarm date and time in HH:MM format:")


while True:
    now = dt.datetime.now().strftime("%H:%M")
    if alarm == now:
        print("Time's up")
        break
    else:
        pass
