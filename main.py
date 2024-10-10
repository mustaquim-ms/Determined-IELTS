pip install kivy kivy_garden.text kivy_garden.speech kivy_garden.filechooser

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from vocabulary import Vocabulary
from speech_recognition import SpeechRecognition
from ui import UI

class DeterminedIELTSApp(App):
    def build(self):
        self.vocabulary = Vocabulary()
        self.speech_recognition = SpeechRecognition()
        self.ui = UI()
        return self.ui.build()

if __name__ == '__main__':
    DeterminedIELTSApp().run()
