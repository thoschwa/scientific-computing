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

a = line(1,2)


def read_mesh(filename, points, triangles, lines):
    with open(filename) as fs:
        while(fs.readline() != "$Nodes\n"):
            pass

        num_nodes = int(fs.readline())

        for i in range(num_nodes):
            myline = fs.readline().split()
            x = float(myline[1])
            y = float(myline[2])
            print(x, y)

            # TODO: read data and populate the vector

        # TODO: discard two lines

        num_elements = int(fs.readline())
        print('num_elements = ', num_elements)

        print("Read element of type ", end="")
        for i in range(num_elements):
            myline = fs.readline().split()
            id = int(myline[0])
            type = int(myline[1])

            print(type, end=" ")

            # TODO: check the type (either 1 for line or 2 for triangle)
            # populate the lists lines and triangles


points=[]
triangles=[]
lines=[]
read_mesh("simple.msh", points, triangles, lines)

# TODO: plot the triangles, lines, and points
