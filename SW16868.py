

T = int(input())
# 등급 배열 처음 등급이 1이니깐
level = [1]*T

# 모든 사람 데이터를 받는다.
infoall= [list(map(int, input().split())) for _ in range(T)] 

# 하나 하나 비교한다 (완전탐색)
for i in range(T):
    for j in range(T):
        if infoall[i][0] < infoall[j][0] and infoall[i][1] < infoall[j][1]:
            level[i]+=1
        else:
            continue
print(*level)
    # ABCDE 사람들을 비교하기
    # 등급을 매긴다
    
