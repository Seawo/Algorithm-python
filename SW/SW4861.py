

for T in range(int(input())):
    N,M = list(map(int, input().split()))
    borad =[input() for _ in range(int(M))]

for _ in range(M):
    print(borad[_][:])


# 가로 비교
# 세로 비교 를 각각 하면서
# 회문을 구한다. 