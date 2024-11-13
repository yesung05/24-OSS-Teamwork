def askonemore():
    resume = input("계속 하시겠습니까? (O,X): ")
    resume = resume.upper()
    if(resume == 'O'):
        return True
    else:
        return False