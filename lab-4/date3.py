from datetime import datetime

dt_with_microseconds = datetime.now()

dt_without_microseconds = dt_with_microseconds.replace(microsecond=0)

print(dt_with_microseconds)

print(dt_without_microseconds)
 
