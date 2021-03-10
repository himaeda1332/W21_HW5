import random
import unittest

VERSION = 0.01

class Card:
    '''a standard playing card
    cards will have a suit and a rank
    Class Attributes
    ----------------
    suit_names: list
        the four suit names in order
        0:Diamonds, 1:Clubs, 2: Hearts, 3: Spades

    faces: dict
        maps face cards' rank name
        1:Ace, 11:Jack, 12:Queen,  13:King
    Instance Attributes
    -------------------
    suit: int
        the numerical index into the suit_names list
    suit_name: string
        the name of the card's suit
    rank: int
        the numerical rank of the card
    rank_name: string
        the name of the card's rank (e.g., "King" or "3")
    '''
    suit_names = ["Diamonds", "Clubs", "Hearts", "Spades"]
    faces = {1: "Ace",11: "Jack",12: "Queen",13: "King"}


    def __init__(self, suit=0,rank=2):
        self.suit = suit
        self.suit_name = Card.suit_names[self.suit]

        self.rank = rank
        if self.rank in Card.faces:
            self.rank_name = Card.faces[self.rank]
        else:
            self.rank_name = str(self.rank)

    def __str__(self):
        return f"{self.rank_name} of {self.suit_name}"


class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self):

        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order

    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card
        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i)

    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters
        ----------
        None
        Returns
        -------
        None
        '''
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list

    def sort_cards(self):
        '''returns the Deck to its original order

        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters
        ----------
        None
        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit,rank)
                self.cards.append(card)

    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck

        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck
        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards

    def deal(self, num_of_hands, num_of_cards=-1):
        '''distribute cards according to the number
        of hands and the number of cards
        Parameters
        ---------------
        num_of_hands: int
            the number of hands
        num_of_cards: int
            the number of cards per hand default is -1
            if the number of cards = -1, all of the cards
            should be dealt
        Returns
        ---------------
        the list of Hnad
        '''
        # compute the number of cards per hand
        if num_of_cards == -1:
            num_of_cards = len(self.cards)
        total_num_of_cards = min(num_of_cards * num_of_hands,
                                len(self.cards))
        hand_dict = {i: 0 for i in range(num_of_hands)}
        for i in range(total_num_of_cards):
            hand_dict[i % num_of_hands] += 1
        # create output list
        hands_list = []
        for idx in hand_dict.keys():
            cards = self.deal_hand(hand_dict[idx])
            h = Hand(cards)
            hands_list.append(h)
        return hands_list


def print_hand(hand):
    '''prints a hand in a compact form

    Parameters
    -------------------
    hand: list
        list of Cards to print
    Returns
    -------
    none
    '''
    hand_str = '/ '
    for c in hand:
        s = c.suit_name[0]
        r = c.rank_name[0]
        hand_str += r + "of" + s + ' / '
    print(hand_str)

class Hand:
    '''a hand for playing card

    Class Attributes
    ----------------
    None

    Instance Attributes
    -------------------
    init_card: list
    a list of cards
    '''
    def __init__(self, init_cards):
        self.init_cards = init_cards

    def add_card(self, card):
        '''add a card
        add a card to the hand
        silently fails if the card is already in the hand
        parameters
        ----------------
        card: instance
            a card to add
        Returns
        ----------------
        None
        '''
        card_strs = [] # forming an empty list
        for c in self.init_cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.init_cards.append(card) # append it to the list

    def remove_card(self, card):
        '''remove a card from the hand
        Parameters
        -----------------
        card: instance
            a card to remove
        Returns
        -----------------
        the card, or None if the card was not in the Hand
        '''
        card_strs = [] # forming an empty list
        for c in self.init_cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() in card_strs:
            self.init_cards.remove(card)
            return card

    def draw(self, deck):
        '''draw a card
        draw a card from a deck and add it to the hand
        side effect: the deck will be depleted by one card
        Parameters
        -----------------
        deck instance
            a deck from which to draw
        Returns
        -----------------
        None
        '''
        card = deck.deal_card()
        self.add_card(card)

    def remove_pairs(self):
        '''look for pairs of cards in a hand and
        remove all of them from hand
        Parameters
        ---------------
        None
        Returns
        ---------------
        None
        '''
        cards_list = []
        rank_list = []
        for card in self.init_cards:
            # if there is a pair in the list
            if card.rank in rank_list:
                idx = rank_list.index(card.rank)
                cards_list.pop(idx)
                rank_list.pop(idx)
            else:
                cards_list.append(card)
                rank_list.append(card.rank)

        self.init_cards = cards_list


