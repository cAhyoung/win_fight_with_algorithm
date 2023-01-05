# 백준 온라인 저지 10986, 시간제한 1초, 난이도 골드 III

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = [0]
sum_num = 0
rest_list =[]

for i in num_list:
    sum_num += i
    sum_list.append(sum_num)

for j in sum_list:
    rest_list.append(j%m)

for k in range(1, len(rest_list)):  #리스트의 요소들을 하나하나 꺼내 대조해보면서..
    for l in range(1, len(rest_list)):
        if (rest_list[k] - rest_list[l]) % m == 0:
            print(k, l)




