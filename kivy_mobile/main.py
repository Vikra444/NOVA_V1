from kivy.app import App
from kivy.uix.label import Label

class NOVAMobileApp(App):
    def build(self):
        return Label(text='Hello from NOVA Mobile!')

if __name__ == '__main__':
    NOVAMobileApp().run()