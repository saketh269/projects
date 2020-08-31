import os
import speech_recognition as sr 
import playsound 
from gtts import gTTS  
import os 
import wolframalpha
import webbrowser
from selenium import webdriver 
num = 1
def assistant_speaks(output): 
  global num 

  
  num += 1
  print("tess : ", output) 

  toSpeak = gTTS(text = output, lang ='en', slow = False) 
  
  file = str(num)+".mp3"
  toSpeak.save(file) 
  
  
  playsound.playsound(file, True) 
  os.remove(file) 


def get_audio(): 

  rObject = sr.Recognizer() 
  audio = '' 

  with sr.Microphone() as source: 
    print("Speak...") 
    
     
    audio = rObject.listen(source, phrase_time_limit = 5) 
  print("Stop.")  

  try: 

    text = rObject.recognize_google(audio, language ='en-US') 
    print("You : ", text) 
    return text 

  except: 

    assistant_speaks("Could not understand your audio, PLease try again !") 
    return 1
def shutdown():
    os.system("shutdown /s /t 1")
def process_text(input):
  try:
    if 'open' in input: 
      open_application(input.lower())
      return
    if 'search' in res1:
      search_web(res4)
      return
    elif "who are you" in input or "define yourself" in input: 
      speak = '''Hello, I am ROOKIE. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra'''
      assistant_speaks(speak) 
      return
    elif "who made you" in input or "created you" in input: 
      speak = "I have been created by saketh reddy."
      assistant_speaks(speak) 
      return

    elif "what can you do for me" in input:
      speak = """many things easier ."""
      assistant_speaks(speak) 
      return

    elif "calculate" in input.lower():
      app_id = "WOLFRAMALPHA_APP_ID"
      client = wolframalpha.Client(app_id)
      indx = input.lower().split().index('calculate') 
      query = input.split()[indx + 1:] 
      res = client.query(' '.join(query)) 
      answer = next(res.results).text 
      assistant_speaks("The answer is " + answer) 
      return

    elif 'search' in res1:
      search_web(res4)
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

    assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
    ans =  input("enter opinion::")
    if 'yes' in ans or 'yeah' in ans: 
      search_web(input)
def search_web(res4):
  if 'youtube' in res4:
    assistant_speaks("Searching in youtube")
    driver=webbrowser.get()
    query=res2
    driver.open("http://www.youtube.com/results?search_query =" +query) 
    return
  elif 'wiki' in res4: 
    assistant_speaks("Searching  in Wikipedia") 
    driver=webbrowser.get()
    query=res2
    driver.open("https://en.wikipedia.org/wiki/" +query) 
    return
  else: 
    if 'google' in res4:
      assistant_speaks("searching in google")
      driver=webbrowser.get()
      query=res2
      driver.open("https://www.google.com/search?q="+query,"&rlz=1C1SQJL_enIN863IN863&oq=pubg&aqs=chrome.0.0l6j69i60l2.1515j0j7&sourceid=chrome&ie=UTF-8") 
    else: 
      driver.open("https://www.google.com/search?q =") 

    return
def open_application(input): 

  if "chrome" in input: 
    assistant_speaks("Opening Google Chrome") 
    os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
    return

  elif "iexplore" in input or "mozilla" in input: 
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

if __name__ == "__main__":
    
  #assistant_speaks("This is tess your personal assistant.What's your name, Human?")
  #name =input("enter your name::")
  #assistant_speaks("Hello, " + name + '.') 
  while(1): 
    assistant_speaks("What can i do for you?")
    text = get_audio()
    if text==0:
      continue
      process_text(text)
    if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
        assistant_speaks("Ok bye, "+ name+'.')
        break
    if text==1:
      break
    process_text(text)
    _____________________________________________
    
import os
import speech_recognition as sr 
import playsound 
from gtts import gTTS  
import os 
import wolframalpha
import webbrowser
from selenium import webdriver
def get_audio():
    rObject = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Speak...")
        audio = rObject.listen(source, phrase_time_limit = 50000000)
        text = rObject.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        if"hi" in text:
            rObject = sr.Recognizer()
            audio = ''
            with sr.Microphone() as source:
                print("Speak...")
                audio = rObject.listen(source, phrase_time_limit = 5)
                print("Stop.")
            print(audio)
        print("Stop.")
    text = rObject.recognize_google(audio, language ='en-US') 
    print("You : ", text) 
    return text
if __name__:
    get_audio()
    

