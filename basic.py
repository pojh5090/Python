# 리스트
# 0 ~ 9 까지 출력해보자
a = [i for i in range(10)]
print(a)

# Q. 1 ~ 19 중에서 짝수만 출력
a = [i for i in range(1, 20) if i % 2 == 0]
print(a)

# ----- 일반 코드와 비교 ------ #
a = []
for i in range(1, 20):
    if i % 2 == 0:
        a.append(i)

print('normal: ', end = '')
print(a)


# Q. 1 ~ 9 까지 수들 중 제곱 값을 포함하는 리스트
a = [i*i for i in range(1, 10)]
print(a)
