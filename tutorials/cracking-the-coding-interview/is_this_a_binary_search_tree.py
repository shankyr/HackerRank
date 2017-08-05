import timeit

start = timeit.default_timer()


def check_bst(root, minVal, maxVal):
    if root is None:
        return True
    else:
        if root.data < minVal or root.data > maxVal:
            return False
        return check_bst(root.left, minVal, root.data - 1) and check_bst(root.right, root.data + 1, maxVal)


def check_binary_search_tree_(root):
    return check_bst(root, 0, 10000)

print timeit.default_timer() - start
