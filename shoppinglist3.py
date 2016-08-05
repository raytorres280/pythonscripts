shoppinglist = []

def showhelp():
  print("\nseparate each item with a comma.")
  print("type DONE to quit, SHOW to see the current list, and HELP to get this message.")
  
def showlist():
  count = 1
  for item in shoppinglist:
    print("{}: {}".format(count, item))
    count +=1
    
print("give me a list of things you want to shop for.")
showhelp()

while True:
  newstuff = input("> ")
  
  if newstuff == 'DONE':
    print("\n here is your list:")
    showlist()
    break
  elif newstuff == 'HELP':
    showhelp()
    continue
  elif newstuff == 'SHOW':
    showlist()
    continue
  else:
    newlist = newstuff.split(",")
    index = input("add this at a certain spot? press enter for the end of the list,"
    "or give me a number. Currently {} items in thelist.".format(len(shoppinglist)))
    if index:
      spot = int(index) - 1
      for item in newlist:
        shoppinglist.insert(spot, item.strip())
        spot += 1 
    else:
      for item in newlist:
        shoppinglist.append(item.strip())
