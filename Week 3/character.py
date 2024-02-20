class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.desctription = char_description
        self.conversation = None


    def describe(self):
        print(f'{self.name} is here')
        print(self.desctription)
        
    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f'{self.name} says {self.conversation}')
        else:
            print(f'{self.name} does not want to talk to you.')

    def fight(self, combat_item):
        print(f'{self.name} does not want to fight with you')
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
    
