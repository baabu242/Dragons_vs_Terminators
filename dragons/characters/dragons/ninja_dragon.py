from .dragon import Dragon


class NinjaDragon(Dragon):
    """NinjaDragon does not block the path and damages all terminators in its place."""

    name = 'Ninja'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.4
    implemented = True  # Change to True to view in the GUI
    blocks_path = False
    food_cost = 5
    # END 2.4

    def action(self, colony):
        # BEGIN 2.4
        "*** YOUR CODE HERE ***"
        l = []
        for i in self.place.terminators :
            i.armor -= self.damage
            if i.armor <= 0 :
                l.append(i)
        for i in l :
            i.place.remove_fighter(i)
            i.death_callback()