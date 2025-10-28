def level1(inventory):

    while True:
        print("")
        print("вы находитесь в камере за решеткой, что вы хотите сделать?: открыть дверь, посмотреть под шконку, проспать всю ночь, посмотреть инвентарь")
        print("-------------------------")
        move = input().lower()

        if move == "посмотреть под шконку":
            if "отмычка" in inventory:
                print("вы посмотрели под шконку, под ней пусто")
            else:
                print("")
                print("вы посмотрели под шконку, под ней лежит отмычка")
                print("получен предмет: отмычка")
                inventory.append("отмычка")
        elif move == "проспать всю ночь":
            print("")
            print("вы проспали всю ночь и встали с новыми силами")
        elif move == "посмотреть инвентарь":
            print("")
            print("инвентарь:", inventory)
        elif move == "открыть дверь":
            if "отмычка" in inventory:
                print("")
                print("вы взломали дверь и попали в коридоры")
                return True
            else:
                print("") 
                print("у вас нет отмычки")
        else:
            print("") 
            print("неизвестная команда")
 
def level2(inventory):

    while True:
        print("")
        print("вы вошли в коридор, что вы сделаете?: пойти направо, пойти налево, оглядеться, посмотреть инвентарь")
        print("-------------------------")
        move = input().lower()

        if move == "оглядеться":
            print("")
            print("в левом конце коридора спит охранник с кодом от выхода, в правом конце коридора находится дверь на выход")
        elif move == "посмотреть инвентарь":
            print("")
            print("инвентарь:", inventory)
        elif move == "пойти налево":
            print("")
            print("-------------------------")
            print("вы пошли налево, рядом спит охранник с кодом от выхода, ваши действия? взять код, прочитать код")
            action = input().lower()
            
            if action == "взять код":
                if "код" in inventory:
                    print("")
                    print("у вас уже есть код, вы вернулись в коридор")    
                else:
                    print("")
                    print("вы забрали код, охранник продолжил спать")
                    print("получен предмет: код")
                    inventory.append("код")
                    print("вы вернулись в коридор")
            elif action == "прочитать код":
                print("")
                print("вы попытались прочитать код, но но охранник уже проснулся!")
                return False
            else: 
                print("")
                print("неизвестная команда")
        elif move == "пойти направо": 
                return True

def level3(inventory):

    while True:
        print("")
        print("вы пришли к двери, ваши действия?: ввести код, вернуться обратно, посмотреть инвентарь, использовать отмычку, прочитать код")
        print("-------------------------")
        move = input().lower()

        if move == "ввести код":
            print("")
            code = int(input())
            print("")
            if code == 1323:
                print("вы ввели код и открыли дверь!")
                return True
            else: 
                print("вы ввели неверный код, включилась сигнализация!")
                return False
        elif move == ("вернуться обратно"):
            level2(inventory)
        elif move == ("использовать отмычку"):
            if "отмычка" in inventory:
                print("")
                print("вы попытались открыть дверь отмычкой, но она сломалась!")
                inventory.remove("отмычка")
            else:
                print("")
                print("у вас больше нет отмычки")
        elif move == "посмотреть инвентарь":
            print("")
            print("инвентарь:", inventory)
        elif move == "прочитать код":
            if "код" in inventory:
                print("")
                print("код: 1323")
            else:
                print("")
                print("у вас нет кода!")
        else: 
            print("")
            print("неизвестная команда")
            
def main():
    inventory = []

    current_room = 1

    while True:
        if current_room == 1:
            if level1(inventory):
                current_room = 2
            else:
                break
        elif current_room == 2:
            if level2(inventory):
                current_room = 3
            else: 
                print("вас поймали!")
                print("-------------------------") 
                print("вы провалили побег!")               
                break
        elif current_room == 3:
            if level3(inventory):
                print("-------------------------")
                print("у вас получилось сбежать!")
                break
            else:
                print("вас поймали!")
                print("-------------------------") 
                print("вы провалили побег!")
                break  

if __name__ == "__main__":
    main()