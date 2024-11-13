def OX(num, Question):  # 단답형 문제 함수 (O, X 문제)
    while(True):
        print(f"{num}. {Question[3]}")  # 문제 출력 (문제 리스트에서 4번째 항목)
        
        # 사용자로부터 O 또는 X 입력 받기 (첫 글자만 사용)
        UserAnswer = input("정답(O, X): ")[0]  # 첫 번째 문자만 가져오기
        UserAnswer = UserAnswer.upper()  # 입력된 문자를 대문자로 변환 (O 또는 X만 입력 받기 위해)
        if(UserAnswer is not 'O' or UserAnswer is not 'X'):
            print("잘못된 입력입니다. O, X중에 선택해주세요.")
            continue
        # 정답 확인
        if(Question[2] == UserAnswer):  # 정답이 맞으면
            print("정답입니다.")  # 정답 출력
            return 1  # 정답이면 1 반환
        elif(Question[2] is not UserAnswer):  # 정답이 틀리면
            print("오답입니다.")  # 오답 출력
            print(f"정답은 {Question[2]}입니다.")  # 정답 출력
            return 0  # 오답이면 0 반환
        else:
            break
