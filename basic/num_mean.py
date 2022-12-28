# 백준 온라인 저지 1546, 시간제한 2초, 난이도 브론즈 I
# 점수/최대점수*100
# 있는 그대로의 풀이방식 1
n = input('과목 수를 입력하시오: ')
score = list(map(int, input('시험 성적을 입력하시오: ').split()))

new_score = []  # 변경된 점수를 담을 빈 리스트
new_tot = 0  # 평균값을 계산하는데 사용될 변수

for i in score:
    new_score.append(i/max(score)*100)  # score에 있는 요소들을 하나씩 꺼내 새로이 계산해줌

for i in new_score:
    new_tot += i  # new_tot에 모두 더한 후

print(new_tot/n)  # 평균값 산출

# 풀이 방식 1 줄여보기
# 과목 수가 3개 주어진다면?
## (A/max*100 + B/max*100 + C/max*100)/3 = ((A+B+C)/max*100)/3  -> 해당 풀이를 이용해 더 단순화
n2 = int(input('과목 수를 입력하시오: '))
score2 = list(map(int, input('시험 성적을 입력하시오: ').split()))
new_mean2 = (sum(score2)/max(score2)*100)/n2

print(new_mean2)