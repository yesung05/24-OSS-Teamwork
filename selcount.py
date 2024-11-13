def selcount(datas):
    sel = True
    while(sel):
        print('------------------------------------------')
        print(f"선택된 문제집에 등록된 문제의 수가 {len(datas)}개입니다.")
        count = input("몇 문제를 풀 것인지 정해주세요. (다시 선택하시려면 'q'를 입력해주세요.): ")
        if(count == 'q'): 
            return False
            
        else:
            count = int(count)

        if(count > len(datas)): # 만약 입력한 문제 수가 문제집 문제 수를 초과하면 (수정 예정)
            print(f"{len(datas)}개의 이하의 값을 입력해주세요.")
            print('------------------------------------------')
            continue
        sel = False
    return int(count)