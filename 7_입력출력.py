# input() : 한 줄의 문자열을 입력받음
# map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용


# ex1. 공백 기준으로 구분된 데이터를 입력 받을 때 사용
#list(map(int, input().split()))

# ex2. 공백 기준으로 구분된 데이터의 개수가 많지 않을 때 사용
#a, b, c = map(int, input().split())  무조건 3개만 들어온다 !


# 문자열 형태로 한 줄 그대로 똑같이 출력됨
data = input()
print(data)

# 공백기준으로 출력해보기 (리스트로 반환, 각 데이터는 문자열type)
data = input().split()  # 10 20 30 40
print(data)             # ['10', '20', '30', '40']


# int로 형변환 + list 로
data = list(map(int, input().split()))  # 10 20 30 40
print(data)                             # [10, 20, 30, 40]


## 빠르게 입력받기 !
import sys
data = sys.stdin.readline().rstrip()
print(data)


## f-string
# 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있음
answer = 7
print(f"정답은 {answer}입니다.")