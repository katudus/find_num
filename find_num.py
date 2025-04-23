# Мини-проект: Числовая угадайка
import random


def is_valid(str, max):
    return True if str.isdigit() and 1 <= int(str) <= max else False


def will_start():
    while True:
        limit = input("Введите максимальное число 1 - ...\n")

        if not limit.isdigit():
            print("А может быть все-таки введем целое число?\n")
            continue

        print()
        limit = int(limit)
        return limit


print("Добро пожаловать в числовую угадайку\n")

limit = will_start()
hidden_number = random.randint(1, limit)
attempts = 0

while True:
    n = input(f"Введите число 1 - {limit}:\n")

    if not is_valid(n, limit):
        print(f"А может быть все-таки введем целое число от 1 до {limit}?")
        continue

    n = int(n)

    if n < hidden_number:
        print("Ваше число меньше загаданного, попробуйте еще разок\n")
        attempts += 1
    elif n > hidden_number:
        print("Ваше число больше загаданного, попробуйте еще разок\n")
        attempts += 1
    else:
        print(f"Вы угадали, поздравляем!\nКоличество попыток: {attempts}.\n")
        if (
            input(
                "Желаете завершить игру? '+' выйдет из цикла, при любом другом вводе продолжим:\n"
            )
            == "+"
        ):
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break
        else:
            print()
            limit = will_start()
            hidden_number = random.randint(1, limit)
            attempts = 0
