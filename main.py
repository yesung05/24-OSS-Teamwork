import random
import QType as pqt  # Print Question Type
import ReturnQuestionType as rqt  # Return Question Type
import readfile
import readcsv
import runq
import onemore
import selcount as ct
"""
**필드명**

Question : 문제
num : 문제번호
answer : 입력받은 정답

"""

print()
print('------------------------------------------')
print()
conti = True
while (conti):
    file_path = readfile.readfile()
    datas = readcsv.readcsv(file_path)

    # 문제 풀기
    random.shuffle(datas)
    
    val = ct.selcount(datas)
    if(val == False):
        continue
    else:
        count = val
    running = runq.runqq(count,datas)
    if(not running):
        if(not onemore.askonemore()):
            break
    

    