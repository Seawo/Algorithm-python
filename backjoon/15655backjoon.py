
from itertools import combinations, permutations

N,M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
combi = sorted(combinations(nums, M))

# 정렬해서 넣으면 된다
for i in combi:
    print(*i)