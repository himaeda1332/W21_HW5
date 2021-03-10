"""
############################## Homework #5 ##############################

% Student Name: Hisamitsu Maeda

% Student Unique Name: himaeda

% Lab Section 00X: 103 (non-SI student)

% I worked with the following classmates: Nobody

"""

import unittest
import hw5_cards_ec2

class TestHand(unittest.TestCase):

    def test_construct_Hand(self):
        d1 = hw5_cards_ec2.Deck()
        cards = d1.deal_hand(5)
        h1 = hw5_cards_ec2.Hand(cards)

        self.assertEqual(len(h1.init_cards), 5)
        self.assertEqual(len(d1.cards), 47)

    def test_remove_pairs(self):
        '''
        Test tha add_card() and remove_card()
        '''
        d1 = hw5_cards_ec2.Deck()
        cards = d1.deal_hand(18)
        h1 = hw5_cards_ec2.Hand(cards)
        # test remove_pairs
        pre_hand_size = len(h1.init_cards)
        self.assertEqual(len(h1.init_cards), 18)
        h1.remove_pairs() # 6, 7, 8, 9, 10, 11, 12, 13
        self.assertEqual(len(h1.init_cards), 8)

        # case no pair
        d1 = hw5_cards_ec2.Deck()
        cards = d1.deal_hand(5)
        h1 = hw5_cards_ec2.Hand(cards)
        pre_hand_size = len(h1.init_cards)
        self.assertEqual(len(h1.init_cards), 5)
        h1.remove_pairs()
        self.assertEqual(len(h1.init_cards), 5)


    def test_deal(self):
        d1 = hw5_cards_ec2.Deck()
        hand_list = d1.deal(3, 5)
        # check hand_list contains Hand class
        self.assertIsInstance(hand_list[0], hw5_cards_ec2.Hand)
        # check a Hand has 5 cards
        self.assertEqual(len(hand_list[0].init_cards), 5)
        # check the number of rest cards in Deck
        self.assertEqual(len(d1.cards), 52 - 15)

        # test edge cases
        d1 = hw5_cards_ec2.Deck()
        hand_list = d1.deal(5, -1)
        # check the first Hand has 11 and the last Hand has 10
        self.assertEqual(len(hand_list[0].init_cards), 11)
        self.assertEqual(len(hand_list[-1].init_cards), 10)
        # check the number of rest cards in Deck
        self.assertEqual(len(d1.cards), 0)

        # test edge cases
        d1 = hw5_cards_ec2.Deck()
        hand_list = d1.deal(60, 100)
        # check the first Hand has 1 and the last Hand has 0
        self.assertEqual(len(hand_list[0].init_cards), 1)
        self.assertEqual(len(hand_list[-1].init_cards), 0)
        # check the number of rest cards in Deck
        self.assertEqual(len(d1.cards), 0)



if __name__=="__main__":
    unittest.main()