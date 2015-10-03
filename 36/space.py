#!/usr/bin/env python3

try:
    while True:
        print(' '.join(input()))
except EOFError:
    print('Done.')

import sys

for line in sys.stdin:
    print(' '.join(line[:-1]))

