def compare_pairs(left, right):
    left_is_numeric = isinstance(left, int)
    right_is_numeric = isinstance(right, int)

    if left_is_numeric and right_is_numeric:

        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1

    elif left_is_numeric:
        left = [left]
        return compare_pairs(left, right)

    elif right_is_numeric:
        right = [right]
        return compare_pairs(left, right)

    else:
        i = 0

        while i < len(right):
            if i >= len(left):
                return -1

            res = compare_pairs(left[i], right[i])

            if res == 1:
                return 1
            elif res == 0:
                i += 1
            else:
                return -1

        return 0 if len(right) == len(left) else 1

with open('input', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    pairs = [[eval(lines[(i*3)]), eval(lines[(i*3)+1])] for i in range(len(lines) // 3 + 1)]

    right_order = []

    for i, pair in enumerate(pairs):
        if compare_pairs(pair[0], pair[1]) == -1:
            right_order.append(i+1)

    print(right_order)
    print(sum(right_order))


