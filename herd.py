from dinosaur import Dinosaur
from weapon import Weapon

class Herd:


    def __init__(self):
        self.dino_profile = [Dinosaur("Tyrannosaurus rex AKA The king" ,100 , Weapon("claws",25)),
                            Dinosaur("Velociraptors AKA The Pack" ,100 ,Weapon("cLAWS",25)),
                            Dinosaur("Mosasaurus AKA The Big Chomp" ,100 ,Weapon("claws",25))]

        