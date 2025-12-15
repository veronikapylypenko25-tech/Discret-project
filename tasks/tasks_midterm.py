x=int(input("Введіть число: "))
n=x
y=0
while n!=0:
    y+=x%10+y*10
    n//=10
print(y)

y=input("Введіть текст: ")
letters = 0
digits=0
others=0
for a in y:
    if "A"<a <"Z":
        letters+=1
    elif 0<int(a)<10:
        digits+=0
    else:
        others+=1
print("letters:", letters)
print("digits: ", digits)
print("others: ", others)