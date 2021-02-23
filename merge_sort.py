import random
import string
import os
import shutil


def file_len(file_name):
    """Функция возращает размер файла
    в качестве аргумента передается название файла"""
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def file_element(file_name, index, data_type='-s'):
    """Функция возвращает элемент файла.
    В качестве аргумента передаются название файла и индекс строки которую необхадимо вернуть"""
    with open(file_name, 'r') as f:
        for i, l in enumerate(f):
            if i + 1 == index:
                if data_type == '-s':
                    if '\n' not in l:
                        data = l + '\n'
                        return data
                    else:
                        return l
                else:
                    if '\n' not in l:
                        data = l + '\n'
                        return int(data)
                    else:
                        return int(l)


def file_element_save(file_name, data):
    """Функция сохраняет данные в файл.
    В качестве аргументов передаются имя файла и данные каторые нужно записать"""
    with open(file_name, 'a') as f:
        f.write(data)


def merge_f(in_file_name, out_file_name, index):
    """"""
    with open(in_file_name, 'r') as f:
        for i, data in enumerate(f):
            if i + 1 == index:
                if data != '\n':
                    with open(out_file_name, 'a') as f1:
                        f1.write(data)


def random_file_name():
    processed_data = 'processed data'  # Папка для хранения обработанных данных
    if os.path.exists(processed_data):  # Проверка наличия папки
        print('Папка уже существует')
    else:
        os.mkdir(processed_data)  # Создает папку processed data
    file_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    track_file = '{}/{}'.format(processed_data, file_name)
    return track_file


def correct_of_norm(last_item, current_item, sort_command):
    if sort_command == '-a':
        if last_item == '' or last_item < current_item or last_item == current_item:
            return True
        else:
            return False
    else:
        if last_item == '' or last_item > current_item or last_item == current_item:
            return True
        else:
            return False


