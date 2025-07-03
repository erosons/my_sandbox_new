# when dealing with timestamp in python
import time

# This is checking time from the begining of time todate
print(time.time())

# excute aa process and calculate the time it took to execute the process


def send_emails():
    for i in range(100000000):
        i


start_time = time.time()
send_emails()
end_time = time.time()
duration = start_time-end_time
print(duration)
