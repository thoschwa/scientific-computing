from matplotlib import pyplot as plt


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
            points.append(point(x,y))


        # TODO: discard two lines
        fs.readline()
        fs.readline()

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
            if type == 1:
                lines.append(line(int(myline[5]), int(myline[6])))
            elif type == 2:
                triangles.append(triangle(int(myline[5]), int(myline[6]), int(myline[7])))


points=[]
triangles=[]
lines=[]
read_mesh("custom1.msh", points, triangles, lines)

# TODO: plot the triangles, lines, and points
# plot the triangles
for i in range(len(triangles)):
    x1 = points[triangles[i].i1-1].x
    y1 = points[triangles[i].i1-1].y
    x2 = points[triangles[i].i2-1].x
    y2 = points[triangles[i].i2-1].y
    x3 = points[triangles[i].i3-1].x
    y3 = points[triangles[i].i3-1].y
    plt.plot([x1,x2,x3,x1], [y1,y2,y3,y1], 'b')

# plot the lines

for i in range(len(lines)):
    x1 = points[lines[i].i1-1].x
    y1 = points[lines[i].i1-1].y
    x2 = points[lines[i].i2-1].x
    y2 = points[lines[i].i2-1].y
    plt.plot([x1,x2], [y1,y2], 'r')

# plot the points
for i in range(len(points)):
    plt.plot(points[i].x, points[i].y, 'ro')

plt.show()
