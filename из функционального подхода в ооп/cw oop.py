class PlayingField:
    def __init__(self):
        self.field_size = self.field_size_check()
        self.dictionary_of_cells = self.cells()
        self.drawn_field = self.field(self.dictionary_of_cells, self.field_size)

    @staticmethod
    def field_size_check():
        """
    Функция запрашивает от пользователя размер поля, проверяет ответ на корректность
        :return: целочисленное значение в диапазоне от 03 до 10
        """
        while True:
            field_size = ''.join(
                input(
                    '\nВведите число N (количество клеток по горизонтали и вертикали) в диапазоне от 03 до 10:\n=>').split())
            lst = [str(number) for number in range(3, 11)]
            if field_size in lst:
                return int(field_size)
            else:
                print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 03 до 10.")

    @staticmethod
    def cells() -> dict[int:str]:
        """
    Функция генерирует словарь размера, равного входящему значению. Ключ равен номеру ячейки игрового поля.
        :param number_of_cells_: Размер поля в виде целочисленного значения
        :return: Словарь с заданным количеством элементов
        """
        cells = {}
        for key in range(1, (self.field_size ** 2) + 1):
            cells[key] = 'None'
        return cells

    def field(self) -> str:  # функция рисующая поле
        """
    Функция приводит словарь в вид игрального поля.
        :param cells: Словарь, в котором сохранены ходы игроков. Ключ - номер ячейки поля, значение - маркер игрока или 'None'
        :param number_of_cells: Число ячеек по горизонтали, по вертикали игрового поля
        :return: Строковое значение; при передаче функции print отображается пользователю(игроку) как текущее игральное поле
        """
        field = []
        counter = 0
        b = '+---+' * self.field_size
        for lst in self.dictionary_of_cells:
            if counter % self.field_size == 0:
                field.append(f'\n{b}\n')
            counter += 1
            if self.dictionary_of_cells.get(lst) == 'None':
                if lst > 9:
                    field.append(f'|{lst} |')
                else:
                    field.append(f'| {lst} |')
            else:
                field.append(f'| {self.dictionary_of_cells.get(lst)} |')
        field.append(f'\n{b}\n')
        return "".join(field)

    def players_move(self, current_player: tuple[str, str], cells: dict) -> dict:
        """
    Ф-я запрашивает у пользователя, какую ячейку в игровом поле он хочет занять. Ответ записывает в словарь.
        :param current_player: Текущий игрок. Список в виде: (наименование_игрока, маркер)
        :param cells: словарь, содержащий в себе данные о занятых ячейках игрового поля
        :return: измененный словарь
        """
        while True:
            answer = ''.join(input(
                f'Твой ход, {current_player[0]}! Выбери число, соответствующее ячейке, от 1 до {len(self.dictionary_of_cells)}.\n=>').split())
            lst = str(list(range(1, len(self.dictionary_of_cells) + 1)))
            if answer in lst:
                if self.dictionary_of_cells[int(answer)] == 'None':
                    self.dictionary_of_cells = current_player[-1]
                    return self.dictionary_of_cells
                else:
                    print(f'Данная ячейка занята. Пожалуйста, выберите свободную ячейку.')
            else:
                print(
                    f'Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до {len(self.dictionary_of_cells)}.')


