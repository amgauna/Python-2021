from tkinter import
from sound_panel import *
import pygame.mixer

app=Tk()
app.title("Heart First Mix")
app.geometry("250x100+200+100)            
sound_file = "50459_M_RED_Nephlimizer.wav")

mixer = pygame.mixer
mixer.init()

def create_gui(app.mixer.sound_file):
  
def track_toggle():
  if track_playing.get() == 1:
    track.play(loops = -1)
  else:
    track.stop()
    
def.change_volume(v):
  track.set_volume(volume.get())
  
track = mixer.sound(sound_file)
track_playing = intVar()
track_button = checkbutton(app, variable = track_playing, 
                                 command = track_toggle, 
                                    text = sound_file()
                             
track_button.pack(side = left)
volume = doubleVar()
volume.set(track.get_volume())
volume_scale = scale(variable = volume, 
                         from = 0.0,
                           to = 1.0,
                   resolution = 0.1,
                      command = change_volume,
                        label = "Volume",
                       orient = horizontal)
 
volume_scale.pack(side = right)
                             
def shutdown():
    track.stop()
    app.destroy()
                             
 app.protocol("wm_delete_window", shutdown)
                           
 app.mainloop()
                     
                             
                   
