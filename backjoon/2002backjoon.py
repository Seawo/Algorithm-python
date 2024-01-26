
    
N = int(input())

in_car = []
for _ in range(N):
    in_car.append(input())                   

out_car = []
for _ in range(N):
    out_car.append(in_car.index(input()))   # 3 0 1 2
    
standard = N                                    
cnt = 0
for i in range(N-1, -1, -1): # index:3 2 1 0  value: 3 0 1 2  
    if out_car[i] > standard:                 
        cnt += 1                                
    else:                                       
        standard = out_car[i]                 

print(cnt)