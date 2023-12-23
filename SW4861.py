

for T in range(int(input())):
    
    N,M = map(int,input().split())
    for Nnum in range(N):
        word = list(input())
        check = word[::-1]
        if word == check:
            word= ''.join(word)
            print(word)
    