import pyttsx3 
import speech_recognition as sr

recognizer = sr.Recognizer()


class Jarvis():
    
    def recongnize(self):
        while True:
            with sr.Microphone() as source:
                recognizer.pause_threshold(0.7)
                audio = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio,language='hi=In')
                    print(text)
                    break
                except:
                    self.speak('वापीस से बोल')

    def speak(self,text):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.setProperty('volume', 1)
        engine.say(text)
        engine.runAndWait()
        engine.setProperty('rate', 180)
        
    def resolve(self, query):
        if query == 'अस्सलमु अलैकूम ':
            self.speak('अलैकूम अस्सलमु')
        
        
        
    

