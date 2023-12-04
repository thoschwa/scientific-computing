from numpy import *

class point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class line:
    def __init__(self, _i1, _i2):
        self.i1 = _i1
        self.i2 = _i2


class triangle:
    def __init__(self, _i1, _i2, _i3):
        self.i1 = _i1
        self.i2 = _i2
        self.i3 = _i3


def read_mesh(filename, points, triangles, lines):
    # TODO
    pass


def triangle_has_vertex(tr, i):
    # return true if the triangle contains the vertex i
    return False

def area_triangle(p1, p2, p3):
    # TODO: return the area of the triangle defined by the points p1, p2, p3
    return 1.0

def area_triangles(points, triangles):
    # TODO: return a list that contains the area of all triangles
    return []

def compute_bc(i, t, points, b, c):
    if i == t.i1:
        p1 = points[t.i1]
        p2 = points[t.i2]
        p3 = points[t.i3]
    elif i == t.i2:
        p1 = points[t.i2]
        p2 = points[t.i1]
        p3 = points[t.i3]
    elif i == t.i3:
        p1 = points[t.i3]
        p2 = points[t.i1]
        p3 = points[t.i2]
    else:
        print("Error: vertex i is not part of triangle t")
        exit(1)
    
    # TODO: compute the coefficients b and c (i.e. b_{ik} and c_{ik}) form the lecture.
    # The code above makes sure that p1 always corresponds to vertex i.


def on_boundary(i, lines):
    # TODO: retun true if the vertex with index i is a boundary point, false otherwise.
    return False


def assemble_matrix(points, triangles, lines):
    n_v = len(points)
    n_T = len(triangles)

    B = zeros(n_v, n_v)

    # TODO: assemble the matrix using the functions defined above.

    return B



points = []
triangles = []
lines = []
read_mesh("test.msh", points, triangles, lines)

# TODO: assemble the matrix and solve the equation
