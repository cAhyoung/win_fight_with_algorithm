n = int(input('몇개의 합을 더할 것인지 적으시오: '))  # 정수로 받아야 range 함수 이용 가능
num = input('숫자들을 공백없이 적으시오: ')  # 문자열로 받아야 인덱스로 접근할 수 있음
tot_num = 0  # 수들을 더할 때 사용해줄 값

for i in range(n):
    tot_num += int(num[i])
                # ^ 덧셈 연산은 숫자형으로 변환해야 하기때문에 인덱스로 접근한 값을 정수형으로 변환해줌
    i += 1

print(tot_num)

