# Write a python program time-based greeting program.

import time

# Get current timestamp
#timestamp = time.time()
#print("Current Timestamp:", timestamp)

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)


t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Sir!")
if(hour>=12 and hour<17):
    print("Good Afternoon Sir!")    
if(hour>=17 and hour<=23):
    print("Good Night Sir!")
    