import random

def print_board(board):
    size = len(board)
    print("  " + " ".join(str(i + 1) for i in range(size)))
    
    for i in range(size):
        print(f"{i + 1} " + " ".join(board[i])) #вывод поля

def check_win(board, player): #метод для проверки на выигрышную комбинацию 
    size = len(board)
    
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(size):
        if all(board[row][col] == player for row in range(size)):
            return True
    
    if all(board[i][i] == player for i in range(size)):
        return True
    
    if all(board[i][size - 1 - i] == player for i in range(size)):
        return True
    
    return False

def check_draw(board): #метод для проверки наличия оставшихся игровых клеток
    for row in board:
        if '.' in row:
            return False
    return True

def get_valid_move(board, size):
    while True:
        try:
            move = input().strip().split()
            
            if len(move) != 2:
                print("Неправильный формат. Введите два числа через пробел (например: 1 2)")
                continue
            
            row, col = int(move[0]), int(move[1])
            
            if not (1 <= row <= size and 1 <= col <= size):
                print(f"Координаты должны быть от 1 до {size}")
                continue  
            
            if board[row - 1][col - 1] != '.':
                print("Эта клетка уже занята. Выберите другую.")
                continue  
            
            return row - 1, col - 1
            
        except ValueError: #вывод ошибки при вводе нечислового значения
            print("Некорректный ввод. Введите два числа через пробел (например: 1 2)")

def main():
    z = True
    while z:
        print()
        print("настройка игры:")
        
        while True:
            try:
                size = int(input("введите размер поля (3-9): "))
                if 3 <= size <= 9:
                    break 
                else:
                    print("некорректный размер, попробуйте снова")
            except ValueError: #вывод ошибки при вводе нечислового значения
                print("некорректный ввод, попробуйте снова")
        
        board = [['.' for _ in range(size)] for _ in range(size)] #создание поля заданного размера
        
        current_player = 'X' if random.choice([True, False]) else 'O' #случайный выбор первого игрока
        
        # Сообщаем, кто ходит первым
        print()
        print("начало игры:")
        print(f"Первым ходит: {current_player}")
        
        # Основной игровой цикл
        while True:
            print_board(board)
            print()
            print(f" очередь {current_player}, (a,b, где a - горизонталь, b - вертикаль)': ", end="")
            
            row, col = get_valid_move(board, size) 
            
            board[row][col] = current_player #замена точки на ход текущего игрока
            
            if check_win(board, current_player):
                print_board(board)
                print()
                print(f"победа за {current_player}")
                break
            
            if check_draw(board):
                print_board(board)
                print()
                print("Ничья")
                break
            
            current_player = 'O' if current_player == 'X' else 'X' #смена игрока
        
        print()
        print("Сыграть еще раз? (да/нет): ", end="")
        
        while True:
            choice = input().strip().lower()
            if choice == "да":
                break
            elif choice == "нет":
                print()
                print("Спасибо за игру! До свидания!")
                z = False
            else:
                print("Пожалуйста, введите 'да' или 'нет': ", end="")

if __name__ == "__main__":
    main()