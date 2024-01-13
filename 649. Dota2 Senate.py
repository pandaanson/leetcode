
"""
Question Rephrased (Dota2 Senate - Problem 649):
In the Dota2 world, there are two parties: Radiant ('R') and Dire ('D'). The Senate, composed of senators from these two parties, is voting on a game change. The voting is in rounds, where each senator has two options:
1. Ban a senator from the opposite party, removing their rights in this and future rounds.
2. Announce victory if all remaining senators are from their party.

Given a string 'senate' representing each senator's party, predict which party will win. The string contains 'R' and 'D' for Radiant and Dire senators. The process starts with the first senator and continues in order until one party wins.

Task: Implement a function to determine which party (Radiant or Dire) will win, assuming each senator plays the best strategy for their party.

Python Solution:
"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Queues to store the positions of Radiant and Dire senators
        radiant, dire = [], []
        
        # Fill the queues with the positions of the senators
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        n = len(senate)
        # Process the rounds until one party wins
        while radiant and dire:
            # Get the positions of the next Radiant and Dire senators
            r, d = radiant.pop(0), dire.pop(0)
            # If Radiant senator's position is earlier, they ban the Dire senator,
            # and the Radiant senator re-enters the queue for the next round.
            # Otherwise, the Dire senator does the same to the Radiant senator.
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        # Return the winning party
        return "Radiant" if radiant else "Dire"
