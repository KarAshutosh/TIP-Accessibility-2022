import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def wait_sally():
    
    try:
        with sr.Microphone() as source:
            print('Listening...')
            
            voice = listener.listen(source)              
            
            command = listener.recognize_google(voice)
            command = command.lower()
            
    except:
        pass
    return command


def take_command():
    
    try:
        with sr.Microphone() as source:
            print('Waiting for command...')
            
            voice = listener.listen(source)              
            
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sally' in command:
                 command = command.replace('sally', '')
                 print(command)
    except:
        pass
    return command


def run_sally():
    command = wait_sally()

    print(command)

    if 'omega' in command:
        talk('Hello, please give me a command')
        
        event = take_command()
        
        print(event)
            
        if 'list' and 'experiments' in event:
            talk('The experiments are still under development') 
        
        else
            talk('Unknown Command')
        
    elif 'who' and 'are' and 'you' in command:
        talk('I am Omega. I am developed by T I P accessible labs of bits Goa')
        
    else:
        talk('Please say something')

        
while (1 == 1):
    run_sally()
