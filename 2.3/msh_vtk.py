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
    with open(filename) as fs:
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
                i1, i2 = int(myline[-2]), int(myline[-1])
                lines.append(line(i1, i2))
            elif element_type == 2:  # Triangle
                i1, i2, i3 = int(myline[-3]), int(myline[-2]), int(myline[-1])
                triangles.append(triangle(i1, i2, i3))

def write_vtk(points, lines, triangles, filename):
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
        file.write('SCALARS vertex_indices int 1\n')
        file.write('LOOKUP_TABLE default\n')
        for i in range(len(points)):
            file.write(f'{i}\n')  # Zero-based index

# Usage
points = []
triangles = []
lines = []
read_mesh("../2.1/custom1.msh", points, triangles, lines)
write_vtk(points, lines, triangles, "output.vtk")

