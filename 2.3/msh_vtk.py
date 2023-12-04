def read_msh(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    vertices = []
    for line in lines:
        if line.startswith('$Nodes'):
            num_nodes = int(next(file).strip())
            for _ in range(num_nodes):
                _, x, y, z = next(file).strip().split()
                vertices.append((float(x), float(y), float(z)))
            break

    return vertices

def write_vtk(vertices, output_filename):
    with open(output_filename, 'w') as file:
        file.write('# vtk DataFile Version 3.0\n')
        file.write('Converted from .msh\n')
        file.write('ASCII\n')
        file.write('DATASET POLYDATA\n')
        file.write(f'POINTS {len(vertices)} float\n')
        for vertex in vertices:
            file.write(f'{vertex[0]} {vertex[1]} {vertex[2]}\n')
        file.write('POINT_DATA {}\n'.format(len(vertices)))
        file.write('SCALARS vertex_indices int 1\n')
        file.write('LOOKUP_TABLE default\n')
        for i in range(len(vertices)):
            file.write(f'{i}\n')

# Usage
msh_filename = 'input.msh'  # Replace with your .msh file path
vtk_filename = 'output.vtk' # Replace with your desired output file path

vertices = read_msh(msh_filename)
write_vtk(vertices, vtk_filename)

