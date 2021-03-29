import webbrowser
import time
from datetime import datetime
import json
now = datetime.datetime.now()

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

for i in range(number_of_courses):

  m = get_courses(i)
  
  to_day = datetime.datetime.today().weekday()

  
#print(an.day)

#if an.hour >=3:    
 # print("connecting")
  #webbrowser.get(chrome_path).open(m1.url)
  #time.sleep()