import random  # 무작위로 항목을 섞는 데 사용되는 모듈
import readfile  # 파일 읽기 함수가 포함된 모듈
import readcsv  # CSV 파일 읽기 함수가 포함된 모듈
import runq  # 문제를 풀고 결과를 출력하는 모듈
import onemore  # 추가 문제를 풀지 여부를 묻는 함수가 포함된 모듈
import selcount as ct  # 문제 수를 선택하거나 설정하는 모듈

"""
**필드명**

Question : 문제
num : 문제번호
answer : 입력받은 정답
"""

print()  # 빈 줄 출력
print('------------------------------------------')  # 구분선 출력
print()  # 빈 줄 출력

conti = True  # 문제 풀이를 계속할지 여부를 나타내는 변수
while (conti):  # 문제가 끝날 때까지 반복
    # 파일 경로 읽기
    file_path = readfile.readfile()  # 문제 파일 경로를 읽는 함수 호출
    datas = readcsv.readcsv(file_path)  # 읽은 파일 경로로 CSV 데이터를 읽어옴

    # 문제 목록을 랜덤하게 섞기
    random.shuffle(datas)  # 문제들을 무작위로 섞음
    
    # 문제의 개수를 선택하거나 설정하는 함수 호출
    val = ct.selcount(datas)  # 문제의 개수를 설정하거나 선택하는 함수
    if (val == False):  # 만약 문제 개수가 올바르게 설정되지 않았다면
        continue  # 문제 개수를 다시 설정하도록 계속해서 반복
    else:
        count = val  # 선택된 문제 개수를 변수에 저장
    
    # 문제 풀기 실행
    running = runq.runqq(count, datas)  # 문제를 풀고 결과를 반환하는 함수 호출
    if (not running):  # 문제가 다 풀린 후
        if (not onemore.askonemore()):  # 추가 문제를 풀지 여부를 묻는 함수 호출
            break  # 더 이상 풀지 않으면 반복을 종료
