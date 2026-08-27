import speedtest
from kivy.app import App
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
        download, upload, ping = self.check_internet_speed()
        if download is not None and upload is not None:
            self.download_label.text = f"Download speed: {download} Mbps"
            self.upload_label.text = f"Upload speed: {upload} Mbps"
            self.ping_label.text = f"Ping: {ping} ms"
        else:
            self.download_label.text = "Error checking the internet speed"
            self.upload_label.text = f"Error: {ping}"
            self.ping_label.text = ""

    @staticmethod
    def convert_speed(bps):
        mbps = bps / (1024 * 1024)  # Convert to megabits per second
        return mbps

    @staticmethod
    def check_internet_speed():
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            download = st.download()
            upload = st.upload()
            ping = st.results.ping

            download_mbps = SpeedTestApp.convert_speed(download)
            upload_mbps = SpeedTestApp.convert_speed(upload)

            return int(download_mbps), int(upload_mbps), int(ping)

        except Exception as e:
            return None, None, str(e)

if __name__ == "__main__":
    SpeedTestApp().run()
