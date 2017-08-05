import timeit

start = timeit.default_timer()


def has_cycle(head):
    lst = []
    lst.append(head)

    if head is None or head.next is None:
        return False

    left = head
    right = head.next

    lst.append(left)

    while right is not None:
        if right in lst:
            return True

        left = left.next
        right = right.next

        lst.append(left)

    return False

print timeit.default_timer() - start
