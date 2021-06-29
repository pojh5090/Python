import sys
import re
import os
import operator

################################################################################
# 환경변수 (사용자가 입력하는)
################################################################################

FILE_PATH = "C:/dev/song.txt"

## 단어를 찾을때 대소문자를 구분하는지 (구분하면 True, 구분하지 않으면 False)
CASE_SENSITIVE = False

################################################################################
# 환경변수체크
################################################################################

if not os.path.exists(FILE_PATH):
    print("환경변수에 설정한 '텍스트 파일경로'를 찾을 수 없습니다.(" + FILE_PATH + ")")
    sys.exit(0)

if "CASE_SENSITIVE" not in globals():
    print("환경변수에서 CASE_SENSITIVE(대소문자구분)이 설정되지 않았습니다.")
    sys.exit(0)

################################################################################
# 글로벌 변수 
################################################################################

# 단어가 들어가는 배열idx
IDX_WORD=0

# 빈도수가 들어가는 배열idx
IDX_CNT=1

################################################################################
# 서브함수 (fn_check)
################################################################################

def fn_check(dictionary, target):
    if target != None:
        if not CASE_SENSITIVE :
            target = target.lower()  # 소문자로
        target = re.sub('[^A-Za-z0-9]+', '', target)  # 영어대문자, 영어소문자, 숫자만 남김

    if target == None or target == '':
        return

    found=False

    for word in dictionary:
        if word[IDX_WORD] == target: ## word[0]번째에는 단어가
            word[IDX_CNT] = word[IDX_CNT]+1 ## word[1]에는 빈도수가 들어감
            found=True
            break

    if not found:
        word=[ {} for x in range(max(IDX_WORD, IDX_CNT)+1) ] ## 동적으로 리스트를 설정한다.
        word[IDX_WORD]=target
        word[IDX_CNT]=1        
        dictionary.append(word) # 찾지못하면 단어와 빈도수(1)를 추가함

################################################################################
# 메인로직 (main)
################################################################################

dictionary = [] # 딕션너리를 사용하지 않음(중괄호 {}를 사용하지 않았음!!)

try:
    f = open(FILE_PATH, 'r')
except FileNotFoundError:
    print("파일경로를 찾을수 없습니다.(" + FILE_PATH + ")")
    sys.exit(0)

while True:
    line = f.readline()
    if not line: break

    splits = line.split(" ")
    for split in splits:
        fn_check(dictionary, split)

f.close()


for word in dictionary:
    print("%s : %d" % (word[IDX_WORD], word[IDX_CNT]))