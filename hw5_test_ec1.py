"""
############################## Homework #5 ##############################

% Student Name: Hisamitsu Maeda

% Student Unique Name: himaeda

% Lab Section 00X: 103 (non-SI student)

% I worked with the following classmates: Nobody

"""

import unittest
import hw5_cards_ec1

class TestHand(unittest.TestCase):

    def test_construct_Hand(self):
        d1 = hw5_cards_ec1.Deck()
        cards = d1.deal_hand(5)
        h1 = hw5_cards_ec1.Hand(cards)

        self.assertEqual(len(h1.init_cards), 5)
        self.assertEqual(len(d1.cards), 47)

    def testAddAndRemove(self):
        '''
        Test tha add_card() and remove_card()
        '''
        d1 = hw5_cards_ec1.Deck()
        cards = d1.deal_hand(5)
        h1 = hw5_cards_ec1.Hand(cards)
        # test add_card()
        c1 = d1.deal_card()
        pre_hand_size1 = len(h1.init_cards)
        h1.add_card(c1)
        self.assertEqual(len(h1.init_cards) - pre_hand_size1, 1)
        # test remove_card()
        pre_hand_size2 = len(h1.init_cards)
        c2 = h1.remove_card(c1)
        # test whether removing same card
        self.assertEqual(c1.__str__(), c2.__str__())
        # test the length reduced
        self.assertEqual(pre_hand_size2 - len(h1.init_cards), 1)

    def testDraw(self):
        d1 = hw5_cards_ec1.Deck()
        cards = d1.deal_hand(5)
        h1 = hw5_cards_ec1.Hand(cards)

        pre_hand_size = len(h1.init_cards)
        pre_deck_size = len(d1.cards)
        h1.draw(d1)
        # test draw works correctly
        self.assertEqual(len(h1.init_cards) - pre_hand_size, 1)
        # test side effects
        self.assertEqual(pre_deck_size - len(d1.cards), 1)



if __name__=="__main__":
    unittest.main()