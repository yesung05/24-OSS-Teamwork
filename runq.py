import QType as pqt
import ReturnQuestionType as rqt
def runqq(count, datas):
    right = 0
    for i in range(count):  # 원하는 문제 횟수로 반복

        Qtype = rqt.getQuestionType(datas[i])
        if Qtype == "객관식":
            right += pqt.MultiChoice(i+1, datas[i])
        elif Qtype == "단답형":
            right += pqt.ShortAnswer(i+1, datas[i])
        elif Qtype == "O, X":
            right += pqt.OX(i+1, datas[i])
        print('------------------------------------------')
    print(f'{count}개의 문제 중 맞은 문제 수는 {right}개 입니다.')
    print(f'정답률은 {right/count:.2%}')
    print('------------------------------------------')
    return False