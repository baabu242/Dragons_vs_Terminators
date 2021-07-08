from .bodyguard_dragon import BodyguardDragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.3
    implemented = True  # Change to True to view in the GUI
    is_container = True
    food_cost = 6
    # END 3.3

    def action(self, colony):
        # BEGIN 3.3
        "*** YOUR CODE HERE ***"
        BodyguardDragon.action(self,colony)
        l = []
        for i in self.place.terminators:
            i.armor -= self.damage
            if i.armor <= 0:
                l.append(i)
        for i in l:
            i.place.remove_fighter(i)
            i.death_callback()