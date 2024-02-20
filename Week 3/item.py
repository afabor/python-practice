class Sword():
    def __init__(self, name):
        self.name = name
        self.attack = None
        self.magic = None
        
    def get_attack(self):
        return self.attack

    def set_attack(self, new_attack):
        self.attack = new_attack

    def get_magic(self):
        return self.magic

    def set_magic(self, new_magic):
        self.magic = new_magic

    def describe(self):
        print(f'This sword is {self.name} with the attacking power of {self.attack} and magical ability of {self.magic}')
    