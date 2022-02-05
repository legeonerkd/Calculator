import abc


class Figure(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def get_area(self):
        pass

class Square(Figure):
    def __init__(self,side):
        self.side = side

    def get_area(self):
        return self.side ** 2


class Triangle(Figure):
    def __init__(self,basis,height):
        self.basis = basis
        self.height = height

    def get_area(self):
        return (self.height * self.height) / 2
    
class Rectangle(Figure):
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def get_area(self):       
        return self.width * self.length
    
            
