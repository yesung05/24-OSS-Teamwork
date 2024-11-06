import csv
# import pandas
import random 
import QType as pqt #Print Question Type
import ReturnQuestionType as rqt #Return Question Type

"""
**필드명**

Question : 문제
num : 문제번호
answer : 입력받은 정답

"""

# CSV 파일 경로 지정
file_path = 'ExampleQuestion.csv'

# 제목과 데이터를 담을 리스트 생성
headers = []
datas = []

# CSV 파일 읽기
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # 첫 번째 행은 제목으로 저장
    headers = next(reader)
    
    # 나머지 행은 데이터를 저장
    for row in reader:
        datas.append(row[:9])  # 첫 9개 열만 가져옴

# print("Headers:", headers)
# for data in datas:
#     print(data)

random.shuffle(datas)

count = int(input("몇 문제를 풀 것인지 정해주세요."))
print()
print('------------------------------------------')
print()
for i in range(count): #원하는 문제 횟수로 반복
    Qtype = rqt.getQuestionType(datas[i])
    # print(f"{i+1}. {Qtype} 형 문제입니다.")
    if(Qtype == "객관식"):
        pqt.MultiChoice(i+1,datas[i])
    elif(Qtype == "단답형"):
        pqt.ShortAnswer(i+1,datas[i])
    elif(Qtype == "O, X"):
        pqt.OX(i+1,datas[i])


