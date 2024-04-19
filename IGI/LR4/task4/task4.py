import math
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Color:
    def __init__(self):
        self._color = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @color.deleter
    def color(self):
        del self._color


class Triangle(Figure):
    def __init__(self, height, base, color, name):
        self._h = height
        self._a = base
        self.c = Color
        self.c.color = color
        self.name = name

    def area(self):
        super().area()
        return int(1 / 2 * self._a * self._h)

    def get_info(self):
        name = self.name
        area = self.area()
        color = self.c.color
        print("Figure: {}\nColor: {}\nArea: {}".format(name, color, area))

    def plot(self):
        x = [1, 1+self._a, 1 + self._a/2,1]
        y = [1, 1, 1+self._h,1]
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.fill(x, y, color=self.c.color, alpha=0.8)
        ax.set_aspect("equal")
        ax.set_title(self.name)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        plt.savefig("task4/triangle.png")

        plt.show()


def task4_run():
    polygon = Triangle(1, 2, "Grey", "Triangle")
    polygon.plot()
