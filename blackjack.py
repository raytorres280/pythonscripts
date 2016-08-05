import random
import time

class blackjack:

    ace = 1 #use try statement at hitorstay calculations, to determine if you want it 1 or 11 somehow
    deck = list(range(1, 11)) * 4
    deck = deck + [ace, ace, ace, ace]
    wincount = 0
    losecount = 0
    



    def drawCards(self):
        popper = self.deck
        hum_down_card = popper.pop(random.choice(popper))
        hum_up_card = popper.pop(random.choice(popper))
        print("your cards are {} and {}".format(hum_up_card, hum_down_card))
        return (hum_down_card, hum_up_card)

    def compDraw(self):
        popper = self.deck
        comp_down_card = popper.pop(random.choice(popper))
        comp_up_card = popper.pop(random.choice(popper))
        print("the comp's face up card is {}".format(comp_up_card))
        return (comp_down_card, comp_up_card)

                
        
    def hitorstay(self):
        popper = self.deck
        hdown, hup = self.drawCards()
        totalhand = [hup, hdown]
        while sum(totalhand) < 21:
            makemove = input("type HIT or STAY\n")
            if makemove == 'HIT':
                nextcard = popper.pop(random.choice(popper))
                totalhand = totalhand + [nextcard]
                print("your hand is{}".format(totalhand))
                continue
            elif makemove == 'STAY':
                break
         #if sum(totalhand) > 21:
         #make them bust right here and up the loss count somehow before the computer gets to go.
        print("your hand is{}".format(totalhand))
        return totalhand
        #somehow stop the game here if you bust right away, before comparing so the comp doesnt take its turn
        
       
        
    
    def comphitorstay(self):
        popper = self.deck
        cdown, cup = self.compDraw()
    #if you want comp to know users hand, call hitorstay  here for return value.
        userhand = self.hitorstay()
        comphand = [cdown, cup]
        while sum(comphand) < 21: #either 18 or give it access to player hand total value and try to make it win?
            if sum(comphand) < sum(userhand):
                drawcard = popper.pop(random.choice(popper))
                print("the computer drew a {}".format(drawcard))
                comphand =comphand + [drawcard]
                continue
            elif sum(comphand) > sum(userhand):
                break
            
        print("the computer has finished its moves")
        print("the computer's face up cards are {}".format(comphand))
        return (userhand, comphand)
            
        
    
    
    def chooseWinner(self):
    
       
        finaluserhand, finalcomphand = self.comphitorstay()
        if sum(finaluserhand) > 21:
            print("that's a bust, you lose!!!")
            self.losecount += 1
        elif sum(finalcomphand) > 21:
            print("computer busts!! you win!")
            self.wincount += 1
        elif sum(finaluserhand) < sum(finalcomphand):
            print("computer has {}, you have{}, YOU LOSE".format(sum(finalcomphand),sum(finaluserhand)))
            self.losecount += 1
        elif sum(finaluserhand) > sum(finalcomphand):
            print("computer has {}, you have{}, YOU WIN".format(sum(finalcomphand),sum(finaluserhand)))
            self.wincount += 1
        else:
            print("ITS A DRAW")
        print("wins {}, losses {}".format(self.wincount, self.losecount))
        
 #use an odd and even adding algorthim, implement to take turns of comp or user going first. to make it interesting
print("Welcome to Blackjack 1.0.")
game = blackjack()
while True:
    game.chooseWinner()
        
#later make comp hit smarter,, based on what's in the list - totalhand - minus the down card.
#also random.choices might repeat cards more than 4 times, not realistic, maybe replace with 
#self.deck = popper
#popper.pop(random.choice(popper)) ??