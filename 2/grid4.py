def get_all_dot_positions(xsize, ysize):
    return [(x,y) for x in range(0, xsize) for y in range(0, ysize)] #range should be from 1 to xsize-1

def create_grid_string(dots, xsize, ysize):
    grid = ""
    for y in range(ysize):
        for x in range(xsize):
            grid += "." if (x, y) in dots else "#"
        grid += "\n"
    return grid

positions = get_all_dot_positions(5, 5)
print(create_grid_string(positions, 5, 5))
