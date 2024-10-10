from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

class UI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create UI components
        self.title_label = Label(text="Determined IELTS", font_size=24, bold=True)
        self.vocabulary_label = Label(text="Vocabulary", font_size=18)
        self.english_input = TextInput(hint_text="Enter English word")
        self.bangla_unicode_input = TextInput(hint_text="Enter Bangla Unicode")
        self.add_button = Button(text="Add Vocabulary")
        self.vocabulary_list = GridLayout(cols=2, spacing=10)
        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.vocabulary_list)
        self.speech_recognition_label = Label(text="Speech Recognition", font_size=18)
        self.recognize_button = Button(text="Recognize Speech")
        self.recognized_text_label = Label(text="")
        self.exam_label = Label(text="Exam", font_size=18)
        self.start_exam_button = Button(text="Start Exam")
        self.exam_results_label = Label(text="")

        # Arrange components in the layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.vocabulary_label)
        self.layout.add_widget(self.english_input)
        self.layout.add_widget(self.bangla_unicode_input)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.scroll_view)
        self.layout.add_widget(self.speech_recognition_label)
        self.layout.add_widget(self.recognize_button)
        self.layout.add_widget(self.recognized_text_label)
        self.layout.add_widget(self.exam_label)
        self.layout.add_widget(self.start_exam_button)
        self.layout.add_widget(self.exam_results_label)

        # Bind event handlers
        self.add_button.bind(on_press=self.add_vocabulary)
        self.recognize_button.bind(on_press=self.recognize_speech)
        self.start_exam_button.bind(on_press=self.start_exam)

    def add_vocabulary(self, instance):
        # Add vocabulary to the database and update the UI
        english = self.english_input.text
        bangla_unicode = self.bangla_unicode_input.text
        if english and bangla_unicode:
            self.vocabulary.add_vocabulary(english, bangla_unicode)
            self.update_vocabulary_list()
            self.english_input.text = ""
            self.bangla_unicode_input.text = ""

    def update_vocabulary_list(self):
        # Update the vocabulary list UI
        self.vocabulary_list.clear_widgets()
        for vocabulary in self.vocabulary.get_vocabulary():
            english_label = Label(text=vocabulary[1])
            bangla_unicode_label = Label(text=vocabulary[2])
            self.vocabulary_list.add_widget(english_label)
            self.vocabulary_list.add_widget(bangla_unicode_label)

    def recognize_speech(self, instance):
        # Recognize speech and update the recognized text label
        recognized_text = self.speech_recognition.recognize_speech()
        self.recognized_text_label.text = recognized_text

    def start_exam(self, instance):
        # Implement exam logic and update the exam results label
      questions = [
            "What is the meaning of the word 'happy'?",
            "How do you say 'book' in Bangla?",
            # ... more questions
        ]
        correct_answers = ["feeling joyful", "বই", ...]  # Replace with correct answers
        user_answers = []
        for question in questions:
            user_answer = input(question + ": ")
            user_answers.append(user_answer)
        score = 0
        for i in range(len(questions)):
            if user_answers[i] == correct_answers[i]:
                score += 1
        self.exam_results_label.text = f"Your score: {score}/{len(questions)}"
        pass
