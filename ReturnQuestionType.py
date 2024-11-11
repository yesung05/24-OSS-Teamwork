
def getQuestionType(type): #문제 유형 반환
    typev = int(type[1])
    match typev:
        case 1:
            return "객관식"
        case 2:
            return "단답형"
        case 3:
            return "O, X"