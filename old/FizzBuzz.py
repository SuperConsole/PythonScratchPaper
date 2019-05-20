#
#   just FizzBuzz
#

def FizzBuzz(num, maxNum):
    if num%15  ==  0:
        print(str(num) + " FizzBuzz")
    elif num%3 ==  0:
        print(str(num) + " Fizz")
    elif num%5 ==  0:
        print(str(num) + " Buzz")
    else:
        print(str(num))
    
    if num <   maxNum:
        FizzBuzz(num+1, maxNum)

if __name__ == "__main__":
    iter = [1300, 1350]
    FizzBuzz(iter[0], iter[-1])
