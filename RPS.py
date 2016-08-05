#rock paper scissor
import random


class rpsgame:

    rps= ["rock", "paper","scissors"]


    wincount=0
    losecount=0
    def usercycle(self):
        userchoice = input("rock, paper, scissor.....")
        print("SHOOT")
        return userchoice
   
    def gamecycle(self):
        computerchoice = random.choice(self.rps)
        print("Bot chooses {}".format(computerchoice))
        return computerchoice
            



    def decisioncycle(self):
            
            uc = self.usercycle()
            gc = self.gamecycle()
            
            if uc == self.rps[0] and gc == self.rps[1]:
                    print("paper beats rock, you lose!")
                    rpsgame.losecount +=1
            elif uc == self.rps[1] and gc == self.rps[0]:
                    print("paper beats rock, you win!")
                    rpsgame.wincount+=1
            elif uc == self.rps[0] and gc == self.rps[2]:
                    print("rock beats scissors, you win!")
                    rpsgame.wincount+=1
            elif uc == self.rps[2] and gc == self.rps[0]:
                    print("rock beats scissors, you lose!")
                    rpsgame.losecount+=1
            elif uc == self.rps[1] and gc == self.rps[2]:
                    print("scissors beats paper, you lose!")
                    rpsgame.losecount+=1
            elif uc == self.rps[2] and gc == self.rps[1]:
                    print("scissors beats paper, you win!")
                    rpsgame.wincount+=1
            elif uc == gc:
                    print("it's a tie!!!")
            print("wins {}, losses {}".format(rpsgame.wincount, rpsgame.losecount))
            
                
while True:

    game = rpsgame()
    game.decisioncycle()
        