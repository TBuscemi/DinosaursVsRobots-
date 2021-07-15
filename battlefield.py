from _typeshed import Self
from robot import Robots
from fleet import Fleet
from herd import Herd
import random
# attack function to be used in the battle
def dino_attacker (dino, robot):
    robot.hp -= dino.attack
    print (dino.attack)
    print(robot.hp)

# need this to pick who fights
def get_random_number(num_1, num_2):
    random_int = random_number(num_1, num_2)
    return random_int


def random_number(min_value, max_value):
    return random.randint(min_value, max_value)



# def robot_attacker(robot, dino):
#     statment asking what weapon you wanna Userwants 
#     doing the damage with that weapon to the dino
    
class Battle_Field:

    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()
# this is an intro to the big battle
    def start_of_it_all():
        print("WELCOME TOO DINSAURS VS ROBOTS!!!!!")
        print ("LETS GET THIS SHOW ON THE ROAD!")
            

    def battle(self):   
        dino_fighters = 3
        robo_fighters = 3
        
        while dino_fighters >= 0 and robo_fighters >= 0:
            d = get_random_number(0 , 2)
            while self.herd.herd[d].hp <= 0:
                d = get_random_number (0 , 2)

            r = get_random_number(0, 2)
            while self.fleet.fleet[r]:
                r = get_random_number(0, 2)




# set dino count down index to the len of Herd
# set robot^

# this will choose the first fighters 
# use lens to get the len to add more fighters and count down 
# while dino >=0 and robot >=0


# var = random roll to see who will atack 1-10 dino 11-10 Robots


# if var < 11 
#         do fino attack fun with inputs 

# if var >10 do robots 

# some type of reminders of how much hot ppoints are left for both 


#  do for robots and dino 2 ifs
# if has no hit points left 
# -1 from the list of fighters 
# and +1 to the fighter index 


# if dino reach 0 robots WindowsError

# if robts reach 0 don win
Battle_Field().battle()
