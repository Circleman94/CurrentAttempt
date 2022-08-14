import random, itertools
import matplotlib.pyplot as plt


class Gambler:
    """Generates a possible player combination that can battle with others and graph"""

    # Class variables that never change between objects
    WIN = 1
    TIE = 0
    LOSS = -1

    def __init__(self, selection, DIE):
        '''Builds player with a 0 filled vs log. And converts their selection into a list'''
        self.playerSelection = [char for char in selection]
        self.die = DIE
        self.selectionSize = len(selection)
        self.vsLog = {key:0 for key in itertools.product(self.die, repeat=self.selectionSize)}


    def printWinPercentages(self, numberofGames):
        '''Doesn't actually show percentages. To be done later.
        Prints the win percentages for each head-to-head'''
        print(f"Main Player: {self.playerSelection}", end='\t\t')
        for player in self.vsLog:
            print(f"{(self.vsLog[player] / numberofGames):>10}", end='\t\t\t')
        print()

    def updateVsLog(self, opponent, result):
        '''After a battle, this method is called to update a players log book'''
        # I convert to a tuple because all dict keys must be immutable
        self.vsLog[tuple(opponent)] += result

    def battle(self, player2):
        '''One player battles another, it does not matter which player calls this method.'''
        # The game log begins with an initial number of rolls to be able to check
        GameLog = [random.choice(self.die) for x in range(self.selectionSize)]
        Winner = 0
        while Winner == 0:
            # Look at the latest three rolls to compare to the players
            latestThreeRolls = GameLog[-self.selectionSize:]
            if latestThreeRolls == list(self.playerSelection) and latestThreeRolls == list(player2.playerSelection):
                break
            elif latestThreeRolls == list(self.playerSelection):
                Winner = 1
            elif latestThreeRolls == list(player2.playerSelection):
                Winner = -1
            else:
                # No one wins so we roll another die
                GameLog.append(random.choice(self.die))
        self.updateVsLog(player2.playerSelection, Winner)
        # I multiply by negative 1 to give the opposite result to the other player
        player2.updateVsLog(self.playerSelection, Winner * -1)

    def plotPlayerRecords(self):
        '''Plots the records for an individual player'''

        #Sorts the dictionary into a list by the keys, aka the player selection
        points = sorted(self.vsLog.items())
        #Converting into points that pyplot can plot
        x, y = zip(*points)
        x = [i for i in range(1, len(x) + 1)]
        plt.plot(x, y)
        #Uncomment below to make it plot the specific graph
        #plt.show()

