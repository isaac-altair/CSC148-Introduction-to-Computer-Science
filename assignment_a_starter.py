'''
    CSC148: Assignment A
            Marble Drop
            
    Author(s):  YOUR UTORID(S)
    abdull68
    c3girich
'''
import unittest
import random
from nqs import Node, Queue, Stack

MIN_PATTERN_LENGTH = 3
NUM_MARBLES = 100
PUZZLE_NUM = 1          # Play puzzle #1

COLOURS = ['amber',
           'mauve',
           'azure',
           'ochre',
           'peach']


def generate_random_puzzle(puzzle_size):
    '''Return a list of numbers for a random puzzle of puzzle_size.'''
    puzzle = []
    
    for i in range(puzzle_size):
        puzzle.append(random.randint(0, len(COLOURS)))
        
    return puzzle

# Puzzle #0 is a random puzzle.
PRESET_PUZZLES = [
    # This generates 
    generate_random_puzzle(NUM_MARBLES),

    [3, 1, 0, 4, 1, 1, 2, 1, 1, 4, 1, 0, 1, 2, 0, 1, 3, 0, 0, 2, 0, 1, 3, 0, 1,
     1, 1, 3, 4, 3, 0, 0, 3, 0, 2, 1, 3, 3, 1, 2, 3, 1, 0, 3, 1, 4, 1, 4, 0, 2,
     2, 4, 3, 2, 4, 0, 3, 2, 1, 2, 2, 4, 1, 3, 2, 3, 3, 1, 1, 1, 1, 4, 3, 2, 1,
     4, 1, 2, 3, 3, 4, 0, 1, 2, 4, 3, 0, 3, 2, 4, 1, 1, 1, 2, 2, 4, 4, 1, 2, 0
     ],

    [0, 1, 0, 1, 1, 0, 0, 1, 2, 1, 4, 2, 3, 0, 4, 3, 4, 0, 0, 3, 2, 2, 0, 4, 3,
     3, 2, 3, 4, 2, 3, 2, 2, 4, 0, 2, 1, 4, 2, 4, 3, 3, 0, 4, 1, 1, 3, 1, 1, 0,
     2, 3, 0, 0, 0, 0, 4, 0, 0, 3, 2, 2, 4, 4, 4, 3, 3, 3, 0, 4, 1, 0, 2, 3, 3,
     2, 1, 1, 2, 2, 0, 4, 0, 0, 4, 1, 4, 3, 3, 2, 0, 0, 0, 1, 0, 3, 2, 0, 1, 0
     ],
    ]


class MoveCancelled(Exception):
    '''A MoveCancelled exception is raised when the user was selecting a pile
    but then decides not to perform the specified move.'''


