from random import randint, shuffle

class Card():
    def __init__(self, value, suit):
        '''
        Stores CARD information
        :param value:
        the numerical value of the card when comparing cards
        :param suit:
        the name of the suit of said card
        '''
        self.value = value
        self.suit = suit

    def display(self):
        return self.getName() + " of " + self.suit

    def getName(self):
        '''
        Returns a string variable being the name of the card
        i.e.
        >> print(card.getName)
        'King'
        :return:
        face or value
        '''
        faces = [
            "Jack",
            "Queen",
            "King"
        ]
        if self.value == 1:
            return "Ace"
        if self.value > 10:
            tempValue = self.value - 11
            return faces[tempValue]
        else:
            return str(self.value)

class Deck():
    def __init__(self, joker = False, aceValue=1):
        self.cards = []
        # create deck of cards, and save it as self.cards
        suits = [
            "Hearts",
            "Spades",
            "Clubs",
            "Diamonds"
        ]
        for suit in suits:
            for value in range(2,14):
                card = Card(value, suit)
                self.cards.append(card)
        if joker:
            jokerCard = Card(99, "Joker")
            self.cards.append(jokerCard)
            self.cards.append(jokerCard)

        for suit in suits:
            aceCard = Card(aceValue, suit)
            self.cards.append(aceCard)

    def _checkValidIndex(self, i):
        # internal function, do not use
        l = len(self.cards)
        if i >= l:
            return False
        else:
            return True

    def shuffle(self):
        '''
        shuffles the deck of cards
        :return:
        '''
        shuffle(self.cards)
    def getRandomCard(self):
        '''
        get a random card from the deck, and its index
        i.e:
        card, index = getRandomCard()
        :return:
        the card and index of the card in the deck
        '''
        i = randint(0,len(self.cards)-1)
        return self.cards[i], i
    def removeByIndex(self, i):
        '''
        removes card at position i from the deck and returns it (so it is not lost)
        :param i:
        index of card to be removed
        :return:
        the removed card, or a Error card
        '''
        tempCard = Card(0, "Error")
        if self._checkValidIndex(i):
            tempCard = self.cards[i]
            del self.cards[i]
        return tempCard

    def getByIndex(self, i):
        '''
        get card from deck specified by its index
        :param i:
        index of card
        :return:
        either the card that is returned or an error card
        if the index is out of range
        '''
        if self._checkValidIndex(i):
            return self.cards[i]
        else:
            return Card(0, "Error")

    def printAtIndex(self, i):
        '''
        print the card at a certain index
        :param i:
        the index you want to print
        :return:
        '''
        if self._checkValidIndex(i):
            card = self.cards[i]
            print(card.display())
        else:
            print("Card does not exist. ")
    def printDeck(self):
        '''
        print all the cards in the deck (for debugging)
        :return:
        '''
        for i in range(0, len(self.cards)):
            card = self.cards[i]
            print("Card Index: " + str(i))
            self.printAtIndex(i)

    def getHand(self, cardCount):
        '''
        returns a list of x cards
        :param cardCount:
        number of cards it will return
        :return:
        the deck/hand of cards
        '''
        hand = []
        for i in range(cardCount):
            card, index = self.getRandomCard()
            self.removeByIndex(index)
            hand.append(card)
        return hand
