import Cards

class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in Cards.suits:
            for rank in Cards.ranks:
                new_card = Cards.Card(suit, rank)
                self.all_cards.append(new_card)

    def deal_one(self):
        return self.all_cards.pop()

    def shuffle(self):
        return Cards.random.shuffle(self.all_cards)

# c = Deck()
# print(len(c.all_cards))
# print(c.all_cards[3])
# c.shuffle()
# print(c.all_cards[3])
# a = c.deal_one()
# print(a)
# print(len(c.all_cards))