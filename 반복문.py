# while문
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1
print(result)


# 1부터 9까지 홀수의 합 구하기
i = 1
result = 0
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)



# for문
# for 변수 in 리스트:
#   실행할 소스코드
# in 뒤에 오는 데이터(리스트, 튜플 등)

array = [9, 8, 7, 6, 5]
for x in array:
    print(x)

# range() 함수!
# range(시작 값, 끝 값 + 1) 형태
# 인자 하나만 넣으면 자동으로 시작 값은 0이 됨!

result = 0
for i in range(1, 10):
    result += i
#--> 이건 1 ~ 9까지 값의 합
print(result)


# continue : 해당 코드 넘어가고 다음 반복문 실행
# break : 반복문 즉시 탈출



# range 사용 예제
scores = [90, 85, 77, 65, 97]
for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")


# 특정 번호의 학생은 제외하기
scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(i+1 ,"번 학생은 합격입니다.")



# 이중 for문
# 구구단 예제
for i in range(2, 10):
    for j in range(1, 10):
        print(i , " X ", j, " = ", i * j)
    print()
