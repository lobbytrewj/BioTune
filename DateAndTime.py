from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
input = str(today) + "T" + str(dt_string);
print(input)
