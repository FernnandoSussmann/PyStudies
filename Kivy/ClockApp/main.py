from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from time import strftime

class ClockApp(App):
    def update_time(self, nap):
        self.root.ids.time.text = strftime("[b]%H[/b]:%M:%S")

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

Window.clearcolor = get_color_from_hex("#101216")


if __name__ == "__main__":
    ClockApp().run()
