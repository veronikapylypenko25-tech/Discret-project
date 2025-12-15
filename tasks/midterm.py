#1
data = [
 12, 4.4, "apple", (2,3), {"age":18}, [2,3], 8.1, "dog", (4,5), 1.1,
 {"key":5}, [9], 14, "python", 6.6, (), {}, False, [True,0], (6,7),
 3.14, "car", {"name":"Bob"}, 10, "data", 7.7, [8,9], (8,9), True, {"flag":False}
]
def d(dani):
    result = []
    for x in data:
        if isinstance(x,int):
            result['int'].append(x)
        if  isinstance(x,float):
            result['float'].append(x)
        if isinstance(x,list):
            result['list'].append(x)
        if isinstance(x,str):
            result['str'].append(x)
        if isinstance(x,tuple):
            result['tuple'].append(x)
        return result
print("Our list:", data)
print("New dict: ", d(data))
print(d(data))

#2
import random
try:
    age = random.randint(0, 125)
    print("age:", age)
    signal = 0
    count_attempts = 6
    age_p = int(input(f"Введіть вік людини. Ви маєте {count_attempts} спроб: "))
    while signal < 6:
        if age_p == age:
            print("Ви вгадали! Гра завершена!")
            break
        else:
            attempt_result = "На жаль, Ви не вгадали:( Спробуйте ще раз!"
            signal += 1
            count_attempts -= 1

            if age > age_p:
                attempt_result = "Age is bigger"
            else:
                attempt_result = "Age is smaller"
    print(attempt_result)
except ValueError:
        print("Помилка! Введіть число!!!")
        signal += 1
        count_attempts -= 1
except TypeError:
        print("Числа мають бути цілі!")
        signal+=1
#3-4
def func1(n:int, v1:str,v2:str)->tuple:
    rates = {"GBP": 49.5, "CHF": 44.7, "CZK": 1.72}
    result= rates[v2]*n
    return(n, v1, int(result), v2)
def func2(n1, v1, n2, v2):
    return f"У вас є {n1} {v1} дорівнює {n2} {v2}"
x =int(input("Введіть число, яке хочете перевести: "))
v1= input("Введіть поточну валюту: ")
v2= input("Введіть валюту, в яку хочете перевести: ")
print((func1(x, v1, v2)))
result = (func1(x, v1, v2))
print(func2(*result))

def get_cort(tupl):
    with open("myfile.cvs","a") as f:
        for x in tupl:
            f = ", ".join(tupl)
    return f
def get_file(file):
    with open("myfile.cvs", "r") as f:
        print(f)
