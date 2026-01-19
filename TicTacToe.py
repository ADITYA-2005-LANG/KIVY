from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.uix.label import Label
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.floatlayout import FloatLayout 
from kivy.core.window import Window
from time import sleep
class tictactoe(Widget):
  turn="X"
  arr=[[],[],[]]
  def clear(self, inst):
      
      
      for k in self.walk():
          if isinstance(k,Button) and k.text!="RESET":
              k.text=" "
             
              k.background_color=(1,1,1,1)
          elif isinstance(k,Label) and k.text!="RESET":
              k.text="X: 0" if k.text[0]=="X" else "O: 0"
          k.disabled=True
      
              
  def over(self,ch):
      for k in self.children[1].children:
          if k.text[0]==ch[0].text:
              score=(int)(k.text[-1])
              k.text=ch[0].text+": "+str(score+1)
      for k in self.children[0].children:
          if k in ch:
              k.background_color=(0,1,0,1)
          else:
              k.background_color=(1,0,0,1)
      
      
         
  def check(self):
    ans=tictactoe.arr
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
  def __init__(self,*k):
   
    super().__init__(*k)
    grid=GridLayout(cols=3,size=(900,900),pos=(100,550),row_force_default=True,row_default_height=300,padding=25)
    for i in range(9):
      b=Button(text=" ",font_size=100)
      grid.add_widget(b)
      b.bind(on_release=self.move)
      tictactoe.arr[i//3].append(b)
    
    self.add_widget(grid)
  def move(self, instance):
    if instance.text == " ":
        txt="X" if self.turn=="X" else "O"
        instance.text=txt
        anim = Animation(font_size=200, duration=0.1)
        anim+=Animation(font_size=100,duration=0.1)
        anim.start(instance)
        self.turn = "O" if self.turn == "X" else "X"
        instance.press=True
        ch=self.check()
        if type(ch)==list:
          self.over(ch)
       
        
      
    
    
    
class TicTacToeApp(App):
  def build(self):
    return tictactoe()

if __name__ == '__main__':
    TicTacToeApp().run()