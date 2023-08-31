def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        print("Division by zero is not allowed.")
        return x

print('Hello, I am a calculator')
print('What\'s your name?')
user_name = input()
print(user_name + ' type equation one by one, and I\'m going to solve it')

number = float(input())
s = 1

while s != 100:
    print(number)
    oho = input("a = ")
    
    if oho == "end":
        print("result = " + str(number))
        break
    elif oho in "+-*/":
        druga_liczba = float(input("Enter the second number = "))
        
        if oho == "+":
            number = dodawanie(number, druga_liczba)
        elif oho == "-":
            number = odejmowanie(number, druga_liczba)
        elif oho == "*":
            number = mnozenie(number, druga_liczba)
        elif oho == "/":
            number = dzielenie(number, druga_liczba)
        else:
            print("Invalid operation")
    else:
        print("Invalid operation")