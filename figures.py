from flask import Flask, request, abort

class Figure:
    def __init__(self) -> None:
        pass


class Square(Figure):
    def __init__(self,side):
        self.side = side

    def get_area(self):
        if self.side is None:
            return 'Incorrect arguments', 400 
        area = self.side ** 2
        return area


class Triangle(Figure):
    def __init__(self,basis,height):
        self.basis = basis
        self.height = height

    def get_area(self):
        if self.basis is None or self.height is None:
            return 'Incorrect arguments', 400
        area = self.height * self.height
        return area
    
class Rectangle(Figure):
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def get_area(self):
        if self.width is None or self.length is None:
            return 'Incorrect arguments', 400        
        area = self.width * self.length
        return area
    
            
