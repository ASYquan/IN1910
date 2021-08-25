import random

suit = ["C", "D", "H", "S"]

deck = []
  
for i in range(1,14):
    for j in suit:
        deck.append((i,j))

random.shuffle(deck)

shuffle = []
for x in range(13):
    shuffle.append(deck[x])
    
print("Deck pre-shuffle")
print(shuffle)
list.sort(shuffle)
print("Deck post-shuffle")
print(shuffle)