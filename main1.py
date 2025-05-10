#..............here we import all the lib.............#
import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime 
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pw
import user_config 
from playsound import playsound


#............here we initialize pyttsx3 lib as an engine for our voice module..........#
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate",150)

#...............  here are all the functions used in project.....................#  
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sou():
    playsound("repul.mp3")    

def command():
    content=""
    while content == "":
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("say something")
            audio=r.listen(source)

        try:
            content= r.recognize_google(audio,language="en-in")
            print("Sir you said........." + content)
        except Exception as e:
            print("please try again sir....")

    return content


def main_process():  
    sou()
    while True:
        request= command().lower()
        if "hello" in request:
            speak("Welcome sir , how can i help you today")
        elif "play song" in request:
            speak("playing song")
            song=random.randint(1,5)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=K4DyBUG242c&list=RDQMKECDzA8siXM&start_radio=1")
            elif song ==2:
                webbrowser.open("https://www.youtube.com/watch?v=AnMhdn0wJ4I&list=RDQMKECDzA8siXM&index=2")
            elif song ==3:
                webbrowser.open("https://www.youtube.com/watch?v=wJnBTPUQS5A&list=RDQMKECDzA8siXM&index=4")
            elif song ==4:
                webbrowser.open("https://www.youtube.com/watch?v=cMg8KaMdDYo&list=RDQMKECDzA8siXM&index=8")
            else:
                webbrowser.open("https://www.youtube.com/watch?v=L-VMCv4Y9l8&list=RDQMKECDzA8siXM&index=15")
        elif "what time is it" in request:
            now_time=datetime.datetime.now().strftime("%H:%M")
            speak("current time is "+ str(now_time))
            print(now_time)
        elif "today's date is" in request:
            now_date=datetime.datetime.now().strftime("%d:%m")
            speak("current date is "+ str(now_date))
            print(now_date)
        elif "new task" in request:
            task=request.replace("new task", "")
            task=task.strip()
            if task != "":
                speak("adding task :" + task)
                with open ("todo.txt","a") as file:
                    file.write(task + "\n")    
        elif "speak task " in request:
            with open ("todo.txt","r") as file:
                speak("work we have to do :" + file.read())
        elif "show work" in request:
            with open ("todo.txt","r") as file:
                task = file.read()
            notification.notify(
                title ="today work",
                message= task
            ) 

        elif "open my facebook" in request:
            webbrowser.open("https://www.facebook.com/")
            speak("opening facebook")

        elif "open my github" in request:
            webbrowser.open("https://github.com/Ujjwalkumar8265")
            speak("opening github")

        elif "open my linkedin" in request:
            webbrowser.open("https://www.linkedin.com/")
            speak("opening linkedin")

        elif "open my instagram" in request:
            webbrowser.open("https://www.instagram.com/")
            speak("opening instagram")

        elif "open my discord" in request:
            webbrowser.open("https://www.discord.com/") 
            speak("opening discord")  
    
        elif "open" in request:
            query = request.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        #elif "close" in request:
            #query = request.replace("close", "").strip()
            #os.system(f"TASKKILL /F /IM {query}.exe")
            #pyautogui.sleep(10)
            #
            # pyautogui.press("enter")


        elif "what r u" in request:
            speak("hello sir my name is friday i am a virtual ai assiatant ")

        elif "who is your creator" in request or "who is your inventor" in request or "who created u" in request or "who created you" in request:
            speak("I am created or invented by my master ujjwal KUMAR")    

        elif "wikipedia" in request:
            query = request.replace("friday","")
            query = request.replace("search ","")
            query = request.replace("wikipedia ","")
            print(request)
            result=wikipedia.summary(request,sentences=2)
            speak(result)
            print(result)

        elif "search google" in request:
            query = request.replace("friday","")
            query = request.replace("search ","")
            query = request.replace("google ","")
            webbrowser.open("https://www.google.co.in/search?q="+request)
            speak("searching on google")
    
                   
        elif "send whatsapp" in request:
            pw.sendwhatmsg("+916396444160", "Hi,how are you", 14,40,30)
            speak("opening whatsapp and sending mail")

        elif "send email" in request:
            pw.send_mail("ujjwalsingh6396@gmail.com",user_config.gamil_pass, "hello hi" ,"my name", "ujjwalkumar6396@gmai.com")

        elif("volume up " in request) or ("increase volume" in request):
            pyautogui.press("volumeup") 
            speak("volume increased")   
        elif("volume down" in request) or ("decrease volume" in request):
            pyautogui.press("volumedown") 
            speak("volume decreased")   
        elif("volume mute" in request) or ("mute" in request):
            pyautogui.press("volumemute") 
            speak("volume muted") 
        elif("volume unmute" in request) or ("unmute" in request):
            pyautogui.press("volumeunmute") 
            speak("volume unmuted")   

        else:
            speak("command not recognize")            

main_process()               
