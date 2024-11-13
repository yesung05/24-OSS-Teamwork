import os

def readfile():
    # 폴더 경로 설정
    folder_path = './workbook/'  # 폴더 경로를 실제 경로로 수정하세요.

    # 폴더 안의 모든 .csv 파일을 가져오기
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # 파일이 있으면 목록을 출력하고 사용자로부터 선택 받기
    if csv_files:
        print('------------------------------------------')
        print("CSV 파일 목록:")
        for idx, file in enumerate(csv_files, 1):
            print(f"{idx}. {file}")
        
        # 사용자로부터 선택 받기
        choice = input("원하는 파일의 번호를 입력하세요(종료 : 'q'): ")
        if(choice.upper()=='Q'):
            print("종료합니다.")
            exit()
        else:
            choice = int(choice)
        if 1 <= choice <= len(csv_files):
            selected_file = csv_files[choice - 1]
            print(f"선택된 파일: {selected_file}")
            file_path = os.path.join(folder_path, selected_file)
            return file_path
        else:
            print("잘못된 선택입니다.")
            exit()  # 잘못된 선택이면 종료
    else:
        print("CSV 파일이 없습니다.")
        exit()  # CSV 파일이 없으면 종료