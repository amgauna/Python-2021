from tkinker import *
from sound_panel import *
import pygame.mixer

app = Tk()
app.title("Head first Mix")

mixer = pygame.mixer
mixer.init()

panel = soundPanel(app, mixer, "50459_M_RED_Nephlimizer.wav")
panel.pack()

panel = soundPanel(app, mixer, "49119_M_RED_Nephlimizer.wav")
panel.pack()

def.shutdown():
  mixer.stop()
  app.destroy()
  
app.protocol(WM_Delete_Window", shutdown)
             
app.mainloop()
             
             
