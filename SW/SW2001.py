
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for x in range(N - M + 1):          
        for y in range(N - M + 1):
            tmp = sum(board[i][j] for i in range(x, x + M) for j in range(y, y + M))   
            ans = max(tmp, ans)         
    
    print(f"#{tc} {ans}")
        