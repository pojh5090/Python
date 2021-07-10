# 문자열은 큰 따옴표, 작은 따옴표로 선언할 수있다

data = 'Hello'
print(data)

data = "do you wanna build a \"Snow Man\"?"
print(data)


# 문자열 연산
# 문자열은 immutable 그래서 인덱스 값을 변경할 수 없다.

a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a * 3)

a = "ABCDE"
print(a[2 : 4])