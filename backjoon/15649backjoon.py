

N,M = map(int, input().split())

arr = [ _ for _ in range(1,N+1)]
sel = [0]*M
check = [0]*N 

def perm(depth):
    if depth == M:
        print(*sel)
        return
    
    for i in range(N):
        if not check[i]:
            check[i] = 1
            sel[depth] = arr[i]
            perm(depth+1)
            check[i] = 0
perm(0)