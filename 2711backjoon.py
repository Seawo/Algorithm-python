

for T in range(int(input())):

    num, spell = input().split()
    _index = int(num)

    res =''
    cnt = 1
    for word in spell:
        if cnt == _index:
            word = ''
            res += word
        else:
            res+=word
        cnt +=1
    print(*res.split())