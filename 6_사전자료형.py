# 사전 자료형은 키(Key)와 값(Value)의 쌍을 데이터로 가지는 자료형

## 예시
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("사과는 존재합니다.")


# 키 데이터만 뽑자 : keys()
# 값 데이터만 뽑자 : values()

# 키, 값만 각각 담은 리스트
data_keys = data.keys()

print(data.keys())
print(data.values())   #--> 반환은 리스트로 반환됨

# 키에 따른 '값'을 하나씩 출력
for key in data_keys:
    print(data[key])