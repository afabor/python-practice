from room import Room

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

current_room = kitchen

while True:
    print('\n')
    current_room.get_details()
    command = input('>')
    current_room = current_room.move(command)

