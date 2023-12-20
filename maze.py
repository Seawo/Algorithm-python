
dc = [1,-1,0,0]
dr = [0,0,-1,1]

maze = []

for T in range(int(input())):
    N = int(input())
    for _ in range(N):
        maze.append(list(map(int,input())))

    # 출발점 찾기
    # 주의 탐색으로 0를 찾는다??
    # 찾아가다가 3를 만나면 1 없다면 0를 반환?

