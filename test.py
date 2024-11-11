import csv
import random
import os
import QType as pqt  # Print Question Type
import ReturnQuestionType as rqt  # Return Question Type

"""
**필드명**

Question : 문제
num : 문제번호
answer : 입력받은 정답

"""

# 폴더 경로 설정
folder_path = './workbook/'  # 폴더 경로를 실제 경로로 수정하세요.

# 폴더 안의 모든 .csv 파일을 가져오기
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# 파일이 있으면 목록을 출력하고 사용자로부터 선택 받기
if csv_files:
    print("CSV 파일 목록:")
    for idx, file in enumerate(csv_files, 1):
        print(f"{idx}. {file}")
    
    # 사용자로부터 선택 받기
    choice = int(input("원하는 파일의 번호를 입력하세요: "))
    
    if 1 <= choice <= len(csv_files):
        selected_file = csv_files[choice - 1]
        print(f"선택된 파일: {selected_file}")
        file_path = os.path.join(folder_path, selected_file)
    else:
        print("잘못된 선택입니다.")
        exit()  # 잘못된 선택이면 종료
else:
    print("CSV 파일이 없습니다.")
    exit()  # CSV 파일이 없으면 종료

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

# 데이터 섞기
random.shuffle(datas)

# 문제 풀기
count = int(input("몇 문제를 풀 것인지 정해주세요."))
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
