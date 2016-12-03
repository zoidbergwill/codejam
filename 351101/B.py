#!/usr/bin/env python3

n = int(input())

for case in range(n):
    x = input()
    print('Case #{}: {}'.format(case + 1, ' '.join(reversed(x.split(' ')))))

