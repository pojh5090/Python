# 순열과 조합


# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
from itertools import combinations, permutations
data = ['A', 'B', 'C']  #데이터 준비
result = list(permutations(data, 3))  #모든 순열 구하기
print(result)


# 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
# A, B, C에서 순서를 고려하지 않고 두 개를 뽑는 경우: 'AB', 'BC', 'AC'
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)


# 중복 순열과 중복 조합
# 중복 순열 -> product
# 중복 조합 -> combinations_with_replacement
from itertools import product 
data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

from itertools import combinations_with_replacement 
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)