

N = int(input())

for num in range(1, N+1):
    Sum_num = num + sum(map(int, str(num))) #문자열로 나온뒤,
                                            # int형으로 두개 뽑고 그 값을 더한다
    if Sum_num == N:
        print(num)
        break
else:
    print(0)
