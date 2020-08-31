import os
import speech_recognition as sr
import playsound
from gtts import gTTS  
import getpass
import time
import wolframalpha
import webbrowser
from selenium import webdriver 
num = 1
def assistant_speaks(output): 
  global num
  num += 1
  #print("Rookie : ", output) 
  toSpeak = gTTS(text = output, lang ='en', slow = False)
  file = str(num)+".mp3"
  toSpeak.save(file) 
  playsound.playsound(file, True) 
  os.remove(file) 

def process_text(input):
  try:
    if 'open' in input: 
      open_application(input.lower())
      return
    if 'search' in input:
      search_web(input.lower())
      return
    if 'close' in input:
      close_application(input.lower())
      return
    elif "explain yourself" in input: 
      speak = '''Hey. this is TESS your text Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra'''
      assistant_speaks(speak) 
      return
    elif "what can you do for me" in input:
      speak = """many things easier ."""
      assistant_speaks(speak) 
      return
    elif 'shutdown' in input:
      speak=("shutting down")
      assistant_speaks(speak)
      shutdown()
      return
    else: 
      assistant_speaks("I can search the web for you, Do you want to continue?") 
      ans = input("enter opinion::")
      if 'yes' in ans or 'yeah' in ans: 
        search_web(input) 
      else: 
        return
  except : 
    speak=("I don't understand, I can search the web for you, Do you want to continue?") 
    ans =  input("enter opinion::")
    assistant_speaks(speak)
    if 'yes' in ans or 'yeah' in ans:
        search_web(input)
def open_application(input):
  if "chrome" in input:
    assistant_speaks("Opening Google Chrome")
    os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    return
  elif "explore" in input or "mozilla" in input:
    assistant_speaks("Opening internet explore") 
    os.startfile('C:\Program Files (x86)\Internet Explorer\iexplore.exe') 
    return

  elif "paint" in input: 
    assistant_speaks("Opening Paint") 
    os.startfile('C:\WINDOWS\system32\mspaint') 
    return

  elif "system settings" in input: 
    assistant_speaks("Opening System Settings") 
    os.startfile('C:\WINDOWS\system32\control') 
    return
  elif "task manager" in input: 
    assistant_speaks("Opening Task Manager") 
    os.startfile('C:\WINDOWS\system32\Taskmgr') 
    return

  else: 
    assistant_speaks("Application not available") 
    return
def close_application(input):
  if "chrome" in input:
    assistant_speaks("closing the application")
    os.system('TASKKILL /F /IM chrome.exe')
  elif "explore" in input:
    assistant_speaks("closing the application")
    os.system('TASKKILL /F /IM iexplore.exe')
  elif "paint" in input:
    assistant_speaks("closing the application")
    os.system('TASKKILL /F /IM mspaint.exe')
  elif "all" in input:
    assistant_speaks("closing all application")
    os.system('TASKKILL /F /IE ')
  else:
    assistant_speaks("no application")
  
if __name__=="__main__":
  assistant_speaks("hey, This is Tess.enter your name?")
  name =input("enter your name::")
  assistant_speaks("Hey, " + name + '.') 
  while(1): 
    assistant_speaks("What can i do for you?")
    text = input("enter ::")
    if text==0:
      continue
      process_text(text)
    if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
        assistant_speaks("Ok bye, "+ name+'.')
        break
    process_text(text)

   
