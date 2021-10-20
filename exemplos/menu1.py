ans=True
while ans:
    print ("""
    1.Add a Student \n
    2.Delete a Student \n
    3.Look Up Student Record \n
    4.Exit/Quit \n
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
      print("\nStudent Added") 
    Elif ans=="2":
      print("\n Student Deleted") 
    Elif ans=="3":
      print("\n Student Record Found") 
    Elif ans=="4":
      print("\n Goodbye") 
    Elif ans !="":
      print("\n Not Valid Choice Try again") 
    break
return(ans)
