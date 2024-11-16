import os  # 운영체제 관련 기능을 제공하는 모듈 (파일 및 폴더 처리)

def readfile():  # 파일을 선택하는 함수
    # 폴더 경로 설정
    folder_path = './workbook/'  # CSV 파일이 들어있는 폴더 경로 (경로 수정 필요)

    # 폴더 안의 모든 .csv 파일을 가져오기
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]  # 폴더 내의 .csv 파일 목록 추출

    # 파일이 있으면 목록을 출력하고 사용자로부터 선택 받기
    if csv_files:  # CSV 파일이 하나 이상 있으면
        print('------------------------------------------')
        print("CSV 파일 목록")  # 파일 목록 출력
        for idx, file in enumerate(csv_files, 1):  # 파일 목록을 출력 (1부터 인덱스 시작)
            print(f"{idx}. {file}")  # 파일 이름 출력
        
        # 사용자로부터 선택 받기
        choice = input("원하는 파일의 번호를 입력하세요(종료 : 'q'): ")  # 사용자에게 파일 선택을 받음
        if(choice.upper() == 'Q'):  # 사용자가 'q'를 입력하면 종료
            print("종료합니다.")
            exit()  # 프로그램 종료
        else:
            choice = int(choice)  # 사용자가 선택한 번호를 정수로 변환
        
        # 선택이 유효한 경우
        if 1 <= choice <= len(csv_files):  # 선택한 번호가 파일 목록에 있는 경우
            selected_file = csv_files[choice - 1]  # 선택한 파일 이름
            print(f"선택된 파일: {selected_file}")  # 선택된 파일 출력
            file_path = os.path.join(folder_path, selected_file)  # 파일 경로 생성
            return file_path  # 선택된 파일 경로 반환
        else:
            print("잘못된 선택입니다.")  # 잘못된 번호 입력 시
            exit()  # 종료
    else:
        print("CSV 파일이 없습니다.")  # 폴더 내에 CSV 파일이 없으면
        exit()  # 종료
