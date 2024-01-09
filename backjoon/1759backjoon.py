from itertools import combinations 

L, C = map(int, input().split())
alphabats = list(input().split())

vowels_gather = ['a','e','i','o','u'] 

vowels = []
consonant = []

# 입력된 값에서 모음과 자음을 두개로 쪼개다.
for alphabat in alphabats:
    if alphabat in vowels_gather:
        vowels.append(alphabat)
    else:
        consonant.append(alphabat)
        
password = [] # 암호

# 최소 한개 모음, 두개의 자음으로 구성 되어있다

# vowels 안에 있는 만큼 돌려서 붙여서 만들어 보자

# 모음이 1개랑 자음이 2개 이상이므로 주어진 글자L에서
# 자음 2개를 뺸 범위 지정 처음 모음을 넣는 부분 부터니 -1
for v in range(1, L-2):
    # 모음을 뽑는다
    for vow in combinations(vowels, v):
        # 자음을 뽑는다
        for cons in combinations(consonant, L-v):
            tmp_password = sorted(list(vow + cons))
            password.append(tmp_password)
password.sort()            

for i in password:
    i = (('').join(i))
    print(i)

    
    
    
