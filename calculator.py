num_1 = float(input("первое число: "))
oper = input("операция: ")
num_2 = float(input("второе число: "))

print("вывод: ")

if oper=="+":
    print(num_1 + num_2)
elif oper=="-":
    print(num_1 - num_2)
elif oper=="**":
    print(num_1 ** num_2)
elif oper=="*":
        print(num_1 * num_2)
elif oper=="/" and num_2!=0:
    print(num_1 / num_2)
elif oper=="/" and num_2==0:
    print("Делить на 0 нельзя!")
elif oper=="//" and num_2!=0:
    print(num_1 // num_2)
elif oper=="//" and num_2==0:
    print("Делить на 0 нельзя!")
elif oper=="%":
    if num_2!=0:
        print(num_1 % num_2)
elif oper=="==":
    print(num_1==num_2)
elif oper=="!=":
    print(num_1!=num_2)
elif oper==">":
    print(num_1>num_2)
elif oper=="<":
    print(num_1<num_2)
elif oper==">=":
    print(num_1>=num_2)
elif oper=="<=":
    print(num_1<=num_2)
else: print("ОШИБКА СИНТАКСИСА")

if not (num_1<0 or num_2<0):
    print("отрицательных чисел нет!")
else: print("есть отрицательные числа!")

