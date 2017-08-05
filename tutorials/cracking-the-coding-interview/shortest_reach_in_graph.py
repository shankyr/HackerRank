from collections import deque


def calc_shortest_path(edges, s):
    global dist

    ver_visited = []
    ver_traverse_queue = deque([])

    ver_visited.append(s)
    ver_traverse_queue.append(s)

    dist[s] = 0
    while len(ver_traverse_queue) != 0:
        ver_ref = ver_traverse_queue.popleft()

        try:
            vertices = edges[ver_ref]
        except KeyError:
            continue

        for v in vertices:
            if v not in ver_visited:
                ver_visited.append(v)
                ver_traverse_queue.append(v)
                dist[v] = (dist[ver_ref]/6 + 1) * 6


tests = int(raw_input().strip())

for test in xrange(tests):
    n, m = map(int, raw_input().strip().split(' '))

    edges = {}
    for i in xrange(m):
        u, v = map(int, raw_input().strip().split(' '))
        try:
            edges[u].append(v)
        except KeyError:
            edges[u] = [v]

        try:
            edges[v].append(u)
        except KeyError:
            edges[v] = [u]

    s = int(raw_input().strip())

    dist = {}
    for i in xrange(1, n + 1):
        dist[i] = -1

    calc_shortest_path(edges, s)

    for k in dist.keys():
        if k == s:
            continue
        print dist[k],
    print
