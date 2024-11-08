import csv

def readcsv(file_path):
    headers = []
    datas = []

    # CSV 파일 읽기
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        # 첫 번째 행은 제목으로 저장
        headers = next(reader)
        
        # 나머지 행은 데이터를 저장
        for row in reader:
            datas.append(row[:9])  # 첫 9개 열만 가져옴
    
    return datas