def ShortAnswer(num,Question): # 단답형 문제 함수
    print(f"{num}. {Question[3]}")
    UserAnwser = input("정답: ").replace(" ","").lower()
    Anwser = Question[2].replace(" ","").lower()
    if(Anwser==UserAnwser):
        print("정답입니다.")
    else:
        print("오답입니다.")
        print(f"정답은 {Question[2]}입니다.")