def merge_file(left_list, right_list, out_file_name, sort_command, data_type_command, out_file_name_r='random'):
    if out_file_name_r == 'random':
        sorted_list = out_file_name
    else:
        sorted_list = out_file_name_r + '.txt'
    left_list_index = right_list_index = 1
    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = file_len(left_list[0])+1, file_len(right_list[0])+1
    last_element = ''
    for _ in range(left_list_length + right_list_length - 2):
        if sort_command == '-a':
            if left_list_index < left_list_length and right_list_index < right_list_length:
                # Сравниваем первые элементы в начале каждого списка
                # Если первый элемент левого подсписка меньше, добавляем его
                # в отсортированный массив
                try:
                    if file_element(left_list[0], left_list_index, data_type_command) <= file_element(right_list[0],
                                                                                                      right_list_index,
                                                                                                      data_type_command):

                        if data_type_command == '-s' and file_element(left_list[0], left_list_index) == '\n':
                            left_list_index += 1
                        else:
                            if correct_of_norm(last_element, file_element(left_list[0], left_list_index, data_type_command), sort_command):
                                file_element_save(sorted_list, file_element(left_list[0], left_list_index))
                                last_element = file_element(left_list[0], left_list_index, data_type_command)
                                left_list_index += 1
                            else:
                                left_list_index += 1
                    # Если первый элемент правого подсписка меньше, добавляем его
                    # в отсортированный массив
                    else:
                        if data_type_command == '-s' and file_element(right_list[0], right_list_index) == '\n':
                            right_list_index += 1
                        else:
                            if correct_of_norm(last_element, file_element(right_list[0], right_list_index, data_type_command), sort_command):
                                file_element_save(sorted_list, file_element(right_list[0], right_list_index))
                                last_element = file_element(right_list[0], right_list_index, data_type_command)
                                right_list_index += 1
                            else:
                                right_list_index += 1
                except ValueError:
                    try:
                        file_element(left_list[0], left_list_index, data_type_command)
                    except ValueError:
                        left_list_index += 1
                    try:
                        file_element(right_list[0], right_list_index, data_type_command)
                    except ValueError:
                        right_list_index += 1

            # Если достигнут конец левого списка, элементы правого списка
            # добавляем в конец результирующего списка
            elif left_list_index == left_list_length:
                merge_f(right_list[0], sorted_list, right_list_index)
                right_list_index += 1
            # Если достигнут конец правого списка, элементы левого списка
            # добавляем в отсортированный массив
            elif right_list_index == right_list_length:
                merge_f(left_list[0], sorted_list, left_list_index)
                left_list_index += 1
        else:
            if left_list_index < left_list_length and right_list_index < right_list_length:
                # Сравниваем первые элементы в начале каждого списка
                # Если первый элемент левого подсписка меньше, добавляем его
                # в отсортированный массив
                try:
                    if file_element(left_list[0], left_list_index, data_type_command) >= file_element(right_list[0],
                                                                                                      right_list_index,
                                                                                                      data_type_command):

                        if data_type_command == '-s' and file_element(right_list[0], right_list_index) == '\n':
                            right_list_index += 1

                        if data_type_command == '-s' and file_element(left_list[0], left_list_index) == '\n':
                            left_list_index += 1
                        else:
                            if correct_of_norm(last_element, file_element(left_list[0], left_list_index, data_type_command), sort_command):
                                file_element_save(sorted_list, file_element(left_list[0], left_list_index))
                                last_element = file_element(left_list[0], left_list_index, data_type_command)
                                left_list_index += 1
                            else:
                                left_list_index += 1
                    # Если первый элемент правого подсписка меньше, добавляем его
                    # в отсортированный массив
                    else:
                        if data_type_command == '-s' and file_element(right_list[0], right_list_index) == '\n':
                            right_list_index += 1
                        else:
                            if correct_of_norm(last_element, file_element(right_list[0], right_list_index, data_type_command), sort_command):
                                file_element_save(sorted_list, file_element(right_list[0], right_list_index))
                                last_element = file_element(right_list[0], right_list_index, data_type_command)
                                right_list_index += 1
                            else:
                                right_list_index += 1
                except ValueError:
                    try:
                        file_element(left_list[0], left_list_index, data_type_command)
                    except ValueError:
                        left_list_index += 1
                    try:
                        file_element(right_list[0], right_list_index, data_type_command)
                    except ValueError:
                        right_list_index += 1

            # Если достигнут конец левого списка, элементы правого списка
            # добавляем в конец результирующего списка
            elif left_list_index == left_list_length:
                merge_f(right_list[0], sorted_list, right_list_index)
                right_list_index += 1
            # Если достигнут конец правого списка, элементы левого списка
            # добавляем в отсортированный массив
            elif right_list_index == right_list_length:
                merge_f(left_list[0], sorted_list, left_list_index)
                left_list_index += 1

    return [sorted_list]


def merge_sort_file(in_file_name, data_type_command, out_file_name='0', sort_command='-a', len_in_file=0):

    # Возвращаем список, если он состоит из одного элемента
    if len(in_file_name) <= 1:
        return in_file_name
    if len(in_file_name) > 2 and len(in_file_name) == len_in_file or len(in_file_name) == 2 and len(
                in_file_name) == len_in_file:
        # Для того чтобы найти середину списка, используем деление без остатка
        # Индексы должны быть integer
        mid = len(in_file_name) // 2

        # Сортируем и объединяем подсписки
        left_list = merge_sort_file(in_file_name[:mid], data_type_command, out_file_name, sort_command)
        right_list = merge_sort_file(in_file_name[mid:], data_type_command, out_file_name, sort_command)

        # Объединяем отсортированные списки в результирующий
        return merge_file(left_list, right_list, out_file_name, sort_command, data_type_command)
    elif len(in_file_name) > 2:
        # Для того чтобы найти середину списка, используем деление без остатка
        # Индексы должны быть integer
        mid = len(in_file_name) // 2

        # Сортируем и объединяем подсписки
        left_list = merge_sort_file(in_file_name[:mid], data_type_command, out_file_name, sort_command)
        right_list = merge_sort_file(in_file_name[mid:], data_type_command, out_file_name, sort_command)
        out_file_name_r = random_file_name()
        # Объединяем отсортированные списки в результирующий
        return merge_file(left_list, right_list, out_file_name, sort_command, data_type_command, out_file_name_r)
    else:
        # Для того чтобы найти середину списка, используем деление без остатка
        # Индексы должны быть integer
        mid = len(in_file_name) // 2

        # Сортируем и объединяем подсписки
        left_list = merge_sort_file(in_file_name[:mid], data_type_command, sort_command=sort_command)
        right_list = merge_sort_file(in_file_name[mid:], data_type_command, sort_command=sort_command)
        out_file_name_r = random_file_name()
        # Объединяем отсортированные списки в результирующий
        return merge_file(left_list, right_list, out_file_name, sort_command, data_type_command, out_file_name_r)


