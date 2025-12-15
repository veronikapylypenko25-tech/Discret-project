#1
import random

marks = {}
students= ['student№1', 'student№2', 'student№3', 'student№4', 'student№5']

for student in students:
    marks[student] = (random.randint(60, 100), random.choice(["Passed", "Failed"]))
print(f"Вхідні данні:{marks}")

st_passed=[]
st_failed=[]
for mark, result in marks.values():
    if result=="Passed":
        st_passed.append(mark)
    else:
        st_failed.append(mark)
if not st_passed or not st_failed:
    print("Професор Грубл був послідовним, бо всі або склали, або завалили!")
else:
    if max(st_failed) < min(st_passed):
        print(
            f"Професор Грубл був послідовним у виставленні оцінок! Поріг сдачі екзамену знаходиться у діапазоні від {max(st_failed)+1} (включно) до {max(st_passed)} (включно).")
    else:
        print("Професор Грубл не був послідовним у виставленні оцінок!")