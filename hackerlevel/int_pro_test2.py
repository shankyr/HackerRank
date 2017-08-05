from collections import Counter


def twins(a, b):
    n = len(a)
    solution = []

    for ind in xrange(n):
        solution.insert(ind, "Yes")

        a_str = a[ind]
        b_str = b[ind]

        a_str_counter = Counter(list(a_str))
        b_str_counter = Counter(list(b_str))

        if len(a_str_counter.keys()) != len(b_str_counter.keys()):
            print "1"
            solution[ind] = "No"
            continue

        else:
            for k in a_str_counter.keys():
                try:
                    if a_str_counter[k] != b_str_counter[k]:
                        solution[ind] = "No"
                        continue

                    else:
                        a_indices = [i for i, e in enumerate(a_str) if e == k]
                        b_indices = [i for i, e in enumerate(b_str) if e == k]

                        a_even_indices = 0
                        a_odd_indices = 0
                        for elem in a_indices:
                            if elem % 2 == 0:
                                a_even_indices += 1
                            else:
                                a_odd_indices += 1

                        b_even_indices = 0
                        b_odd_indices = 0
                        for elem in b_indices:
                            if elem % 2 == 0:
                                b_even_indices += 1
                            else:
                                b_odd_indices += 1

                        if a_even_indices != b_even_indices or a_odd_indices != b_odd_indices:
                            solution[ind] = "No"

                except KeyError:
                    solution[ind] = "No"
                    continue

    return solution


a = ["abbc", "abbdd"]
b = ["abbc", "ddbba"]

print twins(a, b)
