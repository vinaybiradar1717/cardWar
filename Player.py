import Cards
import Deck

class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_card(self, new_card):
        if type(new_card) == list:
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)

    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} cards."


# c = Deck.Deck()
# c.shuffle()
# card = c.deal_one()
# player_1 = Player("One")
# player_1.add_card([card, card])
# for i in player_1.all_cards:
#     print(i)
# print(player_1)
# a = player_1.remove_card()
# print(a)
