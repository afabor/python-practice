from character import Enemy

dave = Enemy('Dave', 'A dirty zombie')
dave.describe()
dave.set_conversation('Hello, what are you going here?')
dave.talk()
dave.set_weakness('cheese')

print('What will you fight with?')
fight_with = input()
dave.fight(fight_with)