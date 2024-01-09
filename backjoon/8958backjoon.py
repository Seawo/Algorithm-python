
T = int(input())

for i in range(T):
    cnt = 0
    res = 0
    check = list(input())
    
    for checks in check:
        if checks == 'O':
            cnt +=1
            res += cnt
        elif checks == 'X':
            cnt = 0
    print(res)