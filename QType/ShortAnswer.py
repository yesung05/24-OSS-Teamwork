!import QType.giveupmidway as gum

def ShortAnswer(num, Question):  # 단답형 문제 함수 (자유 형식 답변)
    print(f"{num}. {Question[3]}")  # 문제 출력 (문제 리스트에서 4번째 항목)
    
    # 사용자로부터 정답 입력 받기 (공백 제거 및 소문자 변환)
    UserAnswer = input("정답: ") # 사용자 입력받기
    !gum(UserAnswer)
    UserAnswer = input("정답: ").replace(" ", "").lower()  # 사용자 입력값에서 공백 제거하고 소문자로 변환
    # 정답도 공백 제거하고 소문자로 변환
    Answer = Question[2].replace(" ", "").lower()  # 문제 리스트에서 3번째 항목을 정답으로 사용하고 공백 제거 및 소문자 변환
    
    # 정답 확인
    if(Answer == UserAnswer):  # 정답이 맞으면
        print("정답입니다.")  # 정답 출력
        return 1  # 정답이면 1 반환
    else:  # 정답이 틀리면
        print("오답입니다.")  # 오답 출력
        print(f"정답은 {Question[2]}입니다.")  # 정답 출력
        return 0  # 오답이면 0 반환
    