class Players:
    def __init__(self):
        self.players_marker_list = self.players_marker()
        self.first_move_list = self.first_move()

    @staticmethod
    def players_marker() -> list[tuple, tuple]:
        """
    Функция запрашивает и сохраняет данные от пользователя о том, какой игрок делает ход каким маркером.
        :return: Список, в котором хранится 2 кортежа в виде [(наименование_игрока, маркер), (наименование_игрока, маркер)]
        """
        while True:
            marker = ''.join(input(
                'Какой знак возьмет себе Player1? Если "Х" - введите 1, если "0", то 2. Невыбранный символ присвоится Player2 автоматически. \n=>').split())
            players_marker_list = []
            lst = ['1', '2']
            if marker in lst:
                players_marker_list.append(('Player1', 'X')) if marker == '1' else players_marker_list.append(
                    ('Player1', '◯'))
                players_marker_list.append(('Player2', '◯')) if marker == '1' else players_marker_list.append(
                    ('Player2', 'X'))
                return players_marker_list
            else:
                print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до 2.")

    def first_move(self) -> tuple[str, str]:
        """
    Функция запрашивает и сохраняет от пользователя данные о том, кто ходит первый.
        :param players_marker: Список, в котором хранится 2 кортежа в виде [(наименование_игрока, маркер), (наименование_игрока, маркер)]
        :return: Возвращает кортеж вида (наименование_игрока_который_ходит_первым, маркер)
        """
        while True:
            move = ''.join(input('Кто ходит первый? Введите 1, если "Player1", если "Player2" то 2. \n=>').split())
            if move == '1':
                first_move_list = self.players_marker_list[0]
                return first_move_list  # возвращает кортеж вида (наименование_игрока_который_ходит_первым, маркер)
            elif move == '2':
                first_move_list = self.players_marker_list[-1]
                return first_move_list  # возвращает кортеж вида (наименование_игрока_который_ходит_первым, маркер)
            else:
                print("Нет варианта ответа для выбранного значения. Выберите, пожалуйста, цифру от 1 до 2.")

    def player_change(player: tuple[str, str]) -> tuple[str, str]:
        """
    Ф. обеспечивает сменность игроков (чередование хода)
        :param player: Игрок, который уже сделал ход
        :param players_marker_list: Список, в котором хранится 2 кортежа в виде [(наименование_игрока, маркер), (наименование_игрока, маркер)]
        :return: Кортеж вида (наименование_игрока_который_ходит_следующим, маркер)
        """
        if player[0] == 'Player1':
            return self.players_marker_list[-1]  # ('Player2', '*')
        else:
            return self.players_marker_list[0]  # ('Player1', '*')


class SystemTools:
    def __init__(self, cells):
        self.matrix = self.matrix_constructor(cells)
        self.diagonal_list  = None


    def matrix_constructor(cells: dict) -> list[list, list, ...]:
        """
        Преобразует словарь в матрицу, состоящую из значений словаря, соответственно строкам игрового поля
        :param cells: Словарь, в котором сохранены ходы игроков.
        :return: Матрица вида [['маркер игрока/None', 'маркер игрока/None',....],[],[],...]
        """

        value = list(cells.values())
        length = len(value)
        middle_index = round(length ** 0.5)
        lst = []
        for x in range(0, length, middle_index):
            lst.append(value[x: middle_index + x])
        return lst

    def transpose_matrix(self) -> list[list, list, ...]:
        """
    Выполняет транспонирование матрицы
        :param matrix: значения словаря cells в матричном виде, соответственно игровому полю
        :return: транспонированная матрица
        """
        trans = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        self.matrix = trans

    def check_line(self) -> bool:
        """
    Ф-я проверяет, все ли значения одинаковы в последовательности
        :param matrix: значения словаря cells в матричном виде
        :return: True - в матрице найдена строка с ячейками, данные в которых одинаковы; False - строка не найдена
        """
        for lst in self.matrix:
            if 'None' not in lst:
                if len(set(lst)) == 1:
                    return True

    def diagonal(self) -> list[list, list, ...]:
        """
    Ф-я создает список со значениями игрового поля по диагонали (слева-направо и справа-налево)
        :param matrix: Значения словаря cells в матричном виде
        :return: Список со значениями игрового поля по диагонали в виде [[слева-направо],[справа-налево]]
        """
        diagonal1 = [self.matrix[j][j] for j in range(len(self.matrix))]
        i = len(self.matrix) - 1
        diagonal2 = []
        for j in range(len(self.matrix)):
            diagonal2.append(self.matrix[j][i])
            i -= 1
        diagonal = [diagonal1, diagonal2]
        self.diagonal_list  = diagonal


class GameTicTacToe:
    def __init__(self):
