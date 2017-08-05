import timeit

start = timeit.default_timer()


def check_rows():
    global numbers
    global cost

    end_of_row = 0
    total = 0
    for ind in range(9):
        total += numbers[ind]
        end_of_row += 1
        if end_of_row == 3:
            cost += abs(15 - total)
            end_of_row = 0
            total = 0


def check_cols():
    global numbers
    global cost

    end_of_col = 0
    total = 0
    for row in range(3):
        for col in range(3):
            total += numbers[row + col * 3]
            end_of_col += 1
            if end_of_col == 3:
                cost += abs(15 - total)
                end_of_col = 0
                total = 0


def check_diags():
    global numbers
    global cost

    d1 = numbers[0] + numbers[4] + numbers[8]
    d2 = numbers[2] + numbers[4] + numbers[6]

    cost += abs(15 - d1)
    cost += abs(15 - d2)

numbers = []

for rows in range(3):
    numbers.extend(map(int, raw_input().strip().split(' ')))

cost = 0

check_rows()
check_cols()
check_diags()

print "cost", cost

ans = 0
while cost > 0:
    d, r = divmod(cost, 3)
    ans += d
    if 0 < r < 3:
        ans += 1
        break
    cost = r

print ans

print timeit.default_timer() - start
