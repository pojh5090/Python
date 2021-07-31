# Counter
# 등장 횟수를 세는 기능을 제공

from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])    # 3
print(counter['green'])   # 1
print(dict(counter))      # 사전 자료형으로 반환 



# math 라이브러리
import math

# 최소 공배수(LCM)를 구하는 함수
# def lcm(a, b):
#     return a * b   

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수 GCD 계산
print(math.lcm(21, 14))      # 최소 공배수 LCM 계산