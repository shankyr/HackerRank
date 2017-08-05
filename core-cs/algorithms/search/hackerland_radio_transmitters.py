

n, k = map(int, raw_input().strip().split(' '))

houses_all = map(int, raw_input().strip().split(' '))
houses = list(set(houses_all))

count = 0
part = 1

while True:

    last_part = True

    if part & 1:
        # print "IF block", part
        houses.sort()
        lower, higher = houses[0], houses[0] + k

        for i in xrange(len(houses)):
            # print i, len(houses)
            if lower <= houses[i] <= higher:
                # tower = houses[i]
                pass
            else:
                count += 1
                houses = list(houses[i - 1:])
                last_part = False
                break

    else:
        # print "ELSE block", part
        houses.sort()
        lower, higher = houses[0], houses[0] + k

        for i in xrange(len(houses)):
            # print i, len(houses)
            if lower <= houses[i] <= higher:
                # tower = houses[i]
                pass
            else:
                # count += 1
                houses = list(houses[i:])
                last_part = False
                break

    if len(houses) == 0:
        break
    elif last_part:
        # print "Hello", part
        if part & 1:
            count += 1
        break

    part += 1

print count
