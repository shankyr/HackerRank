import timeit

start = timeit.default_timer()


def read_input():
    global row
    global col
    global nodes
    row = int(raw_input().strip())
    col = int(raw_input().strip())

    for i in range(row):
        nodes.extend(map(int, raw_input().strip().split(' ')))


def connected_filled_cells(nodes):
    global row
    global col
    global cell_visited
    global cell_travel_path

    region = 1
    while len(cell_travel_path) != 0:
        cell = cell_travel_path.pop()

        if cell not in [e for e in range(0, len(nodes) - col + 1, col)]:

            try:
                if nodes[cell - col - 1] == 1:
                    c = cell - col - 1
                    if c not in cell_visited and c > 0:
                        cell_visited.add(c)
                        cell_travel_path.append(c)
                        region += 1
            except IndexError:
                pass

            try:
                if nodes[cell - 1] == 1:
                    c = cell - 1
                    if c not in cell_visited and c > 0:
                        cell_visited.add(c)
                        cell_travel_path.append(c)
                        region += 1
            except IndexError:
                pass

            try:
                if nodes[cell + col - 1] == 1:
                    c = cell + col - 1
                    if c not in cell_visited and c > 0:
                        cell_visited.add(c)
                        cell_travel_path.append(c)
                        region += 1
            except IndexError:
                pass

        if cell not in [e for e in range(-1, len(nodes), col)] or cell == 0:

            try:
                if nodes[cell - col + 1] == 1:
                    c = cell - col + 1
                    if c not in cell_visited and c > 0:
                        cell_visited.add(c)
                        cell_travel_path.append(c)
                        region += 1
            except IndexError:
                pass

            try:
                if nodes[cell + 1] == 1:
                    c = cell + 1
                    if c not in cell_visited and c > 0:
                        cell_visited.add(c)
                        cell_travel_path.append(c)
                        region += 1
            except IndexError:
                pass

            try:
                if nodes[cell + col + 1] == 1:
                    c = cell + col + 1
                    if c not in cell_visited and c > 0:
                        cell_visited.add(c)
                        cell_travel_path.append(c)
                        region += 1
            except IndexError:
                pass

        try:
            if nodes[cell + col] == 1:
                c = cell + col
                if c not in cell_visited and c > 0:
                    cell_visited.add(c)
                    cell_travel_path.append(c)
                    region += 1
        except IndexError:
            pass

        try:
            if nodes[cell - col] == 1:
                c = cell - col
                if c not in cell_visited and c > 0:
                    cell_visited.add(c)
                    cell_travel_path.append(c)
                    region += 1
        except IndexError:
            pass

    return region


row, col = 0, 0
nodes = []

read_input()
# print nodes

cell_visited = set([])
cell_travel_path = []
regions = []

for ind in range(len(nodes)):
    if ind not in cell_visited and nodes[ind] == 1:
        cell_visited.add(ind)
        cell_travel_path.append(ind)
        regions.append(connected_filled_cells(nodes))

print max(regions)

print timeit.default_timer() - start
