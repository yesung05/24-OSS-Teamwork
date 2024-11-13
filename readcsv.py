import csv  # CSV 파일을 읽고 쓰는 기능을 제공하는 모듈

def readcsv(file_path):  # 주어진 경로의 CSV 파일을 읽어 데이터를 반환하는 함수
    headers = []  # CSV 파일의 첫 번째 행(제목)을 저장할 리스트
    datas = []  # CSV 파일의 나머지 데이터를 저장할 리스트

    # CSV 파일 열기 (읽기 모드, UTF-8 인코딩)
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)  # CSV 파일을 읽기 위한 객체 생성
        
        # 첫 번째 행은 제목(헤더)로 읽어 headers 리스트에 저장
        headers = next(reader)
        
        # 나머지 행들은 데이터로 읽어 datas 리스트에 저장
        for row in reader:
            datas.append(row[:9])  # 각 행에서 첫 9개의 열만 가져와 datas에 추가
    
    return datas  # 읽어들인 데이터를 반환
