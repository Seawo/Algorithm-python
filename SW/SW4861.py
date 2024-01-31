def find_palindrome(board):                                     # 이차원 배열을 입력받아 회문을 검사하는 함수
    for line in board:                                          # 한 줄 씩 돌며,
        for i in range(n - m + 1):                              # 한 줄 당 n-m번 검사
            word = line[i: i + m]                               # 길이가 m이 되도록 문자열을 슬라이싱하여
            if word == word[::-1]:                              # 회문이라면,
                return word                                     # 해당 문자열을 return
    return ''                                                   # 회문을 찾을 수 없다면 빈 문자열을 return

for tc in range(1, int(input()) + 1):                           # test case 만큼 돌며 검사
    n, m = map(int, input().split())                            # n(글자판 길이), m(회문 길이) 입력
    board = [input() for _ in range(n)]                         # board(글자판) 입력

    if find_palindrome(board):                                  # 해당 글자판에 회문이 있다면,
        print(f'#{tc} {find_palindrome(board)}')                # 해당 회문을 출력하고,
        continue                                                # 다음 test case로 넘어가기

    rotated_board = [''.join(line) for line in zip(*board)]     # zip 함수 활용하여 글자판 회전
    if find_palindrome(rotated_board):                          # 해당 글자판에 회문이 있다면,
        print(f'#{tc} {find_palindrome(rotated_board)}')        # 해당 회문 출력



