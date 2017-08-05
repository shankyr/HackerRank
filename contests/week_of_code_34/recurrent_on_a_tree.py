# 9/63 tests passed

import timeit
from collections import deque

start = timeit.default_timer()


def fibonacci_dp(m):
    global fib_dict

    for i in xrange(3, m + 1):
        fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]


def bfs_undirected(e, s):

    global costs
    global all_costs

    path_costs = {}

    ver_visited = set([])

    # a QUEUE data structure to pick elements to apply BFS
    ver_traverse_queue = deque([])

    # initialize below data structures that drive the BFS
    ver_visited.add(s)
    ver_traverse_queue.append(s)
    path_costs[s] = costs[s - 1]

    try:
        all_costs[costs[s - 1]] += 1
    except KeyError:
        all_costs[costs[s - 1]] = 1

    # below BFS algorithm is run considering each vertex as starting
    # vertex until all the vertices are done
    while len(ver_traverse_queue) != 0:
        ver_picked = ver_traverse_queue.popleft()
        path_cost = path_costs[ver_picked]

        vertices = e[ver_picked]

        for vertex in vertices:
            if vertex not in ver_visited:
                ver_visited.add(vertex)
                ver_traverse_queue.append(vertex)

                path_costs[vertex] = path_cost + costs[vertex - 1]

                try:
                    all_costs[path_costs[vertex]] += 1
                except KeyError:
                    all_costs[path_costs[vertex]] = 1


n = int(raw_input().strip())

# a dictionary to hold all edges
edges_undirected = {}

# run loop to read all edges
for edge in xrange(n - 1):
    u, v = map(int, raw_input().strip().split(' '))

    # adding edge to dictionary with tail as key;
    # and all outgoing heads appended to value list

    try:
        edges_undirected[u].append(v)
    except KeyError:
        edges_undirected[u] = [v]

    try:
        edges_undirected[v].append(u)
    except KeyError:
        edges_undirected[v] = [u]

# print edges_undirected

costs = map(int, raw_input().strip().split(' '))
# for i in xrange(n):
#     print i + 1, costs[i]

all_costs = {}
for i in xrange(1, n + 1):
    # print "====", root, "===="
    # print dfs_undirected(edges_undirected, root)
    bfs_undirected(edges_undirected, i)

fib_dict = {0: 1, 1: 1, 2: 2}
fibonacci_dp(max(all_costs.keys()))

total_sum = 0
for k in all_costs.keys():
    # print k, all_costs[k], fib_dict[k]
    total_sum += fib_dict[k] * all_costs[k]
    total_sum %= 1000000007

print total_sum

# print timeit.default_timer() - start
