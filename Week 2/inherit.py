class Employee():
    def __init__(self, name, id, gender):
        self.name = name
        self.id = id
        self.gender = gender
    
    def showDetails(self):
        print(f'Employee Name: {self.name} \nEmployee ID: {self.id} \nEmployee Gender: {self.gender}')

class Programmer(Employee):
    def __init__(self, name, id, gender, language):
        super().__init__(name, id, gender)
        self.language = language

    def showDetails(self):
        super().showDetails()
        print(f'Programming Language:{self.language}')

Dominic = Programmer('Dominic', 49838, 'Male', 'Python')
Dominic.showDetails()
Amanda = Employee('Amanda', 49838, 'Female')
Amanda.showDetails()