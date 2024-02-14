import random as r

# USING Random, create a program that roll dice.
# If dice rolls 6, print 'Congrats, move two spaces'
# If dice does not roll 6, print 'Try Again'


dice_roll = r.randint(1,6)

if dice_roll == 6:
        print('Congrats, Move Two Spaces')
else:
        print('Try Again')

