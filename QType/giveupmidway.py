import main


def giveupmidway(UserAnswer):
    UserAnswer.upper()
    if (UserAnswer == "EXIT"): # EXIT를 입력받았을 시 재차 물어보는 이중 IF문
        print("현재까지 진행된 상황이 모두 초기화 됩니다 정말로 종료하시겠습니까?")
        cancle = input("종료를 취소하려면 C, 계속하려면 아무 키나 입력하세요.")
        
        if (cancle == "C"): # C입력시 실행문
            print("문제풀이를 종료하고 문제 선택화면으로 돌아갑니다.")
            main()
        else: # C를 제외한 아무 키나 입력시 화면으로 다시 돌아감.
            print("다시 문제풀이 화면으로 돌아갑니다.")

            
            

            




    

