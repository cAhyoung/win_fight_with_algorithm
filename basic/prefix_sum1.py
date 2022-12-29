#백준 온라인 저지 11659, 시간제한 0.5초, 난이도 실버 III
import sys
input = sys.stdin.readline

n, q = map(int, input().split())  # arr의 갯수와 몇개의 구간을 입력받을지 정하는 변수
arr = list(map(int, input().split()))  # 주어지는 arr

prefix_sum = 0  # 첫번째부터 각 구간별 합을 구할 때 이용할 변수
prefix_arr = []  # 첫번째부터 각 구간별 합을 담을 빈 리스트

for i in arr:  # 첫번째 부터 각 구간을 담는 과정
    prefix_sum += i
    prefix_arr.append(prefix_sum)

for i in range(q):  # 주어진 구간의 구간 합을 구하는 과정
    j, k = map(int, input().split())  # 주어진 구간

    if j > k:  # 주어지는 구간이 제각각일 수 있기 때문에 조건별로 생각해야 함
        if k-2 < 0:  # k가 음수가 되는 경우 리스트의 뒤로 돌아가지 않도록 하기 위해 조건문 이용
            print(prefix_arr[j-1] - 0)
        else:
            print(prefix_arr[j-1] - prefix_arr[k-2])
    elif j < k:
        if j-2 < 0:  # 마찬가지로 j가 음수가 되는 경우 리스트의 뒤로 돌아가지 않도록 하기 위해 조건문 사용
            print(prefix_arr[k-1] - 0)
        else:
            print(prefix_arr[k-1] - prefix_arr[j-2])
    else:
        print(arr[j-1])

    # print(prefix_arr[j] - prefix_arr[k-1])  -> 해당 코드만 이용하는 경우 제대로 답이 나오지 않음