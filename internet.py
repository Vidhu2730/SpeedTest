from threading import Thread

from speed_core import run_speed_test
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class SpeedTestApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.download_label = Label(text="Download speed: N/A")
        self.upload_label = Label(text="Upload speed: N/A")
        self.ping_label = Label(text="Ping: N/A")

        self.start_button = Button(text="Start Speed Test", on_press=self.start_speed_test)

        self.layout.add_widget(self.download_label)
        self.layout.add_widget(self.upload_label)
        self.layout.add_widget(self.ping_label)
        self.layout.add_widget(self.start_button)

        return self.layout

    def start_speed_test(self, instance):
        self.start_button.disabled = True
        self.start_button.text = "Testing..."
        self.download_label.text = "Download speed: testing..."
        self.upload_label.text = "Upload speed: testing..."
        self.ping_label.text = "Ping: testing..."
        Thread(target=self._run_speed_test, daemon=True).start()

    def _run_speed_test(self):
        try:
            result = run_speed_test()
            Clock.schedule_once(lambda _: self._show_result(result))
        except Exception as exc:
            Clock.schedule_once(lambda _: self._show_error(str(exc)))

    def _show_result(self, result):
        self.download_label.text = f"Download speed: {result.download_mbps} Mbps"
        self.upload_label.text = f"Upload speed: {result.upload_mbps} Mbps"
        self.ping_label.text = f"Ping: {result.ping_ms} ms"
        self.start_button.disabled = False
        self.start_button.text = "Start Speed Test"

    def _show_error(self, message):
        self.download_label.text = "Error checking the internet speed"
        self.upload_label.text = f"Error: {message}"
        self.ping_label.text = ""
        self.start_button.disabled = False
        self.start_button.text = "Start Speed Test"

if __name__ == "__main__":
    SpeedTestApp().run()
