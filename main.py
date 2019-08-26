import numpy as np
import random as r
import sys

class MontyHall:
    def __init__(self):
        self.doors = (1, 2, 3)
        self.prize_door = r.randint(1, 3)
        self.goat_doors = [door for door in self.doors if door is not self.prize_door]
        self.first_choice = None
        self.goat_shown = r.choice(self.goat_doors)
        self.final_choice = None
        # print(f"You choose door {self.first_choice}")
        # print(f"Door {self.goat_shown} is shown. It's a goat! Do you want to keep your choice or change?")
    
    def make_first_choice(self):
        inp = input("Which door shall you choose? (1, 2, or 3)")
        self.first_choice = int(inp)

    def keep_choice(self):
        self.final_choice = self.first_choice        

    def change_choice(self):
        for door in self.doors:
            if door is not self.first_choice and door is not self.goat_shown:
                self.final_choice = door

    def did_win(self):
        if self.final_choice is self.prize_door:
            return True
        else:
            return False

    def sim_game(self, keep_or_not):
        self.first_choice = r.randint(1, 3)
        if keep_or_not:
            self.keep_choice()
        else:
            self.change_choice()
        if self.did_win():
            return True
        else:
            return False    



def simulation():
    mh = MontyHall()
    mh.sim_game(True)
    inp = input("How many iterations do you want to run?\n")
    iterations = int(inp)
    keep_choice_wins = 0
    change_choice_wins = 0
    for i in range(iterations):
        mh = MontyHall()
        if mh.sim_game(True) is True:
            keep_choice_wins += 1
        else:
            change_choice_wins += 1
    print(f"Keeping the first choice resulted in {keep_choice_wins} wins out of {iterations} games, or {keep_choice_wins / iterations * 100}% of the time")
    print(f"Changing the first choice resulted in {change_choice_wins} wins out of {iterations} games, or {change_choice_wins / iterations * 100}% of the time")


if __name__ == "__main__":
    print("Welcome! Would you like to play the game, or simulate the problem?\n")
    type = input("1. play\n2. sim\n\n")
    if type == "1":
        pass
    elif type == "2":
        simulation()
    else:
        print("not a valid choice.")

