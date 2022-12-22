import math

class Shape:
    """
    класс-интерфейс элемента
    """
    def accept(self, visitor):
        pass

    def get_name(self):
        pass


class Circle(Shape):
    """
    конкретный класс фигуры №1
    """
    radius = 0.0
    name = "Circle"

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def accept(self, visitor):
        visitor.visit_circle(self)

    def get_name(self):
        return self.name


class Square(Shape):
    """
    конкретный класс фигуры №2
    """
    length = 0.0
    name = "Square"

    def __init__(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def accept(self, visitor):
        visitor.visit_square(self)

    def get_name(self):
        return self.name


class Rectangle(Shape):
    """
    конкретный класс фигуры №3
    """
    length = 0.0
    width = 0.0
    name = "Rectangle"

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def accept(self, visitor):
        visitor.visit_rectangle(self)

    def get_name(self):
        return self.name


class ShapeVisitor:
    """
    класс-интерфейс посетителя
    """

    def visit_circle(self, circle):
        pass

    def visit_square(self, square):
        pass

    def visit_rectangle(self, rectangle):
        pass


class AreaVisitor(ShapeVisitor):
    """
    Конкретный класс посетителя для подсчёта площади фигур
    """
    area = 0.0

    def visit_circle(self, circle):
        self.area = math.pi * math.pow(circle.getRadius(), 2)

    def visit_square(self, square):
        self.area = 2 * square.getLength()

    def visit_rectangle(self, rectangle):
        self.area = rectangle.getLength() * rectangle.getWidth()

    def get(self):
        return self.area



class PerimeterVisitor(ShapeVisitor):
    """
    Конкретный класс посетителя для подсчёта периметра фигур
    """
    perimeter = 0.0
    def visit_circle(self, circle):
        self.perimeter = 2 * math.pi * circle.getRadius()
    def visit_square(self, square):
        self.perimeter = 4 * square.getLength()
    def visit_rectangle(self, rectangle):
        self.perimeter = 2 * (rectangle.getLength() + rectangle.getWidth())
    def  get(self):
        return self.perimeter


def main():
        shapes = []
        shapes.append(Circle(10))
        shapes.append(Square(10))
        shapes.append(Square(5))
        shapes.append(Rectangle(10, 2))

        areaVisitor = AreaVisitor()
        perimeterVisitor = PerimeterVisitor()

        for shape in shapes:
            shape.accept(areaVisitor)
            shape.accept(perimeterVisitor)
            area = areaVisitor.get()
            perimeter = perimeterVisitor.get()
            print("Area of %s: %.2f\n" % (shape.get_name(), area), end="", sep="")
            print("Perimeter of %s: %.2f\n" % (shape.get_name(), perimeter), end="", sep="")
            print("---------------------------------")


if __name__ == "__main__":
    main()