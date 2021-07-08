from .thrower_dragon import ThrowerDragon


class LaserDragon(ThrowerDragon):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.5
    implemented = True  # Change to True to view in the GUI
    food_cost = 10
    damage = 2

    # END 4.5

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self, armor)
        self.fighters_shot = 0

    def fighters_in_front(self, skynet):
        # BEGIN 4.5
        l = []
        k = self.place
        i = 0
        while k is not skynet :
            if k.dragon is not None :
                if k.dragon is not self :
                    l.append((k.dragon, i))
                if k.dragon.is_container is True and k.dragon.contained_dragon is not None :
                    d = k.dragon.contained_dragon
                    if d is not self :
                        l.append((d, i))
            if len(k.terminators) > 0 :
                for item in k.terminators :
                    l.append((item, i))
            k = k.entrance
            i += 1

        return dict(l)
        # END 4.5

    def calculate_damage(self, distance):
        # BEGIN 4.5
        damage = self.damage - 0.2*distance - 0.05*self.fighters_shot
        if damage <= 0 :
            return 0
        else :
            return damage
        # END 4.5

    def action(self, colony):
        fighters_and_distances = self.fighters_in_front(colony.skynet)
        for fighter, distance in fighters_and_distances.items():
            damage = self.calculate_damage(distance)
            fighter.reduce_armor(damage)
            if damage:
                self.fighters_shot += 1
