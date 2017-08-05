import heapq

Q = int(raw_input().strip())
input_heap = []
input_dict = {}
input_dict_key_set = set([])

for q in xrange(Q):
    inp = raw_input().strip().split(' ')

    if int(inp[0]) == 1:
        if inp[1] in input_dict_key_set:
            input_dict[inp[1]] = 'A'
        else:
            heapq.heappush(input_heap, int(inp[1]))
            input_dict[inp[1]] = 'A'
            input_dict_key_set.add(inp[1])

    elif int(inp[0]) == 2:
        input_dict[inp[1]] = 'I'

    else:
        while True:
            val = input_heap[0]
            if input_dict[str(val)] == 'A':
                print val
                break
            else:
                val = heapq.heappop(input_heap)

print input_heap
print input_dict
print input_dict_key_set