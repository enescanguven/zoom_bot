import pause
from datetime import datetime


t_n=datetime.now()
t_w = datetime.today().weekday()
monday = t_n.day-t_w


print(monday)

pause.until(datetime(2021, 3, 29, 19, 22,55))
print(bitti)
#pause.until(t(2021, t.month, monday+0, 8, 30 ))