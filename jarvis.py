import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import pywhatkit as kit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
name='jarvis'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        print("\U0001F642")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        print("\U0001F642")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        print("\U0001F642")
        speak("Good Evening!")

    speak("I am "+name+" Please tell me how may I help you")
def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening!..........')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognising!...........')
        query=r.recognize_google(audio,language='en-in')
        if not 'exit' in query or 'stop' in query:
            print(f'user said:{query}\n')
    except  Exception as e:
        print("Say that again please....")
        return "None"
    return query
    # query=input('Enter your choice:')
    # return query

def send_whatshapp_message(number,msg):
    kit.sendwhatmsg_instantly(f'+91{number}',msg)

if __name__ == "__main__":
    wishMe()
    speak('i am your'+name+'at your service')
    # speak('listing out the functions that i can perform')
    # print("listing out the functions that i can perform")
    # speak("i can search wikipedia, for that you have to give the command like wikipedia 'whose wikipedia you want'")
    # print("i can search wikipedia, for that you have to give the command like wikipedia 'whose wikipedia you want'")
    # speak('i can open youtube and i can open google and i can open stackoverflow for that you have to give command like open "wikipedia or google or stackoverflow"')
    # print('i can open youtube and i can open google and i can open stackoverflow for that you have to give command like open "google/youtube/stackoverflow"')
    # speak('i can open news for you for that you have to mention news')
    # print('i can open news for you for that you have to mention news')
    # speak('i can search anything in google without typing anything')
    # speak('for that you have to give command search "what you want to seach"')
    # print('i can search anything in google without typing anythingf or that you have to give command search "what you want to seach"')
    # speak('you can send whatshapp messages to any one you need')
    # print('can send whatshpp messages')
    # speak('i can tell you jokes')
    # print('i can tell you jokes')
    # speak("can read and write notes for writing notes give command like 'write a note' and for reading that note 'show note'")
    # print("can read and write notes for writing notes give command like 'write a note' and for reading that note 'show note'")
    # speak('i can help you in seaching locations in maps for that you should give command like where is "some location"')
    # print('i can help you in seaching locations in maps for that you should give command like where is "some location"')
    # speak('are you in a mood of shopping if my guess was right that why late give command as shopping i will help you to open the amazon website')
    # print("for shopping give command shopping")
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for your query, please be more specific.")
                print(e.options)
            except wikipedia.exceptions.PageError:
                speak("No result found for your query on Wikipedia.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")
                print(e)

        elif 'open youtube' in query:
            speak('Here you go to Youtube\n')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Here you go to Google\n')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak('Here you go to stackoverflow')
            webbrowser.open("stackoverflow.com")

        elif 'who i am' in query:
            speak("if you talk then definitely your human.")

        elif 'why you came to world' in query:
            speak("thanks to jahnavi. further it's a secret")

        elif 'is love' in query:
            speak('it is 7th sense that destroy all other senses')

        elif 'who are you' in query:
            speak('i was created as a minor project by jahnavi')

        elif 'news' in query:
            webbrowser.open('https://timesofindia.indiatimes.com/india')

        elif 'search' in query:
            query=query.split()
            print(' '.join(query[1:]))
            a=' '.join(query[1:])
            speak('searching'+a)
            kit.search(a)

        elif 'how are you' in query:
            speak("I'm fine.You're very kind to ask,especially in these tempestuous times")
            speak('how about you...')

        elif 'fine' in query:
            speak('its good to know that you are fine')

        elif 'change name' in query:
            speak('what would you like to call me.sir')
            name=takeCommand()
            speak('thanks for naming me')
            speak('this is '+name+' ,at your service')

        elif "what's your name" in query:
            speak('my friends call me ')
            speak(name)
            print("My friends call me",name)

        elif 'who made you' in query:
            speak('I have been created by jahnavi as a minor project')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'shopping' in query:
            webbrowser.open("https://www.amazon.in/?tag=msndeskabkin-21&hvadid=72705283629710&hvqmt=e&hvbmt=be&hvdev=c&ref=pd_sl_7qhce485bd_e")

        elif 'send message' in query:
            speak("would you please tell me to which number should i send message:")
            number=int(input())
            speak("what do you want to send message:")
            msg=input()
            send_whatshapp_message(number,msg)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'exit' in query:
            break

        elif "where is" in query:
            query=query.replace("where is","")
            location=query
            speak("user asked to locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/"+location+"")

        elif "write a note" in query:
            speak("what should i write,")
            note=takeCommand()
            file=open("jarvis.txt",'w')
            speak("should i include date and time")
            snfm=takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strtime=datetime.datetime.now()
                file.write(strtime)
                file.write(" :- ")
                file.write(note)

            else:
                file.write(note)

        elif "show note" in query:
            speak("showing notes")
            file=open("jarvis.txt","r")
            print(file.read())
            speak(file.read(6))
