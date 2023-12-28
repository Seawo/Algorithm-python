
N, M = map(int,input().split())

cards = list(map(int,input().split()))

max = 0

for i in range(N-2):
    for j in range(i+1, N-1):
       for k in range(j+1, N):
           resum = cards[i] + cards[j] +cards[k]
           if max < resum <= M:
               max = resum
print(max)
               
    