
def go(n):
    if(n%4!=0):
        return 0
    elif(n%100!=0):
        return 1
    elif(n%400==0):
        return 1
    else:
        return 0
