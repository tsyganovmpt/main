def oper_a():
    num_1 = float(input("первое число: "))
    oper = input("операция: ")
    num_2 = float(input("второе число: "))
    if oper=="+":
        print(num_1 + num_2)
    elif oper=="-":
        print(num_1 - num_2)
    elif oper=="**":
        print(num_1 ** num_2)
    elif oper=="*":
            print(num_1 * num_2)
    elif oper=="/":
        if num_2!=0:
            print(num_1 / num_2)
        else: print("делить на 0 нельзя!")
    elif oper=="//":
        if num_2!=0:
            print(num_1 // num_2)
        else: print("делить на 0 нельзя!")
    elif oper=="%":
        if num_2!=0:
            print(num_1 % num_2)
        else: print("делить на 0 нельзя!")
    else: print("ОШИБКА СИНТАКСИСА")
     
def oper_s():
    num_1 = float(input("первое число: "))
    oper = input("операция: ")
    num_2 = float(input("второе число: "))
    if oper==">":
        print(num_1>num_2)
    elif oper=="<":
        print(num_1<num_2)
    elif oper==">=":
        print(num_1>=num_2)
    elif oper=="<=":
        print(num_1<=num_2)
    elif oper=="==":
        print(num_1==num_2)
    elif oper=="!=":
        print(num_1!=num_2)
    else: print("ОШИБКА СИНТАКСИСА")

def oper_p():
    num_1 = float(input("первое число: "))
    oper = input("операция: ")
    num_2 = float(input("второе число: "))
    bool_num_1 = bool(num_1)
    bool_num_2 = bool(num_2)

    if oper=="and" and num_1>0 and num_2>0:
        print(bool_num_1 and bool_num_2)
    elif oper=="or" and (num_1>0 or num_2>0): 
        print(bool_num_1 and bool_num_2) 
    elif oper=="not":
        print("числа равны нулю?")
        print("первое:", not bool_num_1)
        print("второе:", not bool_num_2)
    else: print("False")

def main():
    print("выберите необходимый блок операторов: арифметика, сравнение, логика ")
    print()
    call = input()
    print()
    if call == "арифметика":
        oper_a()
    elif call == "сравнение":
        oper_s()
    elif call == "логика":
        oper_p()
    else: print("НЕСУЩЕСТВУЮЩИЙ БЛОК")

if __name__ == '__main__':
    main()