#!/usr/bin/env python3
"""Count consecutive pairs of letters.

To view those without vowels in sorted order:
./mr.py cat pairs | sort -k 2 -n | grep -v [aeiou]
"""

import sys
from mr import emit

def count_pairs(line):
    """A map function that counts all pairs of letters."""
    for word in line.lower().split():
        for i in range(len(word)-2):
            emit(word[i:i+2], 1)

for line in sys.stdin:
    count_pairs(line)
