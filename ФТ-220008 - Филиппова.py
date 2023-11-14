import random
import logging

# Инициализация логгера
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def extract_numbers(n):
    """
    Функция для вытаскивания чисел из мешка
    """
    numbers = list(range(1, n + 1))  # Генерируем список чисел от 1 до N
    random.shuffle(numbers)  # Перемешиваем список
    return numbers


def main():
    try:
        n = int(input('Введите число N: '))
        logging.info(f"Введено число N: {n}")
        if n <= 0:
            raise ValueError("Число N должно быть больше нуля!")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        logging.error(f"Ошибка ввода: {e}")
        return

    numbers = extract_numbers(n)

    for number in numbers:
        input(f"Вытянут бочонок с номером {number}. Нажмите Enter, чтобы продолжить...")
        logging.info(f"Вытянут бочонок с номером {number}")

    print("Все бочонки вытянуты!")


if __name__ == '__main__':
    main()