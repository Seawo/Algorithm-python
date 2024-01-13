
import sys
input = sys.stdin.readline

N,M  = map(int, input().split()) # N: 포켓몬 개수, M: 문제의 개수

Encyclopedia = dict() # 포켓몬 도감

for tc in range(N):
    pokemon_name = input().rstrip()
     
    Encyclopedia[pokemon_name] = str(tc+1)
    Encyclopedia[str(tc+1)] = pokemon_name
    
for test in range(M):
    print(Encyclopedia[input().rstrip()]) # 양 쪽 복사로 키값을 받으면 그의 맞는 value 출력 



