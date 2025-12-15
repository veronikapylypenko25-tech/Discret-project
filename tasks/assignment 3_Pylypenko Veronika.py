def find_primes(a:int,b:int):
    my_list=[]
    my_new_list=[]
    k=2
    for x in range(a,b):
        my_list.append(x)
    for y in my_list:
        if k<=9:
            if y != k and k!=1 and y % k != 0:
                my_new_list.append(y)
        k += 1
    return my_list, my_new_list
print(find_primes(0, 5))