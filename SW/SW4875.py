
dc = [1,-1,0,0]
dr = [0,0,-1,1]

maze = []

for T in range(int(input())):
    N = int(input())
    for _ in range(N):
        maze.append(list(map(int,input())))

    res = 0
    stack = []
    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                stack = i,j
                break
        if stack:
            break    
    
    while stack != []:
        r,c = stack.pop()
        
        # 찾아가다가 3를 만나면 반환 결과값 반환 = 1
        if maze[r][c] == 3:
            res = 1
            break
        
        maze[r][c] == 1
        
        # 4방 탐색으로 0를 찾는다    
        for _ in range(4):
            nr = r + dr
            nc = c + dc
            
            # 행, 열이 범위 안에 있는지, 값이 1이 아니라면
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1:
                stack.append(nr,nc)
        
    print(res)

