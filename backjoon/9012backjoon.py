


for T in range(int(input())):
    
    brackets = input()
    check = []
    
    for bracket in brackets:
        if bracket == '(':
            check.append(bracket)
        elif check:
            check.pop()
        else:
            check = True
            break    
    print("YES" if not check else "NO")