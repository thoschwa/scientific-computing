import numpy

class point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class line:
    def __init__(self, _i1, _i2, _tag):
        self.i1 = _i1
        self.i2 = _i2
        self.tag = _tag


class triangle:
    def __init__(self, _i1, _i2, _i3):
        self.i1 = _i1
        self.i2 = _i2
        self.i3 = _i3


def read_mesh(filename, points, triangles, lines):
    with open(filename) as fs:
        while(fs.readline() != '$PhysicalNames\n'):
            pass
        
        number_of_boundaries = int(fs.readline())
        
        
        while(fs.readline() != "$Nodes\n"):
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
                i1, i2, tag = int(myline[-2]), int(myline[-1]), int(myline[3])
                lines.append(line(i1, i2, tag))
            elif element_type == 2:  # Triangle
                i1, i2, i3 = int(myline[-3]), int(myline[-2]), int(myline[-1])
                triangles.append(triangle(i1, i2, i3))


def triangle_has_vertex(tr, i):
    return i in [tr.i1, tr.i2, tr.i3]

def area_triangle(p1, p2, p3):
    return 0.5 * abs(p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y))

def area_triangles(points, triangles):
    areas = []
    for t in triangles:
        p1, p2, p3 = points[t.i1], points[t.i2], points[t.i3]
        areas.append(area_triangle(p1, p2, p3))
    return areas

def compute_bc(i, t, points):
    if i == points[t.i1 - 1]:
        p1 = points[t.i1 - 1]
        p2 = points[t.i2 - 1]
        p3 = points[t.i3 - 1]
    elif i == points[t.i2 - 1]:
        p1 = points[t.i2 - 1]
        p2 = points[t.i1 - 1]
        p3 = points[t.i3 - 1]
    elif i == points[t.i3 - 1]:
        p1 = points[t.i3 - 1]
        p2 = points[t.i1 - 1]
        p3 = points[t.i2 - 1]
    else:
        print("Error: vertex i is not part of triangle t")
        exit(1)
    
    matrix = numpy.array([[1, p1.x, p1.y], [1, p2.x, p2.y], [1, p3.x, p3.y]])

    solution = numpy.array([1, 0, 0])

    coeff = numpy.linalg.solve(matrix, solution)

    b = coeff[1]
    c = coeff[2]

    return b, c


def on_boundary(i, lines):
    if lines[i].tag in [1, 6]:
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
            if triangle_has_vertex(triangles[k], i):
                H += area_triangle(points[triangles[k].i1], points[triangles[k].i2], points[triangles[k].i3])

        # Check if vertex is not on the boundary
        if not on_boundary(i, lines):
            for j in range(n_v):
                # Iterate over all triangles
                for k in range(n_T):
                    # Check if the triangle includes vertices i and j
                    if triangle_has_vertex(triangles[k], i) and triangle_has_vertex(triangles[k], j):
                        # Compute contributions to the matrix B
                        b_ik, c_ik = compute_bc(points[i], triangles[k], points)
                        b_jk, c_jk = compute_bc(points[j], triangles[k], points)
                        B[i, j] -= (area_triangle(points[triangles[k].i1], points[triangles[k].i2], points[triangles[k].i3])
                                    / H) * (b_ik * b_jk + c_ik * c_jk)
                        
            B[i][j] /= H

    return B

def write_vtk(filename, points, triangles, temperatures):
    with open(filename, 'w') as file:
        file.write("# vtk DataFile Version 3.0\n")
        file.write("Temperature Field\n")
        file.write("ASCII\n")
        file.write("DATASET UNSTRUCTURED_GRID\n")
        file.write(f"POINTS {len(points)} float\n")

        for point in points:
            file.write(f"{point.x} {point.y} 0.0\n")

        file.write(f"CELLS {len(triangles)} {4 * len(triangles)}\n")

        for triangle in triangles:
            file.write(f"3 {triangle.i1-1} {triangle.i2-1} {triangle.i3-1}\n")

        file.write(f"CELL_TYPES {len(triangles)}\n")

        for _ in triangles:
            file.write("5\n")  # VTK_TRIANGLE

        file.write(f"POINT_DATA {len(points)}\n")
        file.write("SCALARS Temperature float 1\n")
        file.write("LOOKUP_TABLE default\n")

        for temperature in temperatures:
            file.write(f"{temperature}\n")



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

for _ in range(num_steps):
    for t in triangles:
        for i in [t.i1, t.i2, t.i3]:
            next_temperature[i-1] = current_temperature[i-1] + delta_t * B[i-1, i-1] * current_temperature[i-1]

    current_temperature = next_temperature.copy()

# Write results to VTK file
write_vtk("output.vtk", points, triangles, current_temperature)