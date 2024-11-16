import random
!import QType.giveupmidway as gum

def MultiChoice(num, Question):  # 객관식 문제 출력 함수
    while(True):
        Answer = Question[2]  # 정답은 문제 리스트의 3번째 항목
        options = Question[4:9]  # 보기 항목들은 문제 리스트의 5~9번째 항목들
        random.shuffle(options)  # 보기를 랜덤하게 섞음
        
        # 정답이 보기에 포함되어 있지 않으면 문제에 오류가 있다고 판단하고 종료
        if Answer not in options:
            print("이 문제는 잘못된 문제입니다.")
            print("Exiting...")
            return
    
        print(f"{num}. {Question[3]}")  # 문제 내용 출력 (문제 리스트에서 4번째 항목)
        
        # 섞인 보기들 출력
        for i, option in enumerate(options):  # 보기를 하나씩 출력
            print(f"\t({i+1}){option}")  # 보기 번호와 해당 보기 출력
        
        # 사용자에게 정답 입력 받기
        UserAnswer = input("정답: ")  # 사용자 입력 받기
        !gum(UserAnswer) # 사용자 입력을 받은 결과를 중도포기함수에 전달
        if UserAnswer.isdigit():  # 입력이 숫자일 경우 (보기를 숫자로 선택한 경우)
            UserAnswer = int(UserAnswer)  # 입력값을 정수로 변환
            UserAnswer -= 1  # 사용자 선택 번호는 0부터 시작하기 때문에 1을 빼서 인덱스 맞추기
            if(UserAnswer not in range(5)):
                print("잘못된 범위 값입니다. 1에서 5사이의 숫자를 입력해주세요.")
                continue
            Check = options[UserAnswer] == Answer  # 선택한 보기가 정답과 일치하는지 확인
            
        else:  # 입력이 문자열일 경우 (보기를 문자열로 입력한 경우)
            UserAnswer = UserAnswer.replace(" ", "").lower()  # 공백 제거하고 소문자로 변환
            answerNoSpace = Answer.replace(" ", "").lower()  # 정답도 공백 제거하고 소문자로 변환
            Check = (UserAnswer == answerNoSpace)  # 두 값이 같으면 True, 아니면 False

        # 정답 여부에 따라 출력
        if Check:  # 정답인 경우
            print("정답입니다.")
            return 1  # 정답이면 1을 반환
        else:  # 오답인 경우
            print("오답입니다.")
            print(f"정답은 {options.index(Question[2])+1}번 입니다.")  # 정답 번호 출력
            return 0  # 오답이면 0을 반환