class Board(object):
    
    def __init__(self, pipe):
        '''Initialize self with pipe containing marble colours.'''

        # If you're not sure what data type _front should refer to, take a look
        # at the display method.
        self._front = None
        self._pipe = pipe
        self._score = 0

    def drop(self, pile):
        
        c_pile = self._front
        if not self._pipe.front() is None:
            dropping_ball_val = self._pipe.dequeue()
            dropping_ball = Node(dropping_ball_val)
            #Create Stack at front of linked list with dropped ball
            if pile == 0:
                old_front = self._front
                self._front = Node(Stack())
                self._front._value.push(dropping_ball._value)
                print(self._front._value.peek())
                self._front.next = old_front
            #check if board entirely empty
            elif self._front is None:
                self._front = Node(Stack())
                self._front._value.push(dropping_ball._value)
            #Unempty board and inserting into non-zero pile
            else:
                #check if inserting into first pile
                counter = 1
                
                if counter == pile:
                    c_pile._value.push(dropping_ball._value)

                while counter < pile:
                    counter += 1
                    #go to next item if exists
                    if not c_pile.next is None:
                        c_pile = c_pile.next
                        if counter == pile:
                            c_pile._value.push(dropping_ball._value)
                    #append to end of LL if end of list reached
                    else:
                        c_pile.next = Node(Stack())
                        c_pile.next._value.push(dropping_ball._value)
        if c_pile is None:
            c_pile = self._front

        self._score -= 1
        
    def num_piles(self) ->float:
        ''' returns the number of piles on the board '''
        c_node = self._front
        if c_node is None:
            return 0
        counter = 0
        while not c_node is None:
            counter += 1
            c_node = c_node.next
        return counter

    def pluck(self, pile):
        ''' plucks the uppermost colour from the stack given
        and places it back in the pipe'''
        c_pile = self._front
        prev_pile = None
        # Case 1: Pile is empty
        if c_pile is None:
            return None
        # Case 2: Pile contains exactly one element
        counter = 0
        while counter < pile:
            counter += 1
            if counter == pile:
                self._pipe.enqueue(c_pile._value.pop())
                if c_pile._value.is_empty():
                    if prev_pile is None:
                        #then first pile is now empty.
                        if not c_pile.next is None:
                            self._front = c_pile.next
                        else:
                            self._front = None
                    else:
                        if not c_pile.next is None:
                            prev_pile.next = c_pile.next
                        else:
                            prev_pile.next = None
            else: 
                #counter != pile
                prev_pile = c_pile
                if not c_pile.next is None:
                    c_pile = c_pile.next
                else:
                    return None
        self._score -= 1

    def swap(self, nth_pile):
        '''Assume pile is valid input between 1 and the num_piles'''
        counter = 1
        c_pile = self._front
        last_node = self._front
        nth_node = self._front
        #if self.num_piles() > 0:
        if nth_pile > self.num_piles():
            self._score -= 1
            return None
        while not last_node.next is None:
            last_node = last_node.next
        while counter < nth_pile:
            if c_pile is None:
                self._score -= 1
                return None
            counter += 1
            c_pile = c_pile.next
        if counter == nth_pile:
            nth_node = c_pile
            c_pile = c_pile.next 
        last_node.next = self._front
        self._front = c_pile
        nth_node.next = None
        self._score -= 1
        
    def update(self):
        ''' updates the game board '''
        i = 1
        c_pile = self._front
        prev_node = self._front
        score = self._score
        # Take care of the case where pile contains only one ball
        # Create a loop to go over the all elements, not just 3
        while self.num_piles() <= 3 and not c_pile._value.is_empty():            
            peek_1 = c_pile._value.peek()
            peek_2 = c_pile.next._value.peek()
            peek_3 = c_pile.next.next._value.peek()
            if peek_1:
                i = 1
                if peek_1 == peek_2:
                    i = 2
                    if peek_2 == peek_3:
                        i = 3    
                        c_pile._value.pop()
                        c_pile.next._value.pop()
                        c_pile.next.next._value.pop()
                        score += 3
                    else:
                        c_pile = c_pile.next
                else:
                    c_pile = c_pile.next
        if c_pile._value.is_empty():
            c_pile = c_pile.next 
        self._score += score ** 2

    def get_pile(self, min_val):
        '''Get and return a pile number from the user.
        The number entered must be between min_val and the number of piles in
        self (inclusive).'''

        # This ensures the while loop runs at least once.
        pile_num = min_val - 1

        # Loop until a valid pile number is entered.
        while min_val > pile_num or pile_num > self.num_piles():
            pile = input('Enter a pile number or "cancel": ')
            if pile == 'cancel':
                raise MoveCancelled()

            try:
                pile_num = int(pile)
            except ValueError:
                pass
        return pile_num

    def display(self):
        '''Display self to the user.'''

        cur_node = self._front
        print()

        # Display pipe contents
        if not self._pipe.is_empty():
            print('Pipe: ', self._pipe.front(),
                  '(' + str(len(self._pipe)) +
                  ' items remain)')
        else:
            print('Pipe is empty.')

        # Display pile contents
        print("Piles: ", end='')
        while cur_node:
            print(cur_node.get_value().peek(), end=' ')
            cur_node = cur_node.next

        # Display player score
        print()
        print('Score:', self._score)
        print()


def main() -> None:
    '''The main driver for the game.'''

    pipe = Queue()
    for i in range(len(PRESET_PUZZLES[PUZZLE_NUM])):
        pipe.enqueue(COLOURS[PRESET_PUZZLES[PUZZLE_NUM][i]])

    brd = Board(pipe)
    choice = ''

    while choice != 'exit':
        #brd.update()
        brd.display()
        choice = input('Action (Type "help" for available actions): ')

        try:
            if choice == 'help':
                print('Available actions: drop, pluck, swap, exit')

            elif choice == 'drop':
                brd.drop(brd.get_pile(0))

            elif choice == 'pluck':
                brd.pluck(brd.get_pile(1))

            elif choice == 'swap':
                brd.swap(brd.get_pile(1))

        except MoveCancelled:
            pass

if __name__ == '__main__':
    main()
    
  
class TestBoard(unittest.TestCase):
    
    def test_update_for_multiple_numbers_of_equal_balls(self):
        pipe = [azure, azure, azure, azure, azure, azure, ]
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
        pipe = [azure, azure, mauve, mauve, mauve, azure, ]
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
        pipe = [azure, azure, mauve, azure, mauve, mauve, amber, azure, ]
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.drop(3)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.drop(0)
        brd.update()

        selt.assertEqual(brd.num_piles(), 5)
        self.assertEqual(brd._score, -1)
        
    def test_empty_pipe(self):
        
        pipe = []
        brd.drop(0)

        self.assertIsNot(brd._front, None)
        # testing to see what happens when you try to drop from an empty pipe

