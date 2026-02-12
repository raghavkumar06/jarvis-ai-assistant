from ai_engine import ask_gpt
import pyttsx3
import speech_recognition as sr
import webbrowser
import random
import datetime
import pyautogui
import wikipedia
import pywhatkit as pwk
print("Jarvis core loaded")


engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    try:
        text = str(text)
        text = text.replace("\n", " ")  # remove new lines
        text = text.replace("  ", " ")
        text = text.strip()

        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:", e)

def command():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=4, phrase_time_limit=4)

        text = r.recognize_google(audio, language="en-IN")
        print("You said:", text)
        return text.lower()

    except sr.WaitTimeoutError:
        print("Didn't hear anything…")
        return ""

    except sr.UnknownValueError:
        print("Couldn't understand…")
        return ""

    except sr.RequestError:
        speak("Internet issue detected")
        return ""

    except Exception as e:
        print("Mic error:", e)
        return ""

        
def main_process():
    while True:
        request = command()

        if request == "none":
            continue

        # GREET
        if "hello" in request:
            speak("Welcome, how can I help you?")

        # PLAY MUSIC
        elif "play music" in request:
            speak("Playing music")
            songs = [
                "https://www.youtube.com/watch?v=eBaGl0ib3ZY",
                "https://www.youtube.com/watch?v=1Zf1j36B42g",
                "https://www.youtube.com/watch?v=3nQNiwdH2Q"
            ]
            webbrowser.open(random.choice(songs))

        # TIME
        elif "time" in request:
            now_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("Current time is " + now_time)

        # DATE
        elif "date" in request:
            now_date = datetime.datetime.now().strftime("%d:%m")
            speak("Today date is " + now_date)

        # NEW TASK
        elif "new task" in request:
            speak("Okay, tell me the task.")
            task = command()

            if task == "none" or task.strip() == "":
                speak("I did not get the task. Please say again.")
            else:
                with open("todo.txt", "a", encoding="utf-8") as file:
                    file.write(task + "\n")
                speak("Task added successfully.")

        # YOUTUBE
        elif "open youtube" in request:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com/")

        # WIKIPEDIA
        elif "wikipedia" in request:
            search_query = request.replace("wikipedia", "").strip()
            speak("Searching on Wikipedia")
            try:
                result = wikipedia.summary(search_query, sentences=2)
                speak(result)
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        # GOOGLE SEARCH
        elif "search google" in request:
            speak("Searching on Google")
            query = request.replace("search google", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")

        # WHATSAPP MESSAGE
        elif "send whatsapp" in request:
            speak("Kisko message bhejna hai? (Number fixed hai code mein)")
            number = "+918755109800"

            speak("Kya message bhej du?")
            msg = command()

            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute + 1

            # minute overflow fix
            if minute >= 60:
                minute = 0
                hour = (hour + 1) % 24

            pwk.sendwhatmsg(number, msg, hour, minute)
            speak("WhatsApp message schedule kar diya!")
            
        # CHATGPT / AI FEATURE
        elif "ask ai" in request or "chat gpt" in request or "ai question" in request:
            speak("Okay, what should I answer?")
            user_query = command()

            if user_query == "none":
                speak("I couldn't hear that, please repeat.")
            else:
                speak("Thinking, please wait...")
                ai_answer = ask_gpt(user_query)
                ai_answer = str(ai_answer)   # convert to clean string
                print("AI:", ai_answer)
                speak(ai_answer)

        # OPEN ANY APP
        elif request.startswith("open "):
            app = request.replace("open ", "").strip()
            pyautogui.press("super")
            pyautogui.typewrite(app)
            pyautogui.sleep(2)
            pyautogui.press("enter")


