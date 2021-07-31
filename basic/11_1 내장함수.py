# 자주 사용되는 내장 함수

# sunm()
result = sum([1, 2, 3])
print(result)

# min(), max()
min_result = min(4, 3, 10, 2)
max_result = max(4, 3, 10, 2)
print(min_result, max_result)

# eval()
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4])
reversed_result = sorted([9,1, 8, 5, 4], reverse=True)
print(result)
print(reversed_result)

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)