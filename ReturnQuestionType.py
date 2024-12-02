def getQuestionType(type):  # 문제 유형을 반환하는 함수
    typev = int(type[1])  # 문제 유형을 나타내는 두 번째 항목을 정수로 변환
    
    # 문제 유형에 따라 반환할 값을 결정
    match typev:  # typev 값에 맞춰서 분기
        case 1:  # typev 값이 1일 경우
            return "객관식"  # "객관식" 문제 유형 반환
        case 2:  # typev 값이 2일 경우
            return "단답형"  # "단답형" 문제 유형 반환
        case 3:  # typev 값이 3일 경우
            return "O, X"  # "O, X" 문제 유형 반환
