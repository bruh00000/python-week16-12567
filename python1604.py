def funAdd(num1:int, num2:int)->int:

    num3 = num1 + num2
    return num3

#Call a function
def results():
    num1,num2=5,15
    title = "The addition of"
    ans = funAdd(num1,num2)
    print(f"{num1} + {num2} = {ans}")
