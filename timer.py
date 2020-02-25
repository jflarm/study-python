#!/usr/bin/env python3.7
import time

start_time = time.localtime()
print(f"Start time is {time.strftime('%X', start_time)}")

#Stop timer
input("Press 'Enter' to stop timer ")
stop_time = time.localtime()

#Difference time
print(f"Stop time is {time.strftime('%X', stop_time)}")
print(f"The difference is {(time.mktime(stop_time) - time.mktime(start_time))} seconds")
# print(f"Start time is {start_time}")
# print(f"Stop time is {stop_time}")
# print(f"the mktime function for start_time is {time.mktime(start_time)}")