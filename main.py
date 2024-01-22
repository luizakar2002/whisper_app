from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import threading
from client import TranscriptionClient

class VoiceRecorderApp(App):
    def build(self):
        self.transcription_client = TranscriptionClient(
            "localhost",
            9090,
            is_multilingual=True,
            lang="hy",
            translate=True,
            model="lukarape/whisper-small-erebuni-7-chp400-ct2"
        )

        layout = BoxLayout(orientation='vertical')
        self.record_button = Button(text="Start Recording", on_press=self.start_recording)
        layout.add_widget(self.record_button)
        return layout

    def start_recording(self, instance):
        # Start the recording process in a separate thread
        recording_thread = threading.Thread(target=self.transcription_client)
        recording_thread.start()

if name == 'main':
    VoiceRecorderApp().run()
