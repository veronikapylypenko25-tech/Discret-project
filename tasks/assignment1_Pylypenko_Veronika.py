import string
x = int(input("Введіть ціле число від 101 до 999, щоб його остання цифра не дорівнювала 0: "))
if x<101 or x>999 or x%10==0:
    print("Помилка! Введіть число відповідне умові!")
else:
    print(f"Результат№1:{str(x)[::-1]}")
    print(f"Результат№2:{"".join(reversed(str(x)))}")
    res = 0
    abs_x = abs(x)
    while abs_x > 0:
        dig = abs_x % 10
        res = res * 10 + dig
        abs_x //= 10
    print(f"Результат№3:{res}")

p = input("Введіть пароль: ")
print("Цифри:", bool(set(p) & set(string.digits)))
print("Великі літери:", bool(set(p) & set(string.ascii_uppercase)))
print("Довжина >= 9:", len(p) >= 9)

name = input("Введіть своє ім'я: ")
month_salary = float(input("Введіть свою місячну зарплату в доларах: "))
year_salary = month_salary * 12 / 1000

print(f"Річна зарплата {name} = {year_salary:.0f} тис.доларів.")
print(f"Річна зарплата {name} = {year_salary:.0f} тис.доларів.")

a1 = int(input("Введіть перше число: "))
a2 = int(input("Введіть друге число: "))
print("Сума =", a1 + a2)
print("Різниця =", a1 - a2)
print("Добуток =", a1 * a2)
print("Частка =", a1 / a2)
print("Залишок =", a1 % a2)
print(a1 >= a2)
