# Функция для создания пустой доски нужного размера
def create_board(size):
    return [["" for _ in range(size)] for _ in range(size)]


# Функция для отображения игрового поля
def display_board(board):
    cell_width = 3  # Задаю ширину для каждой ячейки
    separator = "-" * (len(board[0]) * (cell_width + 1) + 1)
    print(separator)
    for row in board:
        centered_row = [f"{cell:^{cell_width}}" for cell in row]
        print("|" + "|".join(centered_row) + "|")
        print(separator)


# Функция для проверки победителя
def check_winner(board, player):
    size = len(board)

    # Проверка строк и столбцов
    for i in range(size):
        if all(cell == player for cell in board[i]):
            return True
        if all(row[i] == player for row in board):
            return True
    # Проверка диагоналей
    if all(board[i][i] == player for i in range(size)):
        return True
    if all(board[i][size - 1 - i] == player for i in range(size)):
        return True
    return False


# Функция для проверки ничьей
def check_draw(board):
    for row in board:
        if "" in row:
            return False
    return True


# Основная часть программы
def main():
    # Запрашиваю размер доски у пользователя
    try:
        size = int(input("Введите размер доски (например, 3 для 3х3): "))
        if size < 3:
            print("Размер доски должен быть не менее 3.")
            return
    except ValueError:
        print("Введите корректное число.")
        return

    board = create_board(size)  # Создаем пустую строку

    # Пример использования: добавление символов на доску и проверка победы
    current_player = "X"  # Текущий игрок
    moves = 0  # Подсчет ходов

    while moves < size * size:
        display_board(board)
        print(f"Ход игрока {current_player}")

        try:
            row = int(input("Введите номер строки: ")) - 1
            col = int(input("Введите номер столбца: ")) - 1

            if not (0 <= row < size and 0 <= col < size):
                print(f"Позиция ({row + 1},{col + 1}) вне диапазона, попробуйте снова.")
                continue
            elif board[row][col] != "":
                print("Эта ячейка уже занята, попробуйте другую.")
                continue

        except ValueError:
            print(f"Введите корректные номера от 1 до {size}.")
            continue

        # Обновление поля
        board[row][col] = current_player
        moves += 1

        # Проверка победителя
        if check_winner(board, current_player):
            display_board(board)
            print(f"Игрок {current_player} выиграл!")
            break

        # Проверка ничьей
        if check_draw(board):
            display_board(board)
            print("Ничья!")
            break

        # Смена игрока
        current_player = "O" if current_player == "X" else "X"

    print("Игра окончена!")


# Запуск игры
main()
