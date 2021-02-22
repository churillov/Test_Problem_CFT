import random
import string
import os
import shutil


def file_len(file_name):
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def file_element(file_name, index):
    with open(file_name, 'r') as f:
        for i, l in enumerate(f):
            if i + 1 == index:
                if '\n' not in l:
                    l = l + '\n'
                    return l
                else:
                    return l


def file_element_save(file_name, data):
    with open(file_name, 'a') as f:
        d = f.write(data)


def merge_f(in_file_name, out_file_name, index):
    with open(in_file_name, 'r') as f:
        for i, l in enumerate(f):
            if i + 1 == index:
                with open(out_file_name, 'a') as f1:
                    d = f1.write(l)


def random_file_name():
    processed_data = 'processed data'  # Папка для хранения обработанных данных
    if os.path.exists(processed_data):  # Проверка наличия папки
        print('Папка уже существует')
    else:
        os.mkdir(processed_data)  # Создает папку processed data
    file_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    track_file = '{}/{}'.format(processed_data,file_name)
    return track_file


def merge_file(left_list, right_list, out_file_name, out_file_name_r='random'):
    if out_file_name_r == 'random':
        sorted_list = out_file_name
    else:
        sorted_list = out_file_name_r + '.txt'
    left_list_index = right_list_index = 1
    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = file_len(left_list[0])+1, file_len(right_list[0])+1

    for _ in range(left_list_length + right_list_length - 2):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if int(file_element(left_list[0], left_list_index)) <= int(file_element(right_list[0], right_list_index)):
                file_element_save(sorted_list, file_element(left_list[0], left_list_index))
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                file_element_save(sorted_list, file_element(right_list[0], right_list_index))
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


def merge_sort_file(in_file_name, out_file_name="qw1e.txt"):

    # Возвращаем список, если он состоит из одного элемента
    if len(in_file_name) <= 1:
        return in_file_name
    if len(in_file_name) > 2:
        # Для того чтобы найти середину списка, используем деление без остатка
        # Индексы должны быть integer
        mid = len(in_file_name) // 2

        # Сортируем и объединяем подсписки
        left_list = merge_sort_file(in_file_name[:mid], out_file_name)
        right_list = merge_sort_file(in_file_name[mid:], out_file_name)

        # Объединяем отсортированные списки в результирующий
        return merge_file(left_list, right_list, out_file_name)
    else:
        # Для того чтобы найти середину списка, используем деление без остатка
        # Индексы должны быть integer
        mid = len(in_file_name) // 2

        # Сортируем и объединяем подсписки
        left_list = merge_sort_file(in_file_name[:mid])
        right_list = merge_sort_file(in_file_name[mid:])
        out_file_name_r = random_file_name()
        # Объединяем отсортированные списки в результирующий
        return merge_file(left_list, right_list, out_file_name, out_file_name_r)


def play():

    InFileName = []

    base_prompt = """
        Пожалуйста введите параметры программы через пробел
        Режим сортировки: (-a или -d), необязательный, по умолчанию сортирует по возрастанию
        Тип данных: (-s или -i), обязательный, s-string, i-integer
        Имя выходного файла, обязательный, Например: Out.txt
        Имена входных файлов, не менее одного
        """
    feedback = ""

    while True:
        parameter_program = input(feedback + "\n" + base_prompt)  # -a -s Out.txt in1.txt in2.txt in3.txt

        feedback = ""
        parameter_program = parameter_program.split()
        data_type_command = ''
        sort_command = ''
        print(parameter_program)
        if len(parameter_program) < 3:
            if len(parameter_program) == 0:
                feedback += "Вы не ввели параметры программы!!!"
            elif parameter_program[0] == 'Quit':
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
                                datafile = InFile.read(2).split()
                            InFileName.append(_)
                        except FileNotFoundError:
                            print("Файл с именем {} не найдет".format(_))
                            file_name_error.append(_)
                else:
                    print("Вы не ввели никаких входных файлов")
                if len(file_name_error) > 0:
                    print("Некотырые файлы не читаются")
                    print("А именно {}".format(file_name_error))
                if len(InFileName) != 0:
                    if len(InFileName) == 1:
                        print("Файл уже отсортирован")
                    else:
                        if os.path.exists(parameter_program[start_of_filenames-1]):  # Проверка наличия file
                            print('Файл уже существует и будет перезаписан')
                            os.remove(parameter_program[start_of_filenames-1])
                            x = merge_sort_file(InFileName, parameter_program[start_of_filenames - 1])
                            shutil.rmtree('processed data')
                            return InFileName
                        else:
                            x = merge_sort_file(InFileName, parameter_program[start_of_filenames-1])
                            shutil.rmtree('processed data')
                            return InFileName
                else:
                    print("Введеные файлы не найдены попробуйте еще раз")
        if parameter_program[0] == "Quit":
            print("Exiting...")
            return

# Проверяем, что оно работает

print(play())
