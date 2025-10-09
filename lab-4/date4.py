from datetime import datetime

date1_str = input()

date2_str = input()

date1 = datetime.fromisoformat(date1_str)

date2 = datetime.fromisoformat(date2_str)

time_difference = date2 - date1

print(time_difference.total_seconds())