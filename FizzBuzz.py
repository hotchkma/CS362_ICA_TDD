def convert(n):
    if (n%3==0 and n%5==0):
        return "FizzBuzz"
    elif (n%3==0):
        return "Fizz"
    elif (n%5==0):
        return "Buzz"
    else:
        return n

def run(n):
    result = ""
    for i in range(1,n):
        result+=str(convert(i))+" "
    if (n>0):
        result+=str(convert(n))
    return result
