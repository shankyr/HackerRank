from collections import Counter

q = int(raw_input().strip())

for q0 in xrange(q):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))

    invalid_boxes = []
    max_picks = 0

    for i in xrange(n):

        # index/position is odd; so value should be odd
        if i & 1:
            if not (arr[i] & 1):
                invalid_boxes.append(arr[i])

            max_pick = arr[i] - 1 if arr[i] >= 2 else 0
            max_picks += max_pick

        # index/position is even; so value should be even
        else:
            if arr[i] & 1:
                invalid_boxes.append(arr[i])

            max_pick = arr[i] - 2 if arr[i] >= 3 else 0
            max_picks += max_pick

    len_invalid_boxes = len(invalid_boxes)

    if len_invalid_boxes & 1:
        print -1
    else:
        invalid_boxes_counter = Counter(invalid_boxes)

        len_1_boxes = invalid_boxes_counter[1]
        len_not_1_boxes = len_invalid_boxes - len_1_boxes

        if len_1_boxes <= len_not_1_boxes:
            len_remaining_not_1_boxes = len_not_1_boxes - len_1_boxes
            print len_1_boxes + (len_remaining_not_1_boxes / 2)

        else:
            if len_1_boxes <= max_picks:
                print len_1_boxes
            else:
                print -1
