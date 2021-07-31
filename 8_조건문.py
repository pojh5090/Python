# 1. 기본 형태

x = 15

if x >= 10:
    print("x >= 10")

if x >= 0:
    print("x >= 0")

if x >= 30:
    print("x >= 30")


# 주의점 : 코드의 블록을 들여쓰기로 지정한다.


# 2. 예제
## Q. 점수에 따른 메시지 출력하기
score = 85

if(score >= 75):
    print("75점 이상입니다.")
    if(score >= 90):
        print("90점 이상입니다.")
else:
    print("분발하세요.")    

print("프로그램을 종료합니다.")    

# if ~ elif ~ else 로 사용


# 3. 참. 거짓
# a and b -> a, b 모두 참일 때
# a or b -> a, b 중에 하나만 참이여도 참
# not a -> a가 거짓일 때 참
a = 15
if(a <= 20 and a >= 0):
    print("Yes!")


# 4. in 연산자
# in 연산자와 not in 연산자
# 리스트, 튜플, 문자열, 딕셔너리에서 모두 사용 가능하다
# x in 리스트 : 리스트 안에 x가 들어가 있을 때 True
# x not in 문자열 : 문자열 안에 x가 들어가 있지 않을 때 True


# 5. pass 키워드
# 아무것도 처리하고 싶지 않을 때 pass 키워드를 사용
# 디버깅 과정에서 일단 조건문의 형태만 만들어 놓는 것.
score = 85

if score >= 80:
    pass   #-------> 나중에 작성할 코드 !
else:
    print('성적이 80점 미만입니다')

print('프로그램을 종료합니다.')


# 6. 부등식 그대로 사용 가능
# if 0 < x < 20:  이렇게!
