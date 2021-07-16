from robot import Robots
from weapon import Weapon

class Fleet:


    def __init__(self):  
        self.robot_profile = [Robots("Boss", 100, Weapon("Boom Stick", 25)),
                            Robots("Mech boy", 100, Weapon("Beam Saber", 25)),
                            Robots("gorkanaut", 100, Weapon("missles", 25))]
     
        

        