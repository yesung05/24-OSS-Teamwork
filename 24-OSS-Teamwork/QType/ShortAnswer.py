def ShortAnswer(num,Question): # 단답형 문제 함수
    print(f"{num}. {Question[3]}")
    answer = input("정답: ")
    if(Question[2]==answer):
        print("정답입니다.")
    else:
        print("오답입니다.")
        print(f"정답은 {Question[2]}입니다.")