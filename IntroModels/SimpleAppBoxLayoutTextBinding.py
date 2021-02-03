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
        
        #other items
        
        b1 = Button(text="bigger")
        #-------------------------------------------------------
        t = TextInput(font_size=80, size_hint_y=None,  height=100) 
        #-------------------------------------------------------  
        l = Label(text ="default",
                  font_size = 100)
        
        
        #binding method for text input and the label's text
        t.bind(text=l.setter("text"))
        
        #binding method for pressing the button and the font size getting bigger
        
        self.b1.bind(on_press=self.b1_button)
        
        #funtion binde to the b1 button
    
    def b1_button(self, instance):
        label = self.label.text
        print(label)
        
        
    #widget adding
    b.add_widget(b1)
    b.add_widget(t)
    b.add_widget(l)
                
    return b
                    


if __name__ == '__main__':
    SimpleApp().run()
