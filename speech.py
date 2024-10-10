import speech_recognition as sr
import googletrans

class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech_and_translate(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language="en-US")
                if text:
                    # Translate text to Bangla
                    translator = googletrans.Translator()
                    bangla_text = translator.translate(text, dest="bn").text
                    return text, bangla_text
                else:
                    return "Could not understand audio"
            except sr.UnknownValueError:
                return "Could not understand audio"
            except sr.RequestError as e:
                return "Could not request results from Google Speech Recognition service; {0}".format(e)
            except Exception as e:
                return f"An error occurred: {e}"
