from robot import Robots
from weapon import Weapon

class Fleet:


    def __init__(self, robot_profile, weapon_profile):
        self.robot_profile  = robot_profile 
        self.weapon_profile = weapon_profile
        
        self.robot_profile = [Robots("Boss", 100),Robots("Mech boy", 100),Robots("gorkanaut", 100)]
        self.weapon_profile = [Weapon("Boom Stick", 10),Weapon("beam saber", 10),Weapon("Missles", 10)]      
        

        