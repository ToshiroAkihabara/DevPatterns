from math import cos, sin


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"x: {self.a}, y: {self.b}"

    @staticmethod
    def cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":
    point = Point(5, 6)
    point_2 = Point.polar_point(2, 9)
    print(point, point_2)
