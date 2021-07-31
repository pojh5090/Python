# 리스트 관련 메서드 #
# append() - 변수명.append() : 리스트에 원소를 하나 삽입할 때 사용
# sort() - 변수명.sort() : 기본 정렬 기능으로 오름차순으로 정렬
# sort() - 변수명.sort(reverse = True) : 내림차순으로 정렬
# reverse() - 변수명.reverse() : 리스트의 원소의 순서를 모두 뒤집어 놓음
# insert() - insert(삽입 위치인덱스, 삽입 값) : 특정 인덱스 위치에 원소를 삽입할 때 사용
# count() - 변수명.count(특정 값) : 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용
# remove() - 변수명.remove(특정 값) : 특정한 값을 갖는 원소를 제거하는데,값을 가진 원소가 여러개면 하나만 제거함

# Q.리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5]
remove_set = {3, 5}

#remove_set에 포함되지 않는 값들만 저장
result = [i for i in a if i not in remove_set]
print(result)