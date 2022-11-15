import random
from time import sleep


class Card:
    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    values = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10, "Queen": 10, "King": 10}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{} of {}'.format(self.rank, self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def give_card(self):
        return self.cards.pop()

    def __str__(self):
        for i, card in enumerate(self.cards):
            print(i + 1, card)
        return ""


class Player:

    def __init__(self, balance):
        self.hand = []
        self.value = 0
        self.balance = int(balance)

    def add_card(self, card):
        if card.rank == "Ace":
            choice = int(input(">>> You have Ace. Press 0 if you want 1 point or 1 if you want 11 point"))
            self.hand.append(card)
            if choice:
                self.value += 11
            else:
                self.value = 1
        else:
            self.hand.append(card)
            self.value += Card.values[card.rank]

    def remove_cards(self):
        self.hand = []
        self.value = 0

    def increase_balance(self, balance):
        self.balance = self.balance + int(balance)

    def decrease_balance(self, balance):
        self.balance = self.balance - int(balance)

    def show_cards(self):
        """
        shows all cards in hand
        :return list of cards:
        """
        print("-" * 100)
        print(">>> {} has: ".format(type(self).__name__), end='')
        print('{}'.format(str(self.hand)[1:-1]))
        print(">>> Value: {}".format(self.value))
        print("-" * 100)

    def __str__(self):
        return "-" * 100 + '\n' + 'Player balance: {}\n' \
               'Cards: {}\n' \
               'Value: {}'.format(self.balance, str(self.hand)[1:-1], self.value) + "\n" + "-" * 100


class Dealer(Player):

    def __init__(self):
        self.hand = []
        self.value = 0

    def __str__(self):
        return 'Dealer has {}'.format(self.hand)

    def show_card(self):
        """
        shows the first card in dealer's hand
        :return str of card:
        """
        print("-" * 100)
        print(">>> Dealer has: ", end='')
        print('{}'.format(self.hand[0]))
        if self.hand[0].rank == "Ace":
            print(">>> Value: {}".format(11))
        else:
            print(">>> Value: {}".format(Card.values[self.hand[0].rank]))
        print("-" * 100)

    def add_card(self, card):
        if card.rank == "Ace":
            self.value += 11
            self.hand.append(card)
        else:
            self.hand.append(card)
            self.value += Card.values[card.rank]


if __name__ == "__main__":
    new_deck = Deck()
    player1 = Player(100)
    dealer = Dealer()
    answer = ''
    while True:

        # Ввод значения
        while True:
            bet = int(input(">>> Please place a bet: "))
            if bet > player1.balance:
                print("Invalid amount")
                continue
            break

        player1.decrease_balance(bet)
        dealer.add_card(new_deck.give_card())
        dealer.add_card(new_deck.give_card())
        dealer.show_card()
        player1.add_card(new_deck.give_card())
        player1.add_card(new_deck.give_card())
        player1.show_cards()

        if dealer.value == 21 or player1.value == 21:
            if dealer.value == 21 and player1.value == 21:
                sleep(0.5)
                print("-" * 100)
                print('>>> You both win!!!')
                print("-" * 100)
                sleep(0.5)
                player1.increase_balance(bet)
                print(player1)
                sleep(0.5)
                continue
        if dealer.value > 21 or player1.value > 21:
            if dealer.value > 21 and player1.value > 21:
                sleep(0.5)
                print("-" * 100)
                print(">>> No one wins!!!")
                print("-" * 100)
                sleep(0.5)
                player1.increase_balance(bet)
            elif dealer.value > 21:
                sleep(0.5)
                print("-" * 100)
                print(">>> Player wins!!!")
                print("-" * 100)
                sleep(0.5)
                player1.increase_balance(2 * bet)
            else:
                sleep(0.5)
                print("-" * 100)
                print(">>> Dealer wins!!!")
                print("-" * 100)
                sleep(0.5)


        while answer not in ('yes', 'no'):
            answer = input('>>> Do you want to Hit?(yes/no) \n>>> ')
            if answer not in('yes', 'no'):
                print("Invalid input!")
        while answer == 'no':

            player1.add_card(new_deck.give_card())
            player1.show_cards()

            if dealer.value > 21 or player1.value > 21:
                print("Dealer's value: {}", dealer.value)
                if dealer.value > 21 and player1.value > 21:
                    sleep(0.5)
                    print(">>> No one wins!!!")
                    player1.increase_balance(bet)
                    sleep(0.5)
                elif dealer.value > 21:
                    sleep(0.5)
                    print(">>> Player wins!!!")
                    player1.increase_balance(2 * bet)
                    sleep(0.5)
                else:
                    sleep(0.5)
                    print(">>> Dealer wins!!!")
                    sleep(0.5)
            while answer not in ('yes', 'no'):
                answer = input('>>> Do you want to Hit?(yes/no) \n>>> ')
                if answer not in ('yes', 'no'):
                    print("Invalid input!")

        if dealer.value > player1.value:
            sleep(0.5)
            print('>>> Dealer wins!!!')
            sleep(0.5)
        elif dealer.value == player1.value:
            sleep(0.5)
            print('>>> No one wins!!!')
            sleep(0.5)
        else:
            sleep(0.5)
            print('>>> Player wins!!!')
            sleep(0.5)
            player1.increase_balance(2 * bet)

        dealer.show_cards()
        print(player1)
        sleep(0.5)

        new_deck = Deck()
        player1.remove_cards()
        dealer.remove_cards()
        print('-' * 100)

