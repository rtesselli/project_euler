"""
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle
is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one
thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
"""

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def read_data():
    def build_triangle(line):
        values = list(map(int, line.split(',')))
        point_a = Point(*values[:2])
        point_b = Point(*values[2:4])
        point_c = Point(*values[4:])
        return point_a, point_b, point_c

    with open('./data/p102_triangles.txt', 'r') as f:
        lines = f.readlines()
    return [
        build_triangle(line)
        for line in lines
    ]


def determinant(point_a, point_b):
    return point_a.x * point_b.y - point_a.y * point_b.x


def contains_origin(triangle):
    point_a, point_b, point_c = triangle
    side1 = Point(point_b.x - point_a.x, point_b.y - point_a.y)
    check1 = Point(0 - point_a.x, 0 - point_a.y)
    side2 = Point(point_c.x - point_b.x, point_c.y - point_b.y)
    check2 = Point(0 - point_b.x, 0 - point_b.y)
    side3 = Point(point_a.x - point_c.x, point_a.y - point_c.y)
    check3 = Point(0 - point_c.x, 0 - point_c.y)
    return (determinant(side1, check1) < 0) == (determinant(side2, check2) < 0) == (determinant(side3, check3) < 0)


def problem102():
    triangles = read_data()
    return sum(contains_origin(triangle) for triangle in triangles)
