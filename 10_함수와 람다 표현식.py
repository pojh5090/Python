# 1. 함수의 형태
# def 함수명(매개변수) :
#   실행할 소스코드
#   return 반환 값

# 예시1
def add(a, b):
    return a + b

print(add(3, 7))


# 예시2
def add(a, b):
    print('함수의 결과 : ', a+b)

add(3,5)


# 파라미터를 직접 지정할 수도 있다.
# ex. add(b = 5, a = 3)


# 함수 바깥의 변수를 사용하고자 한다면 (전역변수 처럼)
# 'global' 키워드를 사용하자!
a = 10

def func():
    global a
    a += 1

func()
# 1) 그냥 출력하는 건 global 붙이지 않아도 됨
# 2) 리스트형은 global 안써도 print 외의 다른 메소드 사용 가능
# 3) 만약 함수 내부, 외부 같은 이름의 변수를 쓴다면 내부의 변수 우선순위가 높다.



# 2. 여러개의 반환 값
# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다.
def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var #-> packing 하다

a, b, c, d = operator(7, 3)  #-> unpacking 하다
print(a, b, c, d)




# 3. 람다 표현식
# 람다 표현식을 사용하면 함수를 간단하게 작성 가능
# ex ) print((lambda a, b: a + b)(3, 7))

# 내장 함수에서 자주 사용된다.
# ex )
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1] #두번째 요소를 리턴.

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x : x[1]))
### sorted(정렬할 데이터, key 파라미터) 
### key 파라미터는 어떤 것을 기준으로 정렬할 것인가? 
### sorted(~~, key=무엇) --> 해당 키를 기준으로 정렬하여 반환.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
print(list(result))   #결과 : [7, 9, 11, 13,15]
