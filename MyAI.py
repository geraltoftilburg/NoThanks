from NoThanksPlayer import Player

class MyAI(Player):
    def __init__(self):
        Player.__init__(self)
        self.setName('MyAI')

    def take(self, card, state):
        if self.coins <= 0:
            return True

        penalty_with_card = self.penaltyWhenTake(card)

        if penalty_with_card < self.penalty():
            return True

        if any(c.number == card.number - 1 or c.number == card.number + 1 for c in self.collection):
            return True

        if card.coins >= 3 and card.number <= 20:
            return True

        if card.number > 30 and self.coins > 5:
            return False

        if card.number <= 10 and card.coins >= 1:
            return True

        if min(player.coins for player in state.players if player.name != self.name) <= 2:
            return False

        return False
