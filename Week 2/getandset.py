class Rectangle():
    def __init__(self,height, width):
        self.height = height
        self.width = width

    def get_height(self):
        print(f'Height is {self.height}')
        return self.height
        

    def get_width(self):
        print(f'Width is {self.width}')
        return self.width

    def set_height(self, height):
        self.height = height
        print(f'New Height Is: {self.height}')

    def set_width(self, width):
        self.width = width
        print(f'New Width Is: {self.width}')

    def rec_area(self):
        area = self.height * self.width
        print(f'Area of the rectangle is: {area}')

A = Rectangle(42, 35)
A.get_height()
A.get_width()
A.set_height(50)
A.set_width(45)
A.rec_area()