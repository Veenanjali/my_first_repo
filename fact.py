def fact1():
    num = 4
    factorial = 1
    if num < 0:
       print(" Factorial does not exist for negative numbers")
    elif num == 0:
     print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)
        print("new change is made to trigger the build")
        return factorial



def test_01():
    print("checkin factorial")
    assert fact1() == 24
    print("tests passed")
