import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime


robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

with speech_recognition.Microphone() as mic:
	 print("Robot: I'm listening")
	 audio = robot_ear.listen(mic)

print("Robot: ...")
try:
    you = robot_ear.recognize_google(audio)
except:  
	you = ""
print("You: " + you)

if you == "":
      robot_brain = "I can't hear you, try again"
elif "hello" in you:
      robot_brain = "hello Thuong Hua"
elif "today" in you:
      today = date.today()	
      robot_brain = today.strftime("%B %d, %Y")
elif "time" in you:
      now = datetime.now()
      robot_brain = now.strftime("%H hours %M minutes %S seconds")
elif you == "my brother":
      robot_brain = "Hua Dai Tri and Hua Dai Thang"
elif "family" in you:
      robot_brain = "5 people"
elif "feel" in you:
      robot_brain = "You very handsome"

print("Robot: " + robot_brain)	   
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()