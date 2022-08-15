import Cards
import Deck
import Player

class War():

    def war_game(self):
        player_1 = Player.Player("One")
        player_2 = Player.Player("Two")

        new_deck = Deck.Deck()
        new_deck.shuffle()

        for i in range(26):
            player_1.add_card(new_deck.deal_one())
            player_2.add_card(new_deck.deal_one())

        game_on = True
        round_num = 0
        
        while game_on:
            round_num += 1
            print(f"Round: {round_num}")
            
            if player_1.all_cards == 0:
                print("Player 2 Wins")
                game_on = False
                break
            
            if player_2.all_cards == 0:
                print("Player 1 Wins")
                game_on = False
                break

            player_1_cards = []
            try:
                player_1_cards.append(player_1.remove_card())
            except:
                print("Exception: Player 2 wins")
                game_on = False
                break
            
            player_2_cards = []
            try:
                player_2_cards.append(player_2.remove_card())
            except:
                print("Exception: Player 1 wins")
                game_on = False
                break

            
            at_war = True
            while at_war:
                if player_1_cards[-1].value > player_2_cards[-1].value:
                    player_1.add_card(player_1_cards)
                    player_1.add_card(player_2_cards)
                    at_war = False

                elif player_1_cards[-1].value < player_2_cards[-1].value:
                    player_2.add_card(player_2_cards)
                    player_2.add_card(player_1_cards)
                    at_war = False

                else:
                    print("War!!")
                    if len(player_1.all_cards) < 7:
                        print("Player 2 wins")
                        game_on = False
                        break
                    elif len(player_2.all_cards) < 7:
                        print("Player 1 wins")
                        game_on = False
                        break
                    else:
                        for i in range(7):
                            player_1_cards.append(player_1.remove_card())
                            player_2_cards.append(player_2.remove_card())

war = War()
war.war_game()