from .dragon import Dragon
from .scuba_thrower import ScubaThrower
from utils import terminators_win
from utils import random_or_none

class DragonKing(Dragon):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    implemented = True  # Change to True to view in the GUI
    is_watersafe = True
    food_cost = 7
    instantiated = False
    dking = True
    damage = 1
    # END 4.3

    def __init__(self, armor=1):
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        Dragon.__init__(self, armor)
        self.king = False
        if DragonKing.instantiated is False :
            DragonKing.instantiated = True
            self.king = True
        # END 4.3

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        # BEGIN 1.3 and 2.1
        s = self.place

        while s != skynet :
            if len(s.terminators) > 0 :
                return random_or_none(s.terminators)
            s = s.entrance
        if s is skynet :
            return None
        # END 1.3 and 2.1

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        #print(self.instantiated,'\n')
        if self.king :
            k = self.place.exit
            while k is not None :
                if k.dragon is not None :
                    if k.dragon.is_buffed is False :
                        if not k.dragon is self :
                            k.dragon.damage *= 2
                            k.dragon.is_buffed = True
                    if k.dragon.is_container is True and k.dragon.contained_dragon is not None :
                        t = k.dragon.contained_dragon
                        if not t is self and t.is_buffed is False:
                            k.dragon.contained_dragon.damage *= 2
                            k.dragon.contained_dragon.is_buffed = True
                k = k.exit
            s = self.nearest_terminator(colony.skynet)
            if s is not None :
                s.reduce_armor(self.damage)

        else:
            self.armor = 0
            self.place.remove_fighter(self)
            self.death_callback()
        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        self.armor -= amount
        if self.armor <= 0 and self.king is True:
            terminators_win()