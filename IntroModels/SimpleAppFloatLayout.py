from kivy.app import App

from kivy.uix.scatter import  Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SimpleApp(App):
    def build(self):
        #layout
        b = BoxLayout(orientation="vertical")
        
        
        
        #others
        t = TextInput(font_size=80, size_hint_y=None,  height=100)   
        l = Label(text ="default",
                  font_size = 150)
        
        #binding
        
        t.bind(text=l.setter("text"))
        
        
        #widget adding
        b.add_widget(t)
        b.add_widget(l)
                
        return b
                    


if __name__ == '__main__':
    SimpleApp().run()