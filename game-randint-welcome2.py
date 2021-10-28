from random import randint
secret = randint(1.10)
print ("Welcome")
guess = 0
while guess != secret:
  a = input ("Guess the number!")
  guess = int(g)
  if guess == secret:
    print ("you win!")
  else:
    if guess > secret:
      print ("Too right!")
    else:
      print (Too low!")
   break
return(guess)
print ("Game over!")
    
