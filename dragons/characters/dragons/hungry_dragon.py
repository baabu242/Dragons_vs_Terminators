from .dragon import Dragon
from utils import random_or_none

class HungryDragon(Dragon):
    """HungryDragon will take three turns to digest a Terminator in its place.
    While digesting, the HungryDragon can't eat another Terminator.
    """
    name = 'Hungry'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.3
    implemented = True  # Change to True to view in the GUI
    food_cost = 4
    time_to_digest = 3
    digesting = 0
    # END 2.3

    def __init__(self, armor=1):
        # BEGIN 2.3
        "*** YOUR CODE HERE ***"
        Dragon.__init__(self, armor)
        # END 2.3

    def eat_terminator(self, terminator):
        # BEGIN 2.3
        "*** YOUR CODE HERE ***"
        terminator.reduce_armor(terminator.armor)
        self.digesting = self.time_to_digest
        # END 2.3

    def action(self, colony):
        # BEGIN 2.3
        "*** YOUR CODE HERE ***"
        if self.digesting == 0 :
            if len(self.place.terminators) > 0 :
                terminator = random_or_none(self.place.terminators)
                self.eat_terminator(terminator)
        else :
            self.digesting -= 1
