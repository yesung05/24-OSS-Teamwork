import csv
def printChoiceQ(num,Question):
    print(f"{num}. {Question[3]}")
    for i in range(5):
        print(f"\t({i+1}){Question[4+i]}")
    anwser = int(input("정답: "))
    anwser -= 1
    if(Question[4+anwser]==Question[2]):
        print("정답입니다.")
    else:
        print("오답입니다.")
        print(f"정답은 {Question[4:].index(Question[2])+1}입니다.")




def getQuestionType(type):
    typev = int(type[1])
    match typev:
        case 1:
            return "객관식"
        case 2:
            return "단답형"
        case 3:
            return "O, X"


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

print("Headers:", headers)
for data in datas:
    print(data)

count = int(input("몇 문재를 풀 것인지 정해주세요."))

for i in range(count):
    Qtype = getQuestionType(datas[i])
    print(f"{i+1}. {Qtype} 형 문제입니다.")
    if(Qtype == "객관식"):
        printChoiceQ(i,datas[i])
    elif(Qtype == "단답형"):
        print('단답형')
    elif(Qtype == "O, X"):
        print('OX')

# print(getQuestionType(datas[0]))



