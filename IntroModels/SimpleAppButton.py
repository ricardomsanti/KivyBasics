from kivy.app import App
from kivy.uix.scatter import  Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


from kivy.uix.button import Button

class SimpleApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text = "Label here",
                  font_size = 150)
        
        f.add_widget(s)
        s.add_widget(l)
        
        return f
                    


if __name__ == '__main__':
    SimpleApp().run()