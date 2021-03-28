import webbrowser
import time
from datetime import datetime


chrome_path = '/usr/bin/google-chrome %s'

class Meeting:
  def __init__(self, course, day, hour, mint, url ):
    self.course = course
    self.day = day
    self.hour = hour
    self.mint = mint
    self.url = url

m1 = Meeting("kon214", "28", 8, 30,'https://us05web.zoom.us/j/87840689654?pwd=ZUNZVGo4SVVtWWVNZXpnbXB1L2hQdz09')

print(m1.hour)

#meetin_time = 
an = datetime.now()

print(an.day)

if an.hour >=3:    
    webbrowser.get(chrome_path).open(m1.url)
    time.sleep()

