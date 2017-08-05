# 5/25 tests passed

import timeit
from collections import deque, Counter
import sys

start = timeit.default_timer()


def kmp_pattern_search(pat, txt):
    M = len(pat)
    N = len(txt)
    pattern_count = 0

    lps = [0] * M
    j = 0

    calc_lps(pat, M, lps)

    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            pattern_count += 1
            j = lps[j - 1]

        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return pattern_count


def calc_lps(pat, M, lps):
    len = 0

    lps[0]
    i = 1

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]

            else:
                lps[i] = 0
                i += 1


def get_path(u1, v1):
    global paths_up_until_1
    global nodes_up_until_1

    if u1 == v1:
        return names[u1 - 1]

    u1_nodes = nodes_up_until_1[u1]
    v1_nodes = nodes_up_until_1[v1]

    slice_spot = len(set(u1_nodes) & set(v1_nodes))

    if slice_spot == len(u1_nodes):
        return paths_up_until_1[v1][::-1][slice_spot - 1:]

    elif slice_spot == len(v1_nodes):
        if slice_spot == 1:
            return paths_up_until_1[u1]

        return paths_up_until_1[u1][:-slice_spot + 1]

    else:
        return paths_up_until_1[u1][:-slice_spot] + paths_up_until_1[v1][::-1][slice_spot - 1:]


def bfs_undirected(s):
    global edges
    global names

    ver_visited = set([])

    ver_traverse_queue = deque([])

    ver_visited.add(s)
    ver_traverse_queue.append(s)

    while len(ver_traverse_queue) != 0:

        ver_picked = ver_traverse_queue.popleft()

        vertices = edges[ver_picked]

        for vertex in vertices:
            if vertex not in ver_visited:
                ver_visited.add(vertex)
                ver_traverse_queue.append(vertex)

                paths_up_until_1[vertex] = names[vertex - 1] + paths_up_until_1[ver_picked]
                nodes_up_until_1[vertex] = [vertex] + nodes_up_until_1[ver_picked]


# program begins here
n, q = map(int, raw_input().strip().split(' '))
names = raw_input().strip()
p = raw_input().strip()

names_counter = Counter(names)
names_counter_keys = set(names_counter.keys())

pattern_counter = Counter(p)
pattern_counter_keys = pattern_counter.keys()

for each_pattern_char in pattern_counter_keys:
    if each_pattern_char not in names_counter_keys:
        for q0 in xrange(q):
            print 0
        sys.exit(0)
    elif pattern_counter[each_pattern_char] > names_counter[each_pattern_char]:
        for q0 in xrange(q):
            print 0
        sys.exit(0)

edges = {}
# run loop to read all edges
for edge in xrange(n - 1):
    u, v = map(int, raw_input().strip().split(' '))

    # adding edge to dictionary with tail as key;
    # and head appended to value list
    try:
        edges[u].append(v)
    except KeyError:
        edges[u] = [v]

    # run below try except block only if its un-directional graph
    try:
        edges[v].append(u)
    except KeyError:
        edges[v] = [u]


paths_up_until_1 = {1: names[0]}
nodes_up_until_1 = {1: [1]}

bfs_undirected(1)

# print paths_up_until_1
# print nodes_up_until_1
strings_match_count = {}
for q0 in xrange(q):
    u, v = map(int, raw_input().strip().split(' '))

    path_string = get_path(u, v)

    # print u, v
    # print path_string
    try:
        print strings_match_count[path_string]
    except KeyError:
        count = kmp_pattern_search(p, path_string)
        strings_match_count[path_string] = count
        print count

# print timeit.default_timer() - start
