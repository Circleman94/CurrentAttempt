import itertools
import matplotlib.pyplot as plt
import gamblingClass

# The user-defined DIE will be rolled, players will record a NUMBER_OF_CHOICES long sequence of outcomes.
# Whoever has their sequence appears fist wins and gets a point.
# Loser gets -1 and a tie is 0. Each player will face each other
# NUMBER_OF_GAMES times.

NUMBER_OF_GAMES = 100
NUMBER_OF_CHOICES = 2
DIE = ('A', 'B', 'C', 'D', 'E', 'F')
players = [gamblingClass.Gambler(pick, DIE) for pick in itertools.product(DIE, repeat=NUMBER_OF_CHOICES)]

for player in players:
    for player2 in players:
        for gameRound in range(NUMBER_OF_GAMES):
            player.battle(player2)


for player in players:
    player.printWinPercentages(NUMBER_OF_GAMES)


for p in players:
    p.plotPlayerRecords()

plt.show()