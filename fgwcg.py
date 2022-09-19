from dataclasses import dataclass
import sys

@dataclass
class Game:
    locations:tuple = ('Farmer', 'Goat', 'Wolf', 'Cabbage')
    farmerLoc:str = 'L'
    goatLoc:str = 'L'
    wolfLoc:str = 'L'
    cabbageLoc:str = 'L'
    initial:tuple = ('L', 'L', 'L', 'L')
    endgame:tuple = ('R', 'R', 'R', 'R')
    score:int = 0

    def currentStatus(self):
        print("\nCurrent Locations for Farmer, Goat, Wolf, Cabbage")
        self.current = (self.farmerLoc, self.goatLoc, self.wolfLoc, self.cabbageLoc)
        print(self.current)

    def checkStatus(self):
        if self.goatLoc == self.wolfLoc and (self.farmerLoc != self.wolfLoc or self.farmerLoc != self.goatLoc):
            print("Wolf ate Goat!")
            print("Game over!")
            print(f"Your score is {self.score}")
            sys.exit()

        if self.goatLoc == self.cabbageLoc and (self.farmerLoc != self.goatLoc or self.farmerLoc != self.cabbageLoc):
            print("Goat ate Cabbage!")
            print("Game over!")
            print(f"Your score is {self.score}")
            sys.exit()

    def promptActions(self):
        print("What do you wanna take now?")
        action = input("None\nGoat\nWolf\nCabbage\n(Or type 'exit' to quit)\nI take: ")
        action = action.lower()
        if action == "none": self.takeNone()
        elif action == "goat": self.takeGoat()
        elif action == "wolf": self.takeWolf()
        elif action == "cabbage": self.takeCabbage()
        elif action == "exit": sys.exit()
        else:
            print(f"{action} is not a valid action")
            self.promptActions()

    def takeNone(self):
        if self.farmerLoc == 'L':
            self.farmerLoc = 'R'
        if self.farmerLoc == 'R':
            self.farmerLoc = 'L'
        return self.farmerLoc

    def takeGoat(self):
        if self.goatLoc == 'L' and self.farmerLoc == 'L':
            self.goatLoc = 'R'
            self.farmerLoc = 'R'
        elif self.goatLoc == 'R' and self.farmerLoc == 'R':
            self.goatLoc = 'L'
            self.farmerLoc = 'L'
        else:
            print("Unable to take Goat. Farmer and Goat are on different sides of the bank.")

    def takeWolf(self):
        if self.wolfLoc == 'L' and self.farmerLoc == 'L':
            self.wolfLoc = 'R'
            self.farmerLoc = 'R'
        elif self.wolfLoc == 'R' and self.farmerLoc == 'R':
            self.wolfLoc = 'L'
            self.farmerLoc = 'L'
        else:
            print("Unable to take Wolf. Farmer and Wolf are on different sides of the bank.")

    def takeCabbage(self):
        if self.cabbageLoc == 'L' and self.farmerLoc == 'L':
            self.cabbageLoc = 'R'
            self.farmerLoc = 'R'
        elif self.cabbageLoc == 'R' and self.farmerLoc == 'R':
            self.cabbageLoc = 'L'
            self.farmerLoc = 'L'
        else:
            print("Unable to take Cabbage. Farmer and Cabbage are on different sides of the bank.")
        
    def play(self):
        self.current = (self.farmerLoc, self.goatLoc, self.wolfLoc, self.cabbageLoc)
        while (self.farmerLoc, self.goatLoc, self.wolfLoc, self.cabbageLoc) != self.endgame:
            self.currentStatus()
            self.checkStatus()
            self.promptActions()
            self.score += 1
        print("Congratulations! You got everyone on the other side of the river bank!")
        print(f"Your score is {self.score}")

if __name__ == '__main__':
    g = Game()
    g.play()
