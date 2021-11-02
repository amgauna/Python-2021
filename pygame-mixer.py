import pygame.mixer

def wait.finish(channel):
  while channel.get_busy():
    pass
  
  sounds= pygame.mixer
  sounds.init()
  
  corrrect_s = sounds.sound("correct.way")
  wrong_s = sounds.sound("wrong.way")
  
  prompt = press 1 for correct, 2 for wrong, or 0 to quit: "
    
    number_asked = 0
    number_correct = 0
    number_wrong = 0
    
    choice = input(prompt)
    
    while choice != "0":
      
      if choice == "1":
        number_asked = number_asked + 1
        number_correct = number_correct +1
        number_finish(correct_s.play())
        
      if choice == "2":
        number_asked = number_asked + 1
        number_wrong = number_worng + 1
        wait_finish(wrong_s.play())
        
      choice = input(prompt)
      
print("You asked " + str(number_asked) + "questions.")
print(str(number_correct) + " were correctly answered.")
print(str(number_wrong) + " were answered incorretly.")

