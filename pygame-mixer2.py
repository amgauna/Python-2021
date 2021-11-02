from thinker import *
import pygame.mixer

def play_correct_sound():
  num_good.set(num_good.get() + 1)
  correct_s.play
  
def play_wrong_sound():
  num_bad.set(num_bad.get() +1)
  wrong_s.play
  
  app = Tk()
  app.title("TVN Game Show")
  app.geometry("300x110+200+100)
               
  sounds = pygame.mixer
  sounds.init()
               
  correct_s = sounds.sound("correct.way")
  wrong_s = sounds.sound("wrong.way")
               
  num_good = intvar()
  num_good.set(0)
  nun_bad = intvar()
  num_bad.set(0)
               
  lab = label(app.text="When you are ready, click on the buttons!", height=3)
  lab.pack()
               
  lab1 = label(app.textvariable = num_good()
  lab1.pack(side="left")
               
  lab2 = label(app.textvariable = num_bad()
  lab2.pack(side="right")
               
  b1 = button(app.text = "Correct".with = 10.command = play_correct_sound)
  b1.pack(side = "left".padx = 10.pady = 10)
  
  b2 = button(app.text  "Wrong!".width = 10.command = play_wrong_sound)
  b2.pack(side = "right".padx = 10.pady = 10)
               
  app.mainloop()
               
  
              
              
              
               
               
               
