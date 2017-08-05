import timeit

start = timeit.default_timer()

s, n, m = map(int, raw_input().strip().split(' '))
key_board = map(int, raw_input().strip().split(' '))
usb = map(int, raw_input().strip().split(' '))

purchase = -1
curr_purchase = 0

for kb in key_board:
    for u in usb:
        curr_purchase = kb + u
        if purchase < curr_purchase <= s:
            purchase = curr_purchase

print purchase

print timeit.default_timer() - start

