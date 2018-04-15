import random

# TODO: Create an UnpaidBillException whose amount_owed attribute contains the
# amount owed.


class UnpaidBillException(Exception):
    '''Patron has not fully paid his bill and thus owes us.'''
    def __init__(self: 'UnpaidBillException', value: float):
        self.amount_owed = value
##    pass
        

class DidNotOrderThisException(Exception):
    '''Patron received something that was not ordered.'''
##    def __init__(self: 'DidNotOrderThisException', value: str):
##        self.wrong_order = value
    pass
            

class FoodPoisoningException(DidNotOrderThisException):
    '''Patron received something that was not ordered... and that something was
    food poisoning.'''
    pass


# TODO: Add the get_prix_fixe_price method to the Restaurant class.
# The method body is one line long.
class Restaurant(object):
    '''A Restaurant is a location that can be visited by Patrons.'''

    def __init__(self: 'Restaurant', prix_fixe_price: float) -> None:
        '''Initialize a new Restaurant object where the price of a meal is
        prix_fixe_price.'''

        self._prix_fixe_price = prix_fixe_price

        # This dict stores how much each patron in this Restaurant still owes.
        self._patron_to_amount_owing = {}

    def get_prix_fixe_price(self: 'Restaurant'):
        return self._prix_fixe_price

    def get_amount_owing(self: 'Restaurant', patron: 'Patron') -> float:
        '''Return the amount patron owes to this Restaurant.'''

        # If the patron has been served, return the amount owed from the dict.
        if patron in self._patron_to_amount_owing:
            return self._patron_to_amount_owing[patron]

        # The patron has not been served and therefore owes 0.0.
        return 0.0

    def paid_by_patron(self: 'Restaurant',
                       patron: 'Patron',
                       amount: float) -> None:
        '''Reduce how much patron owes to this Restaurant by amount.

        Preconditions: The patron has been served by this Restaurant.'''

        self._patron_to_amount_owing[patron] = \
            self._patron_to_amount_owing[patron] - amount

    def serve(self: 'Restaurant', patron: 'Patron'):
        '''Serve patron and update how much the patron owes.

        If the patron gets food poisoning, the meal just served should be free.
        If the patron is served the wrong order, the meal just served should be
        half price.
        '''

        # Ensure there is a entry for patron in the owing dict.
        if patron not in self._patron_to_amount_owing:
            self._patron_to_amount_owing[patron] = 0

        # TODO: You'll need to change the rest of this method to implement the
        # behaviour in the docstring.

        try:
            patron.eat()

        except FoodPoisoningException:
##            self._patron_to_amount_owing[patron] = 0.0
            self._prix_fixe_price = 0.0
            
        except DidNotOrderThisException:
##            self._patron_to_amount_owing[patron] = \
##                self._patron_to_amount_owing[patron] * 0.5
            self._prix_fixe_price = self._prix_fixe_price * 0.5

        # Increment the amount patron owes.
        self._patron_to_amount_owing[patron] = \
            self._patron_to_amount_owing[patron] + self.get_prix_fixe_price()

    def patron_leaving(self: 'Restaurant', patron: 'Patron') -> None:
        '''Raise an UnpaidBillException if patron owes money to
        this Restaurant.

        Precondition: The patron has been served by this Restaurant.'''

        # TODO: Complete this method to match the docstring.
    ##        self.serve(self.get_amount_owing(UnpaidBillException()))
       ## self.serve(patron)
        if self._patron_to_amount_owing[patron] > 0.0:
            raise UnpaidBillException(self._patron_to_amount_owing[patron])
            ##self._patron_to_amount_owing[patron] != 0.0
    
                         
class Patron(object):
    '''A Patron visits Restaurants and other establishments.'''

    def eat(self: 'Patron') -> None:
        '''Eat a meal. Randomly raise a DidNotOrderThisException or
        FoodPoisoningException.'''

        if random.random() > 0.6:
            if random.random() > 0.4:
                raise DidNotOrderThisException()

            raise FoodPoisoningException()

    def pay_bill(self, restaurant: 'Restaurant') -> None:
        '''Pay the amount owed to restaurant.

        Precondition: The amount owed to restaurant is a positive number.'''

        restaurant.paid_by_patron(self, restaurant.get_amount_owing(self))

        # TODO: Complete this method. To do this:
        #   * Determine how much the patron owes.
        #   * Use the Restaurant paid_by_patron method to pay the bill.


if __name__ == '__main__':

    fancy_restaurant = Restaurant(80.0)
    patron = Patron()
    fancy_restaurant.serve(patron)
    fancy_restaurant.patron_leaving(patron)
