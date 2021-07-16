from robot import Robots
from weapon import Weapon

class Fleet:


    def __init__(self):  
        self.robot_profile = [Robots("Boss", 100, Weapon("Boom Stick", 10)),
                            Robots("Mech boy", 100, Weapon("Beam Saber", 10)),
                            Robots("gorkanaut", 100, Weapon("missles", 10))]
        # self.weapon_profile = [Weapon("Boom Stick", 10),Weapon("beam saber", 10),Weapon("Missles", 10)]      
        

        