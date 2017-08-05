

n, k = map(int, raw_input().strip().split(' '))
n_arr = map(int, raw_input().strip().split(' '))
n_arr_sorted = sorted(n_arr)
n_arr_sorted_set = set(n_arr_sorted)

answer_arr = []
for i in xrange(n):
    answer = 0
    search_num = n_arr_sorted[i]
    while search_num < n_arr_sorted[-1]:
        search_num += k
        if search_num in 




answer = 0
search_num = min_pick
while search_num <= n_arr_sorted[-1]:
    answer += 1
    search_num += k



