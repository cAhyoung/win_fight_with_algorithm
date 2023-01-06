# 입력받은 수를 재조합 하여 다시 원래 수로 돌아오는 번째를 구하기
# 무한루프에 빠지는 이유: 입력받은 n을 기준으로 루프문을 돌리면 무한루프에 빠짐
# 이때 새로운 new_n이라는 변수를 설정해줘서 이 수를 기준으로 루프문을 돌리면 됨
# 입력받은 수는 계속 유지될 수 있도록 해주는게 포인트인 것 같음
# 수지킴의 질문

n = int(input())

if n < 0:
    left = n
    right = n + 0
    new_n = int(str(left) + str(right))

else:
    left = n % 10
    right = (left + (n // 10)) % 10
    new_n = int(str(left) + str(right))

i = 1

while True:
    if new_n < 10:
        left = new_n
        right = new_n + 0
        new_n = int(str(left) + str(right))
        print(new_n)

        if n == new_n:
            i += 1
            print(i)
            break
        else:
            i += 1

    else:
        left = new_n % 10
        right = (left + (new_n//10)) % 10

        new_n = int(str(left) + str(right))
        print(new_n)

        if n == new_n:
            i += 1
            print(i)
            break
        else:
            i += 1

