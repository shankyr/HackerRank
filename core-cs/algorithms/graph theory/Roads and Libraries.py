#https://www.hackerrank.com/challenges/torque-and-development/submissions/code/47239863
#!/bin/python3

import sys
from collections import deque

q = int(input().strip())
for a0 in range(q):
    n, m, c_lib, c_road = input().strip().split(' ')
    n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
    edges = {}
    for a0 in range(1, n+1):
        edges[a0] = [a0]
    connected_cities = {}
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        
        # adding edge to dictionary with tail as key and head appended to value list
        try:
            edges[city_1].append(city_2)
        except KeyError:
            edges[city_1] = [city_2]

        # run below try except block only if its un-directional graph
        try:
            edges[city_2].append(city_1)
        except KeyError:
            edges[city_2] = [city_1]
    
    #print (edges)
    ver_visited = set([])
    ver_traverse_queue = deque([])
    n_lib = 0
    if (c_lib < c_road):
        print (n * c_lib)
    else:
        for a0 in range(1,n+1):
            if a0 not in ver_visited:
                ver_visited.add(a0)
                ver_traverse_queue.append(a0)
                n_lib += 1
                connected_cities[n_lib] = [a0]
            while len(ver_traverse_queue) != 0:
                ver_picked = ver_traverse_queue.popleft()
                for t in edges[ver_picked]:
                    if t not in ver_visited: 
                        ver_traverse_queue.append(t)
                        ver_visited.add(t)
                        connected_cities[n_lib].append(t)
        #print (connected_cities)
        print ((n_lib * c_lib) + (n - n_lib)*c_road)
 
