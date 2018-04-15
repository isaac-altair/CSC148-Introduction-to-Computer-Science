import unittest
from nqs import Queue
from assignment_a_starter import Board

def get_pipe_1():
    pipe = Queue()
    pipe.enqueue('mauve')
    pipe.enqueue('amber')
    pipe.enqueue('mauve')
    pipe.enqueue('mauve')
    pipe.enqueue('azure')

    return pipe

def get_pipe_2():
    pipe = Queue()
    pipe.enqueue('amber')
    pipe.enqueue('amber')
    pipe.enqueue('amber')

    return pipe

class TestBoard(unittest.TestCase):
    def test_constructor(self):
        '''I hope you didn't change the code we gave you...'''
        pipe = get_pipe_1()
        brd = Board(pipe)
        
        self.assertEqual(len(pipe), 5)
        self.assertEqual(brd._front, None)
        self.assertEqual(brd._score, 0)

    def test_drop_empty(self):
        pipe = get_pipe_1()
        brd = Board(pipe)
        brd.drop(0)
        
        self.assertEqual(len(pipe), 4, 'Pipe did not lose a marble.')
        self.assertEqual(brd.num_piles(), 1, 'Pile not properly created.')
        self.assertIsNot(brd._front, None, 'Board _front not updated.')
        self.assertIs(brd._front.next, None)
        self.assertEqual(brd._score, -1, 'Score not updated.')

    def test_drop_on_top(self):
        pipe = get_pipe_1()
        brd = Board(pipe)
        brd.drop(0)
        brd.drop(1)
        
        self.assertEqual(len(pipe), 3, 'Pipe did not lose a marble.')
        self.assertEqual(brd.num_piles(), 1, 'Pile not properly created.')
        self.assertIsNot(brd._front, None, 'Board _front not updated.')
        self.assertIs(brd._front.next, None, 'Piles not properly updated.')
        self.assertEqual(brd._score, -2, 'Score not updated.')
        
    def test_pluck_last(self):
        pipe = get_pipe_1()
        brd = Board(pipe)
        while not pipe.is_empty():
            brd.drop(0)
            
        brd.pluck(5)
        self.assertEqual(len(pipe), 1, 'Pipe has incorrect number of marbles.')
        self.assertEqual(brd.num_piles(), 4, 'Pile not properly removed.')
        self.assertIsNot(brd._front, None, 'Board _front not updated.')
        self.assertIs(brd._front.next.next.next.next, None, 'Piles not properly updated.')

        self.assertEqual(brd._score, -6, 'Score not updated.')
        self.assertEqual(pipe.front(), 'mauve', 'Incorrect marble plucked.')

    def test_swap(self):
        pipe = get_pipe_1()
        brd = Board(pipe)
        brd.drop(0)
        brd.drop(0)
        brd.swap(1)
            
        self.assertEqual(brd.num_piles(), 2, 'Pile not properly swapped.')
        self.assertIsNot(brd._front, None, 'Board _front not updated.')
        self.assertIsNot(brd._front.next, None, 'Swapped pile not updated properly.')
        self.assertIs(brd._front.next.next, None, 'Swapped pile not updated properly.')

        self.assertEqual(brd._score, -3, 'Score not updated.')
        self.assertEqual(brd._front.get_value().peek(), 'mauve', 'Incorrect result of swap.')
        self.assertEqual(brd._front.next.get_value().peek(), 'amber', 'Incorrect result of swap.')
        
        
    def test_update_solo(self):
        pipe = get_pipe_2()
        brd = Board(pipe)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.update()
            
        self.assertEqual(brd.num_piles(), 0, 'Pile not properly swapped.')
        self.assertIs(brd._front, None, 'Board _front not updated.')

        self.assertEqual(brd._score, 6, 'Score not updated.')        

if __name__ == '__main__':
    print('Normally, we should not be touching those attributes beginning with',
          'an underscore, but we wanted to keep your starter code simple and',
          'reduce the amount of code you had to write.')
    unittest.main()
