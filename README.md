# CardDeck (WIP)

A simple card deck in python

Example usage:
```python
from CardDeck import Deck

deck = Deck()

#create hand with 5 cards
myHand = deck.getHand(5)
# print first card
print(myHand[0])

# print cards in hand
for card in myHand:
    print(card)

# add first card back into deck
deck.addCard(myHand[0])
del myHand[0]

```




