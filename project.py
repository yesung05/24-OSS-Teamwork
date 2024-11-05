import csv
import random

def printChoiceQ(num, Question):  # 객관식 문제 출력
    print(f"{num+1}. {Question[3]}")  # 문제 출력
    options = Question[4:9]
    random.shuffle(options)  # 보기 랜덤하게 섞음
    print(options)
    print(Question[2])
    # 섞인 보기 출력
    for i, option in enumerate(options):
        print(f"\t({i+1}) {option}")
    
    # 사용자 입력 (1~5 사이의 숫자만 입력받도록)
    while True:
        try:
            answer = int(input("정답(1~5): "))
            if 1 <= answer <= 5:
                break
            else:
                print("1부터 5 사이의 숫자만 입력해주세요.")
        except ValueError:
            print("잘못된 입력입니다. 1부터 5 사이의 숫자를 입력해주세요.")
    
    answer -= 1  # 1부터 시작하는 번호를 0부터 시작하는 인덱스로 변환
    
    if str(options[answer]) == str(Question[2]):  # 선택한 보기랑 정답에 값이 같으면
        print("정답입니다.")
    else:
        print("오답입니다.")
        print(f"정답은 {(options.index(Question[2]))+1}번 입니다.")  # 정답 번호 출력

def printTypeQ(num, Question):  # 주관식 문제 출력
    print(f"{num+1}. {Question[3]}")
    answer = input("정답을 입력하세요: ")
    if answer == Question[2]:
        print("정답입니다.")
    else:
        print(f"오답입니다. 정답은 {Question[2]} 입니다.")

def getQuestionType(type):  # 문제 유형 반환
    typev = int(type[1])
    match typev:
        case 1:
            return "객관식"
        case 2:
            return "단답형"
        case 3:
            return "O, X"
        case _:
            return "알 수 없음"  # 예외 처리 추가

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

# 문제 개수 입력 받기
count = int(input("몇 문제를 풀 것인지 정해주세요: "))

# 문제 출력
for i in range(count):  # 원하는 문제 횟수로 반복
    Qtype = getQuestionType(datas[i])
    print(f"{i+1}. {Qtype} 형 문제입니다.")
    if Qtype == "객관식":
        printChoiceQ(i, datas[i])
    elif Qtype == "단답형":
        printTypeQ(i, datas[i])
    elif Qtype == "O, X":
        print("OX 문제는 아직 구현되지 않았습니다.")

print("")