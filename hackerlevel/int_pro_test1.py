

def getMaxElementIndices(a, rotate):
    arr_size = len(a)
    max_initial = a.index(max(a))

    max_indices = [max_initial]
    for i in xrange(1, arr_size):
        max_initial -= 1
        max_indices.append(max_initial)
        if max_initial == 0:
            max_initial = arr_size

    ans = []
    for ind in xrange(len(rotate)):
        r = rotate[ind] % arr_size

        ans.append(max_indices[r])

    return ans

a = [1, 2, 4, 3]
rotate = [1, 3]
print getMaxElementIndices(a, rotate)
