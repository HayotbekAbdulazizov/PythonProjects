time_ = str(input('Time >>>  '))
hour = time_.split(':')[0]
minute = time_.split(':')[1]
time_ = int(hour) + 7
if time_ > 24:
    time_ -= 24
print(f"{time_}:{minute}")
