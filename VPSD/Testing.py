import os

my_file = 'C:\\users\\chethan.r\\desktop\\Interface_files'
print(my_file)
import datetime

timestamp = datetime.datetime.now().strftime("%m%d%y%H")

print(timestamp)

lists = os.listdir(my_file)

zip_files = []

for files in lists:
    if files.endswith(".csv"):
        f = files
        zip_files.append(f)

print("Files are = ", zip_files)

choped_files = []
for filess in zip_files:
    ff = filess.split("_")[0]
    choped_files.append(ff)

print("chopped files = ", choped_files)

count = 0
for ch in choped_files:
    if ch == 'Stop':
        print("stop file is present")
        count = count + 1
    elif ch == 'StopOnRoute':
        print("stop on route file is present")
        count = count + 1
    elif ch == 'StopDistance':
        print("stop distance file is present")
        count = count + 1
    elif ch == 'Schedule':
        print("schedule file is present")
        count = count + 1
    elif ch == 'ScheduleForRoute':
        print("schedule for route file is present")
        count = count + 1
    elif ch == 'ScheduleForStopOnRoute':
        print("Schedule For Stop on route file is present")
        count = count + 1
    elif ch == 'Route':
        print("Route file is present")
        count = count + 1

print("count = ", count)