def play():

    in_file_name = []

    base_prompt = """
        Пожалуйста введите параметры программы через пробел
        Режим сортировки: (-a или -d), необязательный, по умолчанию сортирует по возрастанию
        Тип данных: (-s или -i), обязательный, s-string, i-integer
        Имя выходного файла, обязательный, Например: Out.txt
        Имена входных файлов, не менее одного
        
        Для выхода из программы введите "Quit"!!!
        
        """
    feedback = ""

    while True:  # -a -i Out.txt in1.txt in2.txt in3.txt in4.txt in5.txt
        parameter_program = input(feedback + "\n" + base_prompt)

        feedback = ""
        parameter_program = parameter_program.split()
        data_type_command = ''
        sort_command = ''
        file_name_error = 0
        start_of_filenames = 0

        if len(parameter_program) < 3:
            if len(parameter_program) == 0:
                feedback += "Вы не ввели параметры программы!!!"
            elif parameter_program[0] == "Quit":
                return
            else:
                feedback += "Вы ввели не достаточно параметров программы"

        elif len(parameter_program) >= 3:
            if parameter_program[0] == '-a' or parameter_program[0] == '-d':
                sort_command = parameter_program[0]
            if sort_command == '':
                if parameter_program[0] == '-s' or parameter_program[0] == '-i':
                    data_type_command = parameter_program[0]
                    start_of_filenames = 2
                else:
                    feedback += "Неправильно введены параметры посмотрите инструкцию ввода параметров"
            elif sort_command != '':
                if parameter_program[1] == '-s' or parameter_program[1] == '-i':
                    data_type_command = parameter_program[1]
                    start_of_filenames = 3
                else:
                    feedback += "Неправильно введены параметры посмотрите инструкцию ввода параметров"

            if data_type_command != '':
                if len(parameter_program[start_of_filenames:]) > 0:
                    file_name_error = []
                    for _ in parameter_program[start_of_filenames:]:
                        try:
                            with open(_, "r") as InFile:
                                InFile.read(2).split()
                            in_file_name.append(_)
                        except FileNotFoundError:
                            print("Файл с именем {} не найдет".format(_))
                            file_name_error.append(_)
                else:
                    print("Вы не ввели никаких входных файлов")
                if len(file_name_error) > 0:
                    print("Некотырые файлы не читаются")
                    print("А именно {}".format(file_name_error))
                if len(in_file_name) != 0:
                    if len(in_file_name) == 1:
                        print("Файл уже отсортирован")
                    else:
                        if os.path.exists(parameter_program[start_of_filenames-1]):  # Проверка наличия file
                            print('Файл {} уже существует и будет перезаписан'.format(parameter_program[start_of_filenames-1]))
                            os.remove(parameter_program[start_of_filenames-1])
                            x = merge_sort_file(in_file_name, data_type_command,
                                                parameter_program[start_of_filenames - 1],
                                                sort_command=sort_command, len_in_file=len(in_file_name))
                            try:
                                shutil.rmtree('processed data')
                                return in_file_name
                            except FileNotFoundError:
                                return in_file_name
                        else:
                            x = merge_sort_file(in_file_name, data_type_command,
                                                parameter_program[start_of_filenames - 1],
                                                sort_command=sort_command, len_in_file=len(in_file_name))
                            try:
                                shutil.rmtree('processed data')
                                return in_file_name
                            except FileNotFoundError:
                                return in_file_name
                else:
                    print("Введеные файлы не найдены попробуйте еще раз")


# Проверяем, что оно работает
print(play())
