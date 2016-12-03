#!/usr/bin/env python3

n = int(input())

for case in range(n):
    credit = int(input())
    n_items = int(input())
    items = [int(i) for i in input().strip().split(' ')]
    min_dist = credit
    x, y = 0, 0
    for i in range(len(items) - 1):
        for j in range(i + 1, len(items)):
            curr_dist = credit - (items[i] + items[j])
            if curr_dist < 0:
                continue
            if curr_dist <= min_dist:
                min_dist = curr_dist
                x, y = i + 1, j + 1
                if curr_dist == 0:
                    break

    print('Case #{}: {} {}'.format(case + 1, x, y))

