import numpy


class point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class line:
    def __init__(self, _i1, _i2, _tag, _point1, _point2):
        self.i1 = _i1
        self.i2 = _i2
        self.tag = _tag
        self.point1 = _point1
        self.point2 = _point2


class triangle:
    def __init__(self, _i1, _i2, _i3):
        self.i1 = _i1
        self.i2 = _i2
        self.i3 = _i3


def read_mesh(filename, points, triangles, lines):
    with open(filename) as fs:
        while (fs.readline() != "$Nodes\n"):
            pass

        num_nodes = int(fs.readline())
        for i in range(num_nodes):
            myline = fs.readline().split()
            x = float(myline[1])
            y = float(myline[2])
            points.append(point(x, y))

        # Skipping two lines before reading elements
        fs.readline()
        fs.readline()

        num_elements = int(fs.readline())

        for i in range(num_elements):
            myline = fs.readline().split()
            element_type = int(myline[1])

            if element_type == 1:  # Line
                i1, i2, tag, point1, point2 = int(
                    myline[-2]), int(myline[-1]), int(myline[3]), int(myline[-2]), int(myline[-1])
                lines.append(line(i1, i2, tag, point1, point2))
            elif element_type == 2:  # Triangle
                i1, i2, i3 = int(myline[-3]), int(myline[-2]), int(myline[-1])
                triangles.append(triangle(i1, i2, i3))


def triangle_has_vertex(tr, i, points):
    return points[i] in [points[tr.i1 - 1], points[tr.i2 - 1], points[tr.i3 - 1]]


def area_triangle(p1, p2, p3):
    return 0.5 * abs(p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y))


def area_triangles(points, triangles):
    areas = []
    for t in triangles:
        p1, p2, p3 = points[t.i1], points[t.i2], points[t.i3]
        areas.append(area_triangle(p1, p2, p3))
    return areas


def compute_bc(i, t, points):
    if i == (t.i1 - 1):
        p1 = points[t.i1 - 1]
        p2 = points[t.i2 - 1]
        p3 = points[t.i3 - 1]
    elif i == (t.i2 - 1):
        p1 = points[t.i2 - 1]
        p2 = points[t.i1 - 1]
        p3 = points[t.i3 - 1]
    elif i == (t.i3 - 1):
        p1 = points[t.i3 - 1]
        p2 = points[t.i1 - 1]
        p3 = points[t.i2 - 1]
    else:
        print("Error: vertex i is not part of triangle t")
        exit(1)

    matrix = numpy.array([[1, p1.x, p1.y], [1, p2.x, p2.y], [1, p3.x, p3.y]])

    s = numpy.array([1, 0, 0])

    coefficients = numpy.linalg.solve(matrix, s)

    b = coefficients[1]
    c = coefficients[2]

    return b, c


def on_boundary(i, lines, points):
    for line in lines:
        if i in [points[line.i1 - 1], points[line.i2 - 1]]:
            return True
    return False


def assemble_matrix(points, triangles, lines):
    n_v = len(points)
    n_T = len(triangles)

    B = numpy.zeros((n_v, n_v))

    for i in range(n_v):
        H = 0  # area of adjacent triangles for i
        # Iterate over all triangles
        for k in range(n_T):
            # Check if the triangle includes vertex i
            if triangle_has_vertex(triangles[k], i, points):
                H += area_triangle(points[triangles[k].i1 - 1],
                                   points[triangles[k].i2 - 1], 
                                   points[triangles[k].i3 - 1])

        # Check if vertex is not on the boundary
        if not on_boundary(i, lines, points):
            for j in range(n_v):
                # Iterate over all triangles
                for k in range(n_T):
                    # Check if the triangle includes vertices i and j
                    if triangle_has_vertex(triangles[k], i, points) and triangle_has_vertex(triangles[k], j, points):
                        # Compute contributions to the matrix B
                        b_ik, c_ik = compute_bc(
                            i, triangles[k], points)
                        b_jk, c_jk = compute_bc(
                            i, triangles[k], points)
                        B[i][j] -= area_triangle(points[triangles[k].i1 - 1], points[triangles[k].i2 - 1], points[triangles[k].i3 - 1]) * (b_ik * b_jk + c_ik * c_jk)

                B[i][j] /= H

    return B


def write_vtk(points, lines, triangles, filename, values):
    with open(filename, 'w') as file:
        file.write('# vtk DataFile Version 3.0\n')
        file.write('Mesh data with polygons\n')
        file.write('ASCII\n')
        file.write('DATASET POLYDATA\n')
        file.write(f'POINTS {len(points)} float\n')

        for point in points:
            file.write(f'{point.x} {point.y} 0\n')  # Assuming z = 0 for 2D points

        # Writing lines as VTK_POLY_LINE
        total_line_indices = sum([2 for line in lines])  # 2 points per line
        file.write(f'LINES {len(lines)} {total_line_indices + len(lines)}\n')
        for line in lines:
            file.write(f'2 {line.i1 - 1} {line.i2 - 1}\n')  # Adjusting to zero-based index

        # Writing triangles as polygons
        total_triangle_indices = sum([3 for triangle in triangles])  # 3 points per triangle
        file.write(f'POLYGONS {len(triangles)} {total_triangle_indices + len(triangles)}\n')
        for triangle in triangles:
            file.write(f'3 {triangle.i1 - 1} {triangle.i2 - 1} {triangle.i3 - 1}\n')  # Adjusting to zero-based index

        # Writing point data
        file.write('POINT_DATA {}\n'.format(len(points)))
        file.write('SCALARS value double 1\n')
        file.write('LOOKUP_TABLE default\n')
        
        for i in range(len(values)):
            file.write(f'{values[i]}\n')  # Zero-based index


points = []
triangles = []
lines = []
read_mesh("../2.1/simple.msh", points, triangles, lines)

B = assemble_matrix(points, triangles, lines)

# Set simulation parameters
delta_t = 0.01
num_steps = 100

# Run explicit Euler simulation
current_temperature = numpy.zeros(len(points))
next_temperature = numpy.zeros(len(points))

current_temperature[(len(points) + 5) - len(points)] = 1
current_temperature[len(points) - 1] = 1

for i in range(num_steps):
    next_temperature = current_temperature + \
        delta_t * numpy.dot(B, current_temperature)

    current_temperature = next_temperature.copy()

# Write results to VTK file
write_vtk(points, lines, triangles, "output.vtk", current_temperature)
