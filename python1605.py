def EvenOdd(x:int)->int:
    if(x % 2 == 0):
        result = "Even"
        return result
    else:
        result = "Odd"
        return result

def callEvenOdd():
    print("Please enter number : ", end="")
    x = int(input())
    ans = EvenOdd(x)
    print(f"Number = {x} is {ans}")