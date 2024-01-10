

T = int(input())

def preorder(V):
    global cnt
    cnt += 1
    if left[V] > 0:
        preorder(left[V])
    if right[V] > 0:
        preorder(right[V])



for tc in range(1, T+1):
    E, N = map(int, input().split()) # 간선갯수 E, 시작점 E
    Node_value = list(map(int, input().split()))
    # 부모 자식 순으로 숫자가 들어오고 첫 값은 루트 노드이다
    
    # 왼쪽과 오른 쪽이라는 일차원 배열로 정리할 것
    left = [0]*(E*2)
    right = [0]*(E*2)
    cnt = 0
    
    for i in range(E):
        parent = Node_value[2*i]    
        child  = Node_value[2*i+1]
        if not left[parent]:
            left[parent] = child
        else:
            right[parent] = child

    preorder(N)
    
    print(f'#{tc} {cnt}')
    