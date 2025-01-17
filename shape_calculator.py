class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, value):
        self.width = value
    
    def set_height(self, value):
        self.height = value

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            return (('*' * self.width + '\n') * self.height)
        else:
            return "Too big for picture."
    
    def get_amount_inside(self, smallShape):
        return (self.width // smallShape.width) * (self.height // smallShape.height)
        

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})" 




class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side        

    def set_side(self, value):
        self.width = value
        self.height = value  

    def __str__(self):
        return f"Square(side={self.width})"



