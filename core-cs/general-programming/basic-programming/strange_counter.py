#!/bin/python

t = int(raw_input().strip())

time = 1
val = 3

while time <= t:
    prev_val = val
    prev_time = time

    time += prev_val
    val = 2 * prev_val

if time - t < t - prev_time:
    print time - t
else:
    print prev_val - (t - prev_time)
