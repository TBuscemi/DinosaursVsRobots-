from fleet import Fleet
from herd import Herd
import random

def attacker (attacker, defender):
    defender.hit_points -= attacker.weapon.damage
    print (attacker.weapon.damage)
    print(defender.hit_points)


def get_random_number(num_1, num_2):
    random_int = random_number(num_1, num_2)
    return random_int


def random_number(min_value, max_value):
    return random.randint(min_value, max_value)


class Battle_Field:

    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()




# this is an intro to the big battle


    def battle(self):   
        print("WELCOME TOO DINSAURS VS ROBOTS!!!!!")
        print ("SO WITH OUT SO WITHOUT FURTHER ADIEU LETS GET READY TO RUMBLE!")
        
        dino_fighters = 3
        robo_fighters = 3
        d = 0
        r = 0
        while dino_fighters >0 and robo_fighters >0:


            fighter = get_random_number(1, 20)  

                
            if fighter <= 10:
                attacker(self.herd.dino_profile[d], self.fleet.robot_profile[r])
                print(f"{self.herd.dino_profile[d].name} Attacks with {self.herd.dino_profile[d].weapon.weapon_name}")

            if fighter >= 11:
                attacker(self.fleet.robot_profile[r], self.herd.dino_profile[d])
                print(f"{self.fleet.robot_profile[r].name} Attacks with {self.fleet.robot_profile[r].weapon.weapon_name}")
            

 
            if self.herd.dino_profile[d].hit_points > 0:
                print(f"{self.herd.dino_profile[d].name}'s Hit-Points = {self.herd.dino_profile[d].hit_points}")
            
            if self.fleet.robot_profile[r].hit_points > 0:
                print(f"{self.fleet.robot_profile[r].name}'s Hit-Points = {self.fleet.robot_profile[r].hit_points}")



            if self.herd.dino_profile[d].hit_points <= 0:
                print(f"{self.herd.dino_profile[d].name} HAS BECOME EXTINCT!!")
                d += 1
                dino_fighters -= 1

            if self.fleet.robot_profile[r].hit_points <= 0:
                print(f"{self.fleet.robot_profile[r].name} OOOOO HE IS NOTHING BUT SCRAP!!")
                r += 1
                robo_fighters -= 1

            
            if d == 3:
                print("IT LOOKS LIKE SCIENCE BEATS INSTINCT! THE ROBOTS WIN! ")
                break
            if r == 3:
                print("OMG WHO COULD OF SAW THIS! THE BLAST FROM THE PAST STOMPED ALL OVER THE FUTURE! THE DINOSAURS WIN!")
                break
       


Battle_Field().battle()
