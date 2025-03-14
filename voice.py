import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you repeat?")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your connection.")
            return ""
        except sr.WaitTimeoutError:
            speak("You didn't say anything. Please try again.")
            return ""

def voice_assistant():
    speak("Hello! How can I assist you today?")
    while True:
        command = recognize_speech()
        if command:
            if "hello" in command:
                speak("Hello! How can I help you?")
            elif "time" in command:
                now = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {now}")
            elif "date" in command:
                today = datetime.datetime.today().strftime("%B %d, %Y")
                speak(f"Today's date is {today}")
            elif "search" in command:
                query = command.replace("search for", "").strip()
                speak(f"Searching for {query} on the web")
                pywhatkit.search(query)
            elif "exit" in command or "stop" in command:
                speak("okay, thankyou, Goodbye! Have a great day.")
                break
            else:
                speak("Sorry, I didn't understand that. Try saying 'search for', 'time', or 'date'.")

if __name__ == "__main__":
    voice_assistant()
