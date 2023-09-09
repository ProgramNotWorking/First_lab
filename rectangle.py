class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.__coordinates = {
            'x1': int(x1),
            'y1': int(y1),
            'x2': int(x2),
            'y2': int(y2)
        }

    def find_sides_size(self, find_perimeter, find_area):
        y_side = abs(self.__coordinates.get('y1') - self.__coordinates.get('y2'))
        x_side = abs(self.__coordinates.get('x1') - self.__coordinates.get('x2'))

        find_perimeter(y_side, x_side)
        find_area(y_side, x_side)