from dinosaur import Dinosaur
from weapon import Weapon

class Herd:


    def __init__(self):
        self.dino_profile = [Dinosaur("REX" ,100 , Weapon("claws",25)),Dinosaur("Velociraptor" ,100 ,Weapon("cLAWS",25)),Dinosaur("Megalosaurus" ,100 ,Weapon("claws",25))]

        