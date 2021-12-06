def save_transaction(Price, credit_card, description):
  file = open("transactions.txt","a")
  file.write("%07d%16s%16s\n" % (price * 100, credit_card, description))
  file.close()
  
items = ["WORKOUT", "WEIGHTS", "BIKES"]
prices = [35.0, 10.0, 8.10]
running = true

while running:
  option = 1
  for choice in items:
    print(str(option) + ". " + cloice)
    option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
      running = false
    else:
      credit_card = input("credit card number: ")
      save_transaction(prices[choice -1], credit_card, items[choice - 1])
