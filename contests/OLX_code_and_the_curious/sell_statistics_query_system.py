
day = {}
day_prod = {}
day_prod_catg = {}
day_st = {}
day_st_reg = {}

T = int(raw_input().strip())

p_name = 1
for t in xrange(T):
    inp = raw_input().strip().split(' ')

    # inp[1]
    day01_day02 = map(int, inp[1].split('.'))
    if len(day01_day02) == 2:
        day01, day02 = day01_day02[0], day01_day02[1]
    else:
        day01, day02 = day01_day02[0], 0

    # inp[2]
    prod_catg = map(int, inp[2].split('.'))
    if len(prod_catg) == 2:
        prod, catg = prod_catg[0], prod_catg[1]
    else:
        prod, catg = prod_catg[0], 0

    # inp[3]
    st_reg = map(int, inp[3].split('.'))
    if len(st_reg) == 2:
        st, reg = st_reg[0], st_reg[1]
    else:
        st, reg = st_reg[0], 0

    if inp[0] == "S":
        day02 = day01
        try:
            day[(day01, day02)].add(p_name)
        except KeyError:
            day[(day01, day02)] = {p_name}

        try:
            day_prod[(day01, prod)].add(p_name)
        except KeyError:
            day_prod[(day01, prod)] = {p_name}

        try:
            day_prod_catg[(day01, prod, catg)].add(p_name)
        except KeyError:
            day_prod_catg[(day01, prod, catg)] = {p_name}

        try:
            day_st[(day01, st)].add(p_name)
        except KeyError:
            day_st[(day01, st)] = {p_name}

        try:
            day_st_reg[(day01, st, reg)].add(p_name)
        except KeyError:
            day_st_reg[(day01, st, reg)] = {p_name}

        p_name += 1

        # print day

        # print day_prod
        # print day_prod_catg

        # print day_st
        # print day_st_reg

    else:
        if day02 == 0:
            day02 = day01

        ans = 0
        if catg == 0 and reg == 0:
            for d in xrange(day01, day02 + 1):
                if prod == -1 and st == -1:
                    try:
                        ans += len(day[(d, d)])
                    except KeyError:
                        ans += 0

                elif prod != -1 and st == -1:
                    try:
                        ans += len(day_prod[(d, prod)] & day[(d, d)])
                    except KeyError:
                        ans += 0

                elif prod == -1 and st != -1:
                    try:
                        ans += len(day[(d, d)] & day_st[(d, st)])
                    except KeyError:
                        ans += 0
                else:
                    try:
                        ans += len(day_prod[(d, prod)] & day_st[(d, st)])
                    except KeyError:
                        ans += 0

        elif catg != 0 and reg == 0:
            for d in xrange(day01, day02 + 1):
                if st == -1:
                    try:
                        ans += len(day_prod_catg[(d, prod, catg)] & day[(d, d)])
                    except KeyError:
                        ans += 0
                else:
                    try:
                        ans += len(day_prod_catg[(d, prod, catg)] & day_st[(d, st)])
                    except KeyError:
                        ans += 0

        elif catg == 0 and reg != 0:
            for d in xrange(day01, day02 + 1):
                if prod == -1:
                    try:
                        ans += len(day[(d, d)] & day_st_reg[(d, st, reg)])
                    except KeyError:
                        ans += 0
                else:
                    try:
                        ans += len(day_prod[(d, prod)] & day_st_reg[(d, st, reg)])
                    except KeyError:
                        ans += 0
        else:
            for d in xrange(day01, day02 + 1):
                try:
                    ans += len(day_prod_catg[(d, prod, catg)] & day_st_reg[(d, st, reg)])
                except KeyError:
                    ans += 0
        print ans

