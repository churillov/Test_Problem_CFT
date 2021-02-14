def play():
    InFileName = []

    base_prompt = """
        Пожалуйста введите параметры программы через пробел
        Режим сортировки: (-a или -d), необязательный, по умолчанию сортирует по возрастанию
        Тип данных: (-s или -i), обязательный, s-string, i-integer
        Имя выходного файла, обязательный, Например: Out.txt
        Имена выходных файлов, не менее одного
        """
    feedback = ""

    while True:
        parameter_program = input(feedback + "\n" + base_prompt) # -a -s Out.txt in1.txt

        feedback = ""
        parameter_program = parameter_program.split()

        if len(parameter_program) == 0:
            print("Вы не ввели параметры программы")
        else:
            command = parameter_program
            print(command)
            return


play()
# parameter_program = input()
# parameter_program = parameter_program.split()
# print(parameter_program)
#
# if '-a' == parameter_program[0] or '-d' == parameter_program[0]:
#     print('tet')



# try:
#     if "-a" == parameter_program[0]:
#         print('tyt')
# except:
#     print("Ошибка, введено не целое число")


class FileName:

    def __init__(self, file_name):
        self.file_name = file_name



with open("IN1.txt", "r") as In1:
    list_In1 = In1.read()
    a = [list_In1.split()]
    print(a)

with open("IN2.txt", "r") as f1:
    z1 = f1.read()
    a1 = list(z1.split())
    print(a1)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)

# Проверяем, что оно работает


random_list_of_nums = ['56', 'р', '3', '185', '120']
random_list_of_nums = merge_sort(a)
print(random_list_of_nums)
