

n, m, k = map(int, raw_input().strip().split(' '))

track_cells = 0
track_end_points = {}
track_rows = set([])
for track in xrange(k):
    r, c1, c2 = map(int, raw_input().strip().split(' '))

    if r in track_rows:
        t_c1, t_c2 = track_end_points[r]

        if c1 > t_c2 or c2 < t_c1:
            track_cells += abs(c2 - c1) + 1
        else:
            track_cells -= abs(t_c2 - t_c1) + 1
            n_c1, n_c2 = min(c1, t_c1), max(c2, t_c2)
            track_cells += abs(n_c2 - n_c1) + 1
            track_end_points[r] = (n_c1, n_c2)

    else:
        track_rows.add(r)
        track_end_points[r] = (c1, c2)

        track_cells += abs(c2 - c1) + 1

print n * m - track_cells
