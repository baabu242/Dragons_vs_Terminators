from .dragon import Dragon


class FireDragon(Dragon):
    """FireDragon cooks any Terminator in its Place when it expires."""

    name = 'Fire'
    damage = 3
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.2
    implemented = True  # Change to True to view in the GUI
    food_cost = 5
    # END 2.2

    def __init__(self, armor=3):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the FireDragon from its place if it
        has no armor remaining.

        Make sure to damage each terminator in the current place, and apply the bonus
        if the fire dragon dies.
        """
        # BEGIN 2.2
        "*** YOUR CODE HERE ***"
        self.armor -= amount
        for i in range(0, len(self.place.terminators)) :
            self.place.terminators[i].armor -= amount

        l = []
        if self.armor == 0 :
            for i in range(0, len(self.place.terminators)) :
                self.place.terminators[i].armor -= self.damage
                if self.place.terminators[i].armor <= 0 :
                    l.append(self.place.terminators[i])

            for i in l :
                i.place.remove_fighter(i)
                i.death_callback()
            self.place.remove_fighter(self)
            self.death_callback()
