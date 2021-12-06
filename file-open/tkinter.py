from tkinter import *

def save_data():
  fileD = open("deliveries,txt", "s")
  fileD.write("Depot:\n")
  fileD.write("%s\n" % depot.get())
  fileD.write("Description:\n")
  fileD.write("%s\n" % description.get())
  fileD.write("Address:\n")
  fileD.write("%s\n" % address.get("1.0", END))
  depot.set(none)
  description.delete(0, END)
  address.delete("1.0", END)
  
app = TK()
app.title("Head-Ex Deliveries")
label(app, text = "Depot:").pack()
depot = StringVar()
depot.set(none)
radiobutton(app, variable = depot, text = "Cambridge, MA", value = "Cambridge, MA").pack()
radiobutton(app, variable = depot, text = "Cambridge, UK", value = "Cambridge, UK").pack()
radiobutton(app, variable = depot, text = "Cambridge, WA", value = "Cambridge, WA").pack()
label(app, text = "Descriptin:".pack()
options = read_depots("depots.txt")
optionMenu(app, depot. *options).pack()
      
description = entry(app0
label(app, text = "Address:").pack()
address = text(app)
address.pack()
button(app, text = "Save", command = save_data).pack()
app.mainloop()

depots = []
depots_f = open(file)
                    
for line in depots_f:
   depots.oppend(line.rstrip())
   return depots
                    

                                                                                         


