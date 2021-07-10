# n x m 의 2차원 배열 선언
n = 4
m = 3

array = [[0] * m for _ in range(n)]
print(array)

# 반복문을 수행 할 때 변수의 값이 필요 없을 때 '언더바' 사용
for _ in range(1, 9):
    print("hi")
