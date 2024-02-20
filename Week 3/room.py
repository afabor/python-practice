class Room():
    def __init__(self, room_name):
        self.name = room_name 
        self.description = None
        self.linked_rooms = {}
# GETTERS AND SETTERS
    def get_description(self):
        return self.description

    def set_description(self, new_desc):
        self.description = new_desc 

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name
    
    def describe(self):
        print(self.description)
# LINKING ROOMS
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
# GET THE CURRENT ROOM DETAILS

    def get_details(self):
        print(self.name)
        print('')
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f'The {room.get_name()} {direction}')

# METHOD TO MOVE ROOM 
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else: 
            print('You cannot go that way')
            return self

    