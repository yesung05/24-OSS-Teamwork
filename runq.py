import QType as pqt
import ReturnQuestionType as rqt
def runqq(count, datas):
    for i in range(count):  # 원하는 문제 횟수로 반복

        Qtype = rqt.getQuestionType(datas[i])
        if Qtype == "객관식":
            pqt.MultiChoice(i+1, datas[i])
        elif Qtype == "단답형":
            pqt.ShortAnswer(i+1, datas[i])
        elif Qtype == "O, X":
            pqt.OX(i+1, datas[i])
        print('------------------------------------------')
    return False