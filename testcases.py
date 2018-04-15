import unittest
from nqs import Queue
from assignment_a_starter import Board

class TestBoard(unittest.TestCase):
    def test_update_for_multiple_numbers_of_equal_balls(self):
        pipe = [azure, azure, azure, azure, azure, azure,]
        brd = Board(pipe)

        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.update()

        self.assertEqual(brd.num_piles(), 0)
        self.assertIs(brd._front, None)
        self.assertEqual(brd._score, 12)

    def test_update_remove_one_triplet_of_balls(self):
        pipe = [azure, azure, mauve, mauve, mauve, azure,]
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.update()

        self.assertEqual(brd.num_piles(), 2)
        self.assertEqual(brd._score, 4)
        self.assertIs(brd._front.get_value().peek(), 'azure')
        self.assertIs(brd._front.next.get_value().peek(), 'azure')

    def test_pluck_pluck_up(self):
        pipe = [azure, azure, azure, mauve, amber, mauve, amber, azure, azure,]
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.drop(3)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)

        brd.pluck(6)
        brd.update()

        selt.assertEqual(brd.num_piles(), 5)
        self.assertEqual(brd._score, -1)
        
    def test_empty_pipe(self):
        pipe = []
        brd.drop(0)

        self.assertIsNot(brd._front, None)
# testing to see what happens when you try to drop from an empty pipe

