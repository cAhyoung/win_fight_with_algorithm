# 백준 온라인 저지 11660, 시간제한 1초, 난이도 실버 I
# 이해 못함.. 이해좀 해볼게요
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr_list = [[0]*(n+1)]
sum_list = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    arr_row = [0] + [int(x) for x in input().split()]
    arr_list.append(arr_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_list[i][j] = sum_list[i][j-1] + sum_list[i-1][j] - sum_list[i-1][j-1] + arr_list[i][j]
        print(sum_list)

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    result = sum_list[x2][y2] - sum_list[x1-1][y2] - sum_list[x2][y1-1] + sum_list[x1-1][y1-1]  # 중복해서 빠지는 부분을 다시 더해줌
    print(result)