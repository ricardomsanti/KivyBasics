from kivy.app import App
from kivy.uix.button import Button

class SimpleApp(App):
    def build(self):
        return Button(text="Click here",
                      background_color=(0,0,1,1),
                      font_size=150)
                    


if __name__ == '__main__':
    SimpleApp().run()