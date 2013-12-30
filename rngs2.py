#!/usr/bin/env python
# coding: utf-8
import sys

s = """Wybierz generator:
1) MWC1
2) MWC2
3) Cong
4) SHR3
5) MWC64
6) KISS
7) KISS2
8) LFSR113 (Tausworthe)
9) LFSR88 (Tausworthe)
"""

print s
G = int(raw_input(">>> "))
N = int(raw_input("Wielkość próby:\n>>> "))

s1 = int(raw_input("Seed1:\n>>> "))
s2 = int(raw_input("Seed2:\n>>> "))
s3 = int(raw_input("Seed3:\n>>> "))
s4 = int(raw_input("Seed4:\n>>> "))

if G == 1:
    from simplerandom.iterators import MWC1 as rng
elif G == 2:
    from simplerandom.iterators import MWC2 as rng
elif G == 3:
    from simplerandom.iterators import Cong as rng
elif G == 4:
    from simplerandom.iterators import SHR3 as rng
elif G == 5:
    from simplerandom.iterators import MWC64 as rng
elif G == 6:
    from simplerandom.iterators import KISS as rng
elif G == 7:
    from simplerandom.iterators import KISS2 as rng
elif G == 8:
    from simplerandom.iterators import LFSR113 as rng
elif G == 9:
    from simplerandom.iterators import LFSR88 as rng
else:
    sys.exit()

rng = rng(s1, s2, s3, s4)
for i in range(N):
    print next(rng)
