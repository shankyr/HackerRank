import operator

n = int(raw_input().strip())
inp_arr = []
for ind in xrange(n):
    inp_arr.append(str(raw_input().strip()))

inp_arr.sort(key=lambda item: (len(item), item))

for ind in xrange(n):
    print inp_arr[ind]
