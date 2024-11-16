def askonemore():  # 추가 문제를 풀지 여부를 묻는 함수
    resume = input("계속 하시겠습니까? (O,X): ")  # 사용자에게 문제를 계속 풀지 여부를 입력받음
    resume = resume.upper()  # 입력받은 문자열을 대문자로 변환 (대소문자 구분 없이 처리)
    
    if(resume == 'O'):  # 사용자가 'O'를 입력한 경우
        return True  # 문제를 계속 풀겠다고 응답했으므로 True 반환
    else:  # 'O'가 아닌 값을 입력한 경우 (예: 'X')
        return False  # 문제를 더 이상 풀지 않겠다고 응답했으므로 False 반환
