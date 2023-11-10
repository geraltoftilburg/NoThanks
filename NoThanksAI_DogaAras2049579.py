from NoThanksPlayer import Player

#Student Name: Doga Aras 
#Student Number: 2049579
class MyAI(Player):
    def __init__(self):
        Player.__init__(self)
        self.setName('MyAI')

    def take(self, card, state):

        #Game Rule 
        #If a player does not have coins, they must take the card. 
        if self.coins <= 0:
            return True

        #Calculate Pentaly 
        penalty_with_card = self.penaltyWhenTake(card)

        #Strategies 

        #A player should take the card if the penalty is less than the current pentaly. 
        if penalty_with_card < self.penalty():
            return True

        #A player should take the card if it connects with any card in the collection. 
        for c in self.collection:
             if c.number == card.number - 1 or c.number == card.number + 1:
                 return True 
             
        #The player will take the card if it has 3 or more coins and its number is 20 or less. 
        if card.coins >= 3 and card.number <= 20:
            return True

        #THe player will not take the card if its number is greater than 30 and if the player has more than 5 coins. 
        if card.number > 30 and self.coins > 5:
            return False

        #A player will take the card if its number is 10 or less and it has at least 1 coin. 
        if card.number <= 10 and card.coins >= 1:
            return True

        #A player will not take the card if the minimum coins of other players is 2 or less. 
        if min(player.coins for player in state.players if player.name != self.name) <= 2:
            return False

        return False
