# Basic
Do it! 코딩테스트 - 기초편의 문제들을 풀며 작성한 코드들을 업로드합니다. 
<hr>

### First Chapter, Data Structure

1. Array and List
   * Array
     - 메모리의 연속 공간에 값이 채워져있는 형태의 자료구조. 배열의 값은 인덱스를 통해 참조할 수 있으며, 선언한 자료형의 값만 저장할 수 있음.
   * Array characteristic
     - 인덱스를 사용하여 바로 값에 접근할 수 있음
     - 새로운 값을 삽입하거나 특정 인덱스에 있는 값을 삭제하기 어려움
       + 삭제를 원하는 경우 해당 인덱스 주변에 있는 값들을 움직여야 함
     - 구조가 간단하여 코테에서 많이 사용
   * List
     - 노드를 포인터로 연결한 자료구조
       - 노드는 값과 포인터가 묶여있음
   * List Characteristic
     - 인덱스가 없어 값에 접근하기 위해서는 Head 포인터부터 순서대로 접근해야 함
       - 속도가 느림
     - 포인터로 연결되어있어 데이터를 삽입, 삭제하는 연산 속도는 빠름
     - 선언할 때 크기를 별도로 지정하지 않아도 됨
       - 크기가 변하기 쉬운 데이터를 다룰 때 적절함
     - 포인터를 저장할 공간이 필요하므로 배열보다 구조가 복잡함


    ```python
    
    # Do it! 알고리즘 코딩테스트 파이썬편
    # 35p, 1번문제, 숫자의 합 구하기
    ## 정답 풀이
    n = input()  # 확인만 하는 용도로 받기 때문에 정수형 변환 상관 X
    numbers = list(input())  # 모두 붙어있는 형태로 입력을 받아도 리스트로 변환이 가능
    sum = 0  # 각 숫자들을 모두 더해줄 변수
        
    for i in numbers:
      sum = sum + int(i)  # 리스트에 들어가있는 숫자들은 정수형이 아니기 때문에 형변환 
        
    print(sum)
    ```


    ```python
    # Do it! 알고리즘 코딩테스트 파이썬편
    # 38p, 2번문제, 평균 구하기
    ## 정답 풀이
    n = input()
    mylist = list(map(int, input().split()))  # map 함수를 이용해 형변환을 좀 더 쉽게
    # (A/max*100 + B/max*100 + C/max*100)/3 = ((A+B+C)/max*100)/3  -> 해당 풀이를 이용해 더 단순화
    mymax = max(mylist)
    sum = sum(mylist)
    
    print(sum*100/mymax/int(n))
    ```
2. Prefix Sum
   * 구간합
     - 합 배열을 이용해 시간 복잡도를 더 줄이기 위해 사용하는 특수한 목적의 알고리즘
   * 구간 합의 핵심 이론
     - 합배열 S[i] = A[1] + A[2] + ... A[i]
     - 위의 식을 통해 S[i] = s[i-1] + A[i] 임을 알 수 있음
     - 기존 리스트의 일정범위 합을 구하는 시간 복잡도가 O(N)에서 O(1)로 줄어듬
     - 만약 i~j까지의 구간 합을 원한다면?
       - S[j] - S[i-1]


     ```python
      # Do it! 알고리즘 코딩테스트 파이썬편
      # 43p, 3번문제, 부분 합 구하기
      ## 정답풀이
      import sys
      input = sys.stdin.readline
      suNo, quizNo = map(int, input().split())
      numbers = list(map(int, input().split()))
      prefix_sum = [0]  # 0부터 시작함으로써 리스트 뒤로 돌아가는 경우가 발생해도 괜찮게 해줌
      temp = 0
      
      for i in numbers:
        temp = temp + i
        prefix_sum.append(temp)
      for i in range(quizNo):
        s, e = map(int, input().split())
        print(prefix_sum[e] - prefix_sum[s-1])
      
     ```