import webbrowser
import time
from datetime import datetime
import json

monday = datetime.now().day-datetime.today().weekday()


json_file = open('conf.json')
chrome_path = '/usr/bin/google-chrome %s'
data = json.load(json_file)

class Meeting:
  def __init__(self, i ):
    self.name = data["courses"][i]["name"]
    self.day = data["courses"][i]["day"]
    self.hour = data["courses"][i]["hour"]
    self.mint = data["courses"][i]["min"]
    self.url = data["courses"][i]["url"]

number_of_courses = len(data["courses"])

def get_courses(i):
  course = Meeting(i)
  return course

def check_time(day, hour, mint, course_day, course_hour, course_min):
  """ print(day, "bu gün")
  print(course_day, "kurs gün") """
  if course_day == day:
    print("1")
    if course_hour == hour:
      print("2")
      if course_min <= mint:
        print("3")
        return True
  return False

while True:
  for i in range(number_of_courses):
    day = datetime.today().weekday()
    hour = datetime.now().hour
    mint = datetime.now().minute
    m = get_courses(i)
    a=check_time(day, hour, mint, m.day, m.hour, m.mint)
    if a == True:
      print ("bağlanılıyor", m.name)
      webbrowser.get(chrome_path).open(m.url)
      exit()

  time.sleep(10)
print("deneme")

