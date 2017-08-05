# all tests passed


def palindrome_max_length(arr):
    arr_len = len(arr)

    lengths = [[0 for x in range(arr_len)] for x in range(arr_len)]

    for i in range(arr_len):
        lengths[i][i] = 1

    for c in range(2, arr_len + 1):
        for i in range(arr_len - c + 1):
            j = i + c - 1
            if arr[i] == arr[j] and c == 2:
                lengths[i][j] = 2
            elif arr[i] == arr[j]:
                lengths[i][j] = lengths[i + 1][j - 1] + 2
            else:
                lengths[i][j] = max(lengths[i][j - 1], lengths[i + 1][j])

    return lengths[0][arr_len - 1]


def dfs_undirected(e, s):
    # a list to keep track of the vertices visited applying DFS
    dfs_order = []

    # a list to keep track of all visited vertices to ensure
    # we don't process DFS for already visited vertex
    ver_visited = set([])

    # a STACK data structure to pick elements to apply DFS
    ver_traverse_stack = []

    # initializing with starting vertex
    ver_visited.add(s)
    ver_traverse_stack.append(s)

    while len(ver_traverse_stack) != 0:

        ver_picked = ver_traverse_stack.pop()
        dfs_order.append(ver_picked)

        try:
            vertices = e[ver_picked]
        except KeyError:
            continue

        for vertex in vertices:
            if vertex not in ver_visited:
                ver_visited.add(vertex)
                ver_traverse_stack.append(vertex)

    return dfs_order

# PROGRAM BEGINS HERE
n, k, m = map(int, raw_input().strip().split(' '))

transformations_dict = {}

for i in xrange(k):
    x, y = map(int, raw_input().strip().split(' '))

    try:
        transformations_dict[x].append(y)
    except KeyError:
        transformations_dict[x] = [y]

    try:
        transformations_dict[y].append(x)
    except KeyError:
        transformations_dict[y] = [x]

    # print transformations_dict


arr = map(int, raw_input().strip().split(' '))

num_replacements = {}
num_visited = set([])
updated_arr = []
for elem in arr:
    if elem not in num_visited:
        # print "calling DFS"
        # finding all the connected/transformable nodes/integers
        num_groups = dfs_undirected(transformations_dict, elem)
        min_of_num_group = min(num_groups)

        for num in num_groups:
            num_visited.add(num)

            # after knowing all the connected integers,
            # replacing all of them with the minimum in the lot
            # objective is to make integers as identical as possible
            num_replacements[num] = min_of_num_group

    updated_arr.append(num_replacements[elem])

print palindrome_max_length(updated_arr)
