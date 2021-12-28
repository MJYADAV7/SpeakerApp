import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from test import testing
class childApp(GridLayout):
    def __init__(self,**kwargs):
        super(childApp,self).__init__()
        self.cols=1
        self.press=Button(text="Start",font_size=32,size_hint_y=None,size_hint_x=None,pos=(100,100))
        self.add_widget(self.press)
        self.label1=Label(text ="Press Start",font_size=32,size_hint_y=None,height=50)
        self.add_widget(self.label1)
        self.ids['name_label']=self.label1
        self.press.bind(on_press = self.click_me)

    def click_me(self,instance):
        self.ids.name_label.text="Recording"
        self.ids.name_label.text=testing("recording1.wav")


class parentApp(App):
    def build(self):
        return childApp()

if __name__=="__main__":
    p1=parentApp()
    p1.run()