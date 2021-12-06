from tkinker import *
import pygame.mixer

class SoundPanel(frame):
  def_init_(self, app, mixer, sound_file):
    frame._init_(self, app)
    self.track = mixer.sound(sound_file)
    self.track_playing = intVar()
    track_button = checkbutton(self, variable = self.track_playing,
                                      command = self.track_toggle, 
                                         text = sound_file)
    
    track_button.pack(side = left)
    set.volume = doubleVar()
    set.volume.set(self.track.get_volume())
    volume_scale = scale(self, variable = self.volume,
                               from_ = 0.0, to = 1.0,
                               resolution = 0.1,
                               command = self.change_volume,
                         label = "volume, orient = horizontal)
    volume_scale.pack(side = right)
                         
def track_toggle(self):
    if self.track_playing.get() == 1:
       self.track.play(loops -1)
    else:
    self.track.stop()
                         
def change_volume(self, v):
    self.track.set_volume(self.volume.get())
                         
                           
