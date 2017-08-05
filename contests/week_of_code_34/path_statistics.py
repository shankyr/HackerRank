# 2/38 tests passed

from collections import deque


def bfs_undirected(e, s, d):
    global u_v_cost_counters

    ver_visited = set([])
    ver_traverse_queue = deque([])

    ver_visited.add(s)
    ver_traverse_queue.append(s)

    u_v_cost_counters[s] = {costs[s - 1]: 1}

    while len(ver_traverse_queue) != 0:
        ver_picked = ver_traverse_queue.popleft()

        vertices = e[ver_picked]

        for vertex in vertices:
            if vertex not in ver_visited:
                ver_visited.add(vertex)
                ver_traverse_queue.append(vertex)

                curr_ver_cost = costs[vertex - 1]

                temp_cost_counters = u_v_cost_counters[ver_picked].copy()

                try:
                    temp_cost_counters[curr_ver_cost] += 1
                except KeyError:
                    temp_cost_counters[curr_ver_cost] = 1

                u_v_cost_counters[vertex] = temp_cost_counters

        if d in ver_visited:
            break


n, q = map(int, raw_input().strip().split(' '))

costs = map(int, raw_input().strip().split(' '))

edges = {}

for edge in xrange(n - 1):
    u, v = map(int, raw_input().strip().split(' '))

    try:
        edges[u].append(v)
    except KeyError:
        edges[u] = [v]

    try:
        edges[v].append(u)
    except KeyError:
        edges[v] = [u]

answers = {}
for i in xrange(q):
    u_v_cost_counters = {}

    u, v, k = map(int, raw_input().strip().split(' '))

    try:
        v_costs_counter_sorted = answers[(u, v)]
    except KeyError:
        bfs_undirected(edges, u, v)

        v_costs_counter = u_v_cost_counters[v]

        v_costs_counter_sorted = sorted(v_costs_counter.items(), key=lambda x: (x[1], x[0]), reverse=True)

        answers[(u, v)] = v_costs_counter_sorted
        answers[(v, u)] = v_costs_counter_sorted

    ans = v_costs_counter_sorted[k - 1][0]

    print ans
