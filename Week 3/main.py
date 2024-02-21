from room import Room
from character import Enemy

kitchen = Room('Kitchen')
ballroom = Room('Ballroom')
dining_hall = Room('Dining Hall')

kitchen.set_description('A dank and dirty room buzzing with flies.')
kitchen.describe()

ballroom.set_description('A nicely lit room with a diamond chandalier')
ballroom.describe()

dining_hall.set_description('A lively area filled with lovely aroma')
dining_hall.describe()

kitchen.link_room(dining_hall, 'south')

dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')

ballroom.link_room(dining_hall, 'east')

dave = Enemy('Dave', 'A smelly zombie')
dave.set_conversation('....')
dave.set_weakness('apples')

dining_hall.set_character(dave)

current_room = kitchen


while True:
    print('\n')
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input('>')
    current_room = current_room.move(command)



