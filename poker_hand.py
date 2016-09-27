class Card():
    def __init__(self, card_string):
        self.value = card_string[0:-1]
        self.suit = card_string[-1]
        if self.value == 'T':
            self.rank = 10
        elif self.value == 'J':
            self.rank = 11
        elif self.value == 'Q':
            self.rank = 12
        elif self.value == "K":
            self.rank = 13
        elif self.value == 'A':
            self.rank = 14
        else:
            self.rank = int(self.value)
        self.string_rank = "0"
        if self.rank >= 10:
            self.string_rank = str(self.rank)
        else:
            self.string_rank += str(self.rank)

    def __gt__(self, other_card):
        return self.rank > other_card.rank

    def __lt__(self, other_card):
        return self.rank < other_card.rank

    def __eq__(self, other_card):
        return self.rank == other_card.rank

    def __repr__(self):
        return self.value + self.suit



class Hand():
    def __init__(self, cards):
        self.cards = cards
        self.cards.sort()
        self.cards.reverse()
        self.flush = True
        suit = cards[0].suit
        for card in cards:
            if card.suit != suit:
                self.flush = False
                break
        self.straight = True
        self.big_pair = []
        self.small_pair = []
        self.high_value = cards[0].rank
        current = self.high_value
        is_first_card = True
        for card in cards:
            if is_first_card:
                is_first_card = False
                continue
            if current == card.rank:
                if not self.big_pair:
                    self.big_pair.append(card.rank)
                    self.big_pair.append(card.rank)
                elif current in self.big_pair:
                    self.big_pair.append(card.rank)
                elif current in self.small_pair:
                    self.small_pair.append(card.rank)
                else:
                    self.small_pair.append(card.rank)
                    self.small_pair.append(card.rank)
            if current != card.rank + 1:
                self.straight = False
            current = card.rank
        if len(self.big_pair) < len(self.small_pair):
            self.big_pair, self.small_pair = self.small_pair, self.big_pair
        self.hand_type = None
        self.hand_rank = ""
        if self.flush:
            if self.straight:
                if self.high_value == 14: #High card is an ace
                    self.hand_type = "Royal Flush"
                    self.hand_rank += "9"
                else:
                    self.hand_type = "Straight Flush"
                    self.hand_rank += "8"
            else:
                self.hand_type = "Flush"
                self.hand_rank += "5"
        elif self.straight:
            self.hand_type = "Straight"
            self.hand_rank += "4"
        elif len(self.big_pair) == 4:
            self.hand_type = "Four of a Kind"
            self.hand_rank += "7"
        elif len(self.big_pair) == 3:
            if self.small_pair:
                self.hand_type = "Full House"
                self.hand_rank += "6"
            else:
                self.hand_type = "Three of a Kind"
                self.hand_rank += "3"
        elif len(self.big_pair) == 2:
            if self.small_pair:
                self.hand_type = "Two Pairs"
                self.hand_rank += "2"
            else:
                self.hand_type = "One Pair"
                self.hand_rank  += "1"
        else:
            self.hand_type = "High Card"
            self.hand_rank += "0"
        if not self.big_pair:
            for card in cards:
                self.hand_rank += card.string_rank
        else:
            for card in cards:
                if card.rank in self.big_pair:
                    self.hand_rank += card.string_rank
            for card in cards:
                if card.rank in self.small_pair:
                    self.hand_rank += card.string_rank
            for card in cards:
                if card.rank not in self.big_pair and card.rank not in self.small_pair:
                    self.hand_rank += card.string_rank
        if cards[0].suit == "S":
            self.hand_rank += "3"
        elif cards[0].suit == "D":
            self.hand_rank += "2"
        elif cards[0].suit == "H":
            self.hand_rank += "1"
        else:
            self.hand_rank += "0"
        self.hand_rank = int(self.hand_rank)

    def __gt__(self, other_hand):
        return self.hand_rank > other_hand.hand_rank

    def __lt__(self, other_hand):
        return self.hand_rank < other_hand.hand_rank

    def __eq__(self, other_hand):
        return self.hand_rank == other_hand.hand_rank

    def __repr__(self):
        return repr(self.cards)


def convert_to_hands(card_list):
    first_hand = []
    second_hand = []
    counter = 0
    for card in card_list:
        if counter < 5:
            first_hand.append(Card(card))
        else:
            second_hand.append(Card(card))
        counter += 1
    player_one = Hand(first_hand)
    player_two = Hand(second_hand)
    return player_one, player_two


comparison_list = []
poker_doc = open("p054_poker.txt", "r")
total_won = 0
for line in poker_doc:
    card_list = line.split()
    player_one, player_two = convert_to_hands(card_list)
    if player_one > player_two:
        total_won += 1
print total_won


# ###TESTING
# list_combos = []
# list_combos.append(convert_to_hands(["5H", '5C', '6S', '7S', 'KD', '2C', '3S', '8S', '8D', 'TD']))
# list_combos.append(convert_to_hands(["5D", '8C', '9S', 'JS', 'AC', '2C', '5C', '7D', '8S', 'QH']))
# list_combos.append(convert_to_hands(["2D", '9C', 'AS', 'AH', 'AC', '3D', '6D', '7D', 'TD', 'QD']))
# list_combos.append(convert_to_hands(["4D", '6S', '9H', 'QH', 'QC', '3D', '6D', '7H', 'QD', 'QS']))
# list_combos.append(convert_to_hands(["2H", '2D', '4C', '4D', '4S', '3C', '3D', '3S', '9S', '9D']))


# for game in list_combos:
#     player_one, player_two = game
#     print "Player One: ", player_one, player_one.hand_type
#     print player_one.big_pair, player_one.small_pair
#     print "Player Two:", player_two, player_two.hand_type
#     print player_two.big_pair, player_two.small_pair
#     if player_one > player_two:
#         print "Player One Wins!"
#     else:
#         print "Player Two Wins!"
#     print ""


