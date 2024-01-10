
# 내풀이
# T = int(input())

# Working = []


# for tc in range(T):
#     name, status = input().split()
    
#     if status == 'enter':
#         Working.append(name)
    
#     if status == 'leave':
#         Working.remove(name)

# working_member = sorted(list(Working), reverse= True)

# for member in working_member:
#     print(('').join(member))
###########################################################################


# 수정 set 자료구조 활용
T = int(input())

Working = []


for tc in range(T):
    name, status = input().split()
    
    if status == 'enter':
        Working.append(name)
    
    if status == 'leave':
        Working.remove(name)

working_member = sorted(list(Working), reverse= True)

for member in working_member:
    print(('').join(member))
