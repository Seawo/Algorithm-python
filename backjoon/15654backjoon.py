
from itertools import combinations, permutations

N,M = map(int, input().split())
nums = list(map(int, input().split()))
perm = sorted(permutations(nums, M))

for i in perm:
    print(*i)
