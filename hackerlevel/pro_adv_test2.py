from collections import Counter


def bestTrio(friends_nodes, friends_from, friends_to):

    frn = {}
    for ind in xrange(len(friends_from)):
        try:
            frn[friends_from[ind]].append(friends_to[ind])
        except KeyError:
            frn[friends_from[ind]] = [friends_to[ind]]

        try:
            frn[friends_to[ind]].append(friends_from[ind])
        except KeyError:
            frn[friends_to[ind]] = [friends_from[ind]]

    friends_with_two_best = [f for f in Counter(friends_from) if Counter(friends_from)[f] > 1]

    if len(friends_with_two_best) == 0:
        return -1

    trios = []
    for f1 in friends_with_two_best:
        f2s = frn[f1]
        f2s_set = set(f2s)

        for f2 in f2s:
            f3s = frn[f2]

            for f3 in f3s:
                if f3 in f2s_set:
                    trios.append([f1, f2, f3])

    sums = []
    for trio in trios:
        first_score = len(frn[trio[0]]) - 2
        if first_score < 0:
            first_score = 0
        second_score = len(frn[trio[1]]) - 2
        if second_score < 0:
            second_score = 0
        third_score = len(frn[trio[2]]) - 2
        if third_score < 0:
            third_score = 0

        sums.append(first_score + second_score + third_score)

    return min(sums)


print bestTrio(5, [1, 1, 2, 2, 3, 4], [2, 3, 3, 4, 4, 5])
print bestTrio(7, [2, 3, 5, 1], [1, 6, 1, 7])
