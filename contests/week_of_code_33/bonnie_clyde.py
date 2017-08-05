# its a wrong solution, I mis-understood the question as its asking
# to check if bonnie and clyde could reach sushi without passing
# through each others nodes. So, I did a dfs on bonnie adding
# clyde as already visited node; so no nodes connected to clyde
# will be picked. If I can see sushi node in the result dfs path,
# then bonnie is able to reach sushi without passing through clyde.
# I did run same logic on clyde as well; and formulated answer as
# "YES" or "NO". Surprisingly, it passed couple of tests.

import timeit

start = timeit.default_timer()


def dfs_undirected(e, source, kill):
    # a list to keep track of the vertices visited applying DFS
    dfs_order = set([])

    # a list to keep track of all visited vertices to ensure
    # we don't process DFS for already visited vertex
    ver_visited = set([])

    # a STACK data structure to pick elements to apply DFS
    ver_traverse_stack = []

    # initializing with starting vertex
    ver_visited.add(source)
    ver_visited.add(kill)
    ver_traverse_stack.append(source)

    while len(ver_traverse_stack) != 0:

        ver_picked = ver_traverse_stack.pop()
        dfs_order.add(ver_picked)

        vertices = e[ver_picked]

        for vertex in vertices:

            if vertex not in ver_visited:
                ver_visited.add(vertex)
                ver_traverse_stack.append(vertex)

    return ver_visited


# PROGRAM BEGINS HERE
# read number of vertices - n; and
# number of edges - m
n, m, q = map(int, raw_input().strip().split(' '))

# a dictionary to hold all edges
edges = {}

# run loop to read all edges
for edge in xrange(m):
    u, v = map(int, raw_input().strip().split(' '))

    # adding edge to dictionary with tail as key;
    # and all outgoing heads appended to value list
    try:
        edges[u].append(v)
    except KeyError:
        edges[u] = [v]

    try:
        edges[v].append(u)
    except KeyError:
        edges[v] = [u]

# print edges
all_paths = {}

for q0 in xrange(q):
    bon, cly, shu = map(int, raw_input().strip().split(' '))

    try:
        check01 = shu in all_paths[(bon, cly)]
        # print "Success"
    except KeyError:
        all_paths[(bon, cly)] = dfs_undirected(edges, bon, cly)
        check01 = shu in all_paths[(bon, cly)]

    try:
        check02 = shu in all_paths[(cly, bon)]
        # print "Success"
    except KeyError:
        all_paths[(cly, bon)] = dfs_undirected(edges, cly, bon)
        check02 = shu in all_paths[(cly, bon)]

    if check01 and check02:
        print "YES"
    else:
        print "NO"

# print timeit.default_timer() - start
