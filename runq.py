import QType as pqt  # 문제 유형별로 문제를 푸는 함수들이 있는 모듈
import ReturnQuestionType as rqt  # 문제의 유형을 반환하는 함수가 있는 모듈


def runqq(count, datas):  # 문제를 풀고 결과를 출력하는 함수
    right = 0  # 맞힌 문제 수를 셀 변수 초기화
    for i in range(count):  # 원하는 문제 횟수만큼 반복
        Qtype = rqt.getQuestionType(datas[i])  # 현재 문제의 유형을 가져옴 (객관식, 단답형, OX)
        
        # 문제 유형에 따라 해당 함수 호출
        if Qtype == "객관식":  # 객관식 문제인 경우
            right += pqt.MultiChoice(i+1, datas[i])  # 객관식 문제 풀기 함수 호출, 정답 맞으면 1 증가
        elif Qtype == "단답형":  # 단답형 문제인 경우
            right += pqt.ShortAnswer(i+1, datas[i])  # 단답형 문제 풀기 함수 호출, 정답 맞으면 1 증가
        elif Qtype == "O, X":  # O, X 문제인 경우
            right += pqt.OX(i+1, datas[i])  # O, X 문제 풀기 함수 호출, 정답 맞으면 1 증가
        
        print('------------------------------------------')  # 각 문제 풀이 후 구분선 출력
        

    # 모든 문제 풀이 후 정답 수 및 정답률 출력
    print(f'{count}개의 문제 중 맞은 문제 수는 {right}개 입니다.')  # 맞은 문제 수 출력
    print(f'정답률은 {right/count:.2%}')  # 정답률 계산 및 출력 (소수점 2자리까지 표시)
    print('------------------------------------------')  # 구분선 출력
    
    return False  # 문제 풀이가 끝났으므로 종료 (추후 필요에 따라 반환 값 수정 가능)