# 문제은행 프로그램

 - .csv로 이루어진 문제 파일을 선택하여 해당 문제 파일에서 문제를 랜덤으로 선택하여 풀 수 있는 콘솔 프로그램입니다.
 - 독학등 개인 공부에 유용하게 사용할 수 있습니다.

## 📜 Description

- 사용자로부터 파일 경로에 있는 문제집 중 하나 선택
- 문제를 무작위로 섞어 사용자가 풀 문제를 랜덤하게 배정
- 사용자에게 문제의 개수를 선택하게 하고, 설정된 개수만큼 문제를 풀도록 유도
- 문제를 풀고 난 후, 맞춘 문제 수를 출력
- 문제 풀이가 끝난 후 추가 문제를 풀지 여부를 묻고, 선택에 따라 계속 문제를 풀거나 종료

## 🛠️ Tools

- **Python**: 
- **모듈**:
  - `random`: 문제를 무작위로 섞기 위해 사용
  - `os`: 파일 경로 관련 작업을 처리

## 💻 Question Type
 - 객관식
 - 단답형
 - O, X

## 👥 Teammate

- 조예성 [@yesung05](https://www.github.com/yesung05)
- 황용범 [@bengaldr0gon](https://www.github.com/bengaldr0gon)
- 석지환 [@AJihwan](https://www.github.com/AJihwan)
- 이윤석 [@leeyunseok110](https://www.github.com/leeyunseok110)
- 함정원 [@jwon0117](https://www.github.com/jwon0117)

## .exe 파일 생성하기
- pyinstaller 설치  
```
pip install pyinstaller
```  
- onefile로 .exe 생성  
```
pyinstaller -F main.py
```  

## Git Bash 도움말
- github 저장소 로컬에 복제하기  
```
git clone https://github.com/yesung05/24-OSS-Teamwork
```  
- 로컬 깃 저장소의 내용을 github 파일로 최신화  
```
git pull
```  
- 로컬 깃 저장소의 내용을 github로 업로드  
```
git push
```  

