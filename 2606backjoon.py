

CT = int(input())

adj_matricx = [[0]*(CT+1) for _ in range(CT+1)]

cnt=0
for T in range(int(input())):
    start, end = map(int, input().split())
    adj_matricx[start][end] = 1
    adj_matricx[end][start] = 1
    
for i in range(CT+1):
    for j in range(CT+1):
        if adj_matricx[i][j] == 1:
            cnt += 1
    print(adj_matricx[i][:])
    
    # 행렬로 쌍을 이룬 값
print(cnt)