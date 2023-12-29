
cards=[]
cnt = 1
T = int(input())
for order in range(1, T+1):
    cards.append(order)

while len(cards) != 1:
    if cnt == 1:
        cards.pop(0)
        cnt +=1
    elif cnt == 2:
        cards.append(cards[0])
        cards.pop(0)
        cnt +=1
    else:
        cnt =1

print(*cards)