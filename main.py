from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider
from os import system
from kivy.uix.screenmanager import ScreenManager,FallOutTransition
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
class MenuScreen(Screen):
    turn="X"
    arr=[[],[],[]]
    able=True
    def on_enter(self):
        if self.manager.current=="menu": 
            self.ids.clk.text="5"
            self.event = Clock.schedule_interval(self.clock, 1)
    def on_leave(self):
        if hasattr(self, 'event'):
            self.event.cancel()
    def win(self,k):
        if self.manager.current=="menu" and k.text[-1]!='0' and k.text[-1] == str(int(self.manager.get_screen('settings').ids.slider.value)):
            self.win=k.text[0]
            popup= Popup(title="RESULT",content=Label(text='X WINS !!!',font_size=70),size_hint=(None, None), size=(400, 400))
            popup.open(parent=self)

    def clock(self,dt):
        s=(int)(self.ids.clk.text)-1
        self.ids.clk.text=str(s)
        if(s<=3):
            anim = Animation(font_size=100, duration=0.1)
            anim+=Animation(font_size=50,duration=0.1)
            anim.start(self.ids.clk)
        if s<=0:
            self.over('X' if MenuScreen.turn=='O' else 'O')

    def clear(self, inst):
      
      self.ids.clk.text="5"
      self.event.cancel()
      MenuScreen.able=True
      for k in self.children[0].children:
        k.text=" "
        k.background_color=(1,1,1,1)
      if inst.text=="RESET":
        for k in self.children[1].children:
            if not isinstance(k,Button) and len(k.text)>1:
                k.text="X: 0" if k.text[0]=="X" else "O: 0"
      if self.manager.current=="menu": self.event=Clock.schedule_interval(self.clock,1)

    def over(self,ch):
      self.event.cancel()
      MenuScreen.able=False
      if type(ch)==list:
        for k in self.children[1].children:
            if k.text[0]==ch[0].text:
                score=(int)(k.text[-1])
                k.text=ch[0].text+": "+str(score+1)
                self.win(k)

        for k in self.children[0].children:
            if k in ch:
                k.background_color=(0,1,0,1)
            else:
                k.background_color=(1,0,0,1)
      else:
        for k in self.children[1].children:
            if k.text[0]==ch:
                score=(int)(k.text[-1])
                k.text=k.text[0]+": "+str(score+1)
                self.win(k)
        for k in self.children[0].children:
            if k.text!=" ":
                if k.text==ch:
                    k.background_color=(0,1,0,1)
                else:
                    k.background_color=(1,0,0,1)
         
    def __init__(self,**kw):
        super().__init__(**kw)
        self.add_btn()
        
    def check(self):
        ans=MenuScreen.arr
        for k in range(3):
            if ans[k][0].text==ans[k][1].text==ans[k][2].text!=" ":
                return [ans[k][0],ans[k][1],ans[k][2]]
        for k in range(3):
            if ans[0][k].text==ans[1][k].text==ans[2][k].text!=" ":
                return [ans[0][k],ans[1][k],ans[2][k]]
        if ans[0][0].text==ans[1][1].text==ans[2][2].text!=" ":
            return [ans[0][0],ans[1][1],ans[2][2]]
        if ans[0][2].text==ans[1][1].text==ans[2][0].text!=" ":
            return [ans[0][2],ans[1][1],ans[2][0]]
        return None
    def add_btn(self):
        for k,i in zip(self.ids.grid.children,range(9)):
            MenuScreen.arr[i//3].append(k)
    def move(self, instance):
        self.ids.clk.text="5"
        if instance.text == " " and MenuScreen.able:
            txt="X" if MenuScreen.turn=="X" else "O"
            instance.text=txt
            anim = Animation(font_size=100, duration=0.1)
            anim+=Animation(font_size=50,duration=0.1)
            anim.start(instance)
            MenuScreen.turn = "O" if MenuScreen.turn == "X" else "X"
            ch=self.check()
            if type(ch)==list:
                self.over(ch)

            

class SettingsScreen(Screen):
    pass

class TicTacToeApp(App):

    def build(self):
        sm = ScreenManager(transition=FallOutTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.current='settings'
        
        return sm

if __name__ == '__main__':
    system("clear")
    TicTacToeApp().run()