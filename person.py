# PURPOSE OF THIS IS TO SHOW THAT 'self' CAN BE ASSINGED TO ANY VALUE, AND DOESNT HAVE TO BE 'self' BUT IT IS BEST PRACTICE
class Person():
    def __init__(sillyObject, name, age):
        sillyObject.name = name
        sillyObject.age = age
    
    def myFunc(abc):
        print(f'Hello,  my name is {abc.name}')

p1 = Person('Amos', 29)
p1.myFunc()