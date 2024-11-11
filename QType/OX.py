def OX(num,Question): # 단답형 문제 함수
    print(f"{num}. {Question[3]}")
    UserAnswer = input("정답(O, X): ")[0]
    UserAnswer = UserAnswer.upper()

    if(Question[2]==UserAnswer):
        print("정답입니다.")
    else:
        print("오답입니다.")
        print(f"정답은 {Question[2]}입니다.")