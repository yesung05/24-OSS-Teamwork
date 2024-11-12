import random
import QType as pqt  # Print Question Type
import ReturnQuestionType as rqt  # Return Question Type
import readfile
import readcsv
"""
**필드명**

Question : 문제
num : 문제번호
answer : 입력받은 정답

"""

file_path = readfile.readfile()
datas = readcsv.readcsv(file_path)

# 데이터 섞기
random.shuffle(datas)

sel = True
# 문제 풀기
while(sel):
    print(f"선택된 문제집에 등록된 문제의 수가 {len(datas)}개입니다.")
    count = int(input("몇 문제를 풀 것인지 정해주세요."))
    if(count > len(datas)): # 만약 입력한 문제 수가 문제집 문제 수를 초과하면 (수정 예정)
        print(f"{len(datas)}개의 이하의 값을 입력해주세요.")
        continue

    sel = False
print()
print('------------------------------------------')
print()

for i in range(count):  # 원하는 문제 횟수로 반복

    Qtype = rqt.getQuestionType(datas[i])
    if Qtype == "객관식":
        pqt.MultiChoice(i+1, datas[i])
    elif Qtype == "단답형":
        pqt.ShortAnswer(i+1, datas[i])
    elif Qtype == "O, X":
        pqt.OX(i+1, datas[i])
    print("------------------------------------------")

input()