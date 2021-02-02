import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.stacklayout import StackLayout

# A stack layout arranges widgets vertically or horizontally
# as they best fit

class StackLayoutApp(App):

    def build(self):
        return StackLayout()


StackLayoutApp().run()


