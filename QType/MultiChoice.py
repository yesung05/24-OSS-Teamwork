import random

def MultiChoice(num,Question): #객관식 문제 출력
    Answer = Question[2]
    options = Question[4:9] 
    random.shuffle(options)
    if Answer not in options:
        print("이 문제는 잘못된 문제입니다.")
        print("Exiting...")
        return
    
    print(f"{num}. {Question[3]}") #문제 출력
     #보기 랜덤하게 섞음
    
    # 섞인 보기 출력

    for i, option in enumerate(options):
        print(f"\t({i+1}){option}")
    UserAnswer = input("정답: ")
    if UserAnswer.isdigit():
        UserAnswer = int(UserAnswer)
        UserAnswer -= 1
        Check = options[UserAnswer] == Answer 
    else:
        UserAnswer = UserAnswer.replace(" ","")
        answerNoSpace = Answer.replace(" ","")
        Check =  (UserAnswer == answerNoSpace) # 두 값이 같으면 true, 아니면 False

    if(Check): #선택한 보기랑 정답에 값이 같으면
        print("정답입니다.")
    else:
        print("오답입니다.")
        print(f"정답은 {options.index(Question[2])+1}번 입니다.") #정답 번호 출력