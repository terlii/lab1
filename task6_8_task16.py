# -*- coding: utf-8 -*-
"""
Задания 6-8, Задача 16: Найти минимальное из имеющихся в строке целых чисел
Вариант 3
"""

import re
import math

def find_min_integer():
    """
    Находит минимальное целое число в строке.
    
    Returns:
        int или None: Минимальное целое число или None если числа не найдены
    """
    print("=" * 60)
    print("ЗАДАНИЯ 6-8, ЗАДАЧА 16: Поиск минимального целого числа в строке")
    print("=" * 60)
    
    try:
        # Ввод строки от пользователя
        text = input("Введите строку для анализа: ")
        
        # Проверка на пустую строку
        if not text:
            print("❌ Строка пуста")
            return None
        
        print(f"\n📄 Анализируемая строка: '{text}'")
        print(f"   Длина строки: {len(text)} символов")
        
        # Поиск всех целых чисел (включая отрицательные)
        # Паттерн для поиска целых чисел: опциональный минус, затем цифры
        pattern = r'-?\b\d+\b'
        matches = re.findall(pattern, text)
        
        if not matches:
            print("❌ Целые числа в строке не найдены")
            return None
        
        # Преобразуем найденные строки в числа
        numbers = []
        invalid_numbers = []
        
        for match in matches:
            try:
                num = int(match)
                numbers.append(num)
            except ValueError:
                invalid_numbers.append(match)
        
        if not numbers:
            print("❌ Нет корректных целых чисел")
            return None
        
        # Находим минимальное число
        min_num = min(numbers)
        max_num = max(numbers)
        
        print(f"\n✅ Найдено целых чисел: {len(numbers)}")
        print(f"   Все числа: {numbers}")
        
        # Сортировка для наглядности
        sorted_numbers = sorted(numbers)
        print(f"   Отсортированные: {sorted_numbers}")
        
        print(f"\n📊 Результаты:")
        print(f"   Минимальное число: {min_num}")
        print(f"   Максимальное число: {max_num}")
        print(f"   Сумма чисел: {sum(numbers)}")
        print(f"   Среднее арифметическое: {sum(numbers)/len(numbers):.2f}")
        
        # Дополнительная информация о числах
        positive = [n for n in numbers if n > 0]
        negative = [n for n in numbers if n < 0]
        zero = [n for n in numbers if n == 0]
        
        print(f"\n📈 Статистика:")
        print(f"   Положительных: {len(positive)}")
        print(f"   Отрицательных: {len(negative)}")
        print(f"   Нулей: {len(zero)}")
        
        return min_num
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        return None

def find_numbers_with_context():
    """
    Находит числа и показывает контекст вокруг них.
    """
    print("\n" + "=" * 60)
    print("ПОИСК ЧИСЕЛ С КОНТЕКСТОМ")
    print("=" * 60)
    
    try:
        text = input("Введите текст: ")
        
        if not text:
            print("❌ Текст пуст")
            return
        
        # Паттерн для поиска чисел с контекстом (до 20 символов до и после)
        pattern = r'(.{0,20})(-?\b\d+\b)(.{0,20})'
        matches = re.findall(pattern, text)
        
        if not matches:
            print("❌ Числа не найдены")
            return
        
        print(f"\n🔍 Найдено {len(matches)} чисел с контекстом:")
        
        numbers_found = []
        for i, (before, number, after) in enumerate(matches, 1):
            num = int(number)
            numbers_found.append(num)
            print(f"\n--- Число {i}: {number} ---")
            print(f"   Контекст: ...{before}【{number}】{after}...")
            print(f"   Значение: {num}")
        
        if numbers_found:
            print(f"\n📊 Статистика по найденным числам:")
            print(f"   Минимальное: {min(numbers_found)}")
            print(f"   Максимальное: {max(numbers_found)}")
            print(f"   Среднее: {sum(numbers_found)/len(numbers_found):.2f}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def analyze_number_distribution():
    """
    Анализирует распределение чисел в тексте.
    """
    print("\n" + "=" * 60)
    print("АНАЛИЗ РАСПРЕДЕЛЕНИЯ ЧИСЕЛ")
    print("=" * 60)
    
    try:
        text = input("Введите текст: ")
        
        if not text:
            print("❌ Текст пуст")
            return
        
        # Находим все числа
        pattern = r'-?\b\d+\b'
        numbers = [int(m) for m in re.findall(pattern, text)]
        
        if not numbers:
            print("❌ Числа не найдены")
            return
        
        print(f"\n📊 РАСПРЕДЕЛЕНИЕ ЧИСЕЛ:")
        print(f"   Всего чисел: {len(numbers)}")
        
        # Диапазоны
        ranges = {
            "Отрицательные": [n for n in numbers if n < 0],
            "0-9": [n for n in numbers if 0 <= n <= 9],
            "10-99": [n for n in numbers if 10 <= n <= 99],
            "100-999": [n for n in numbers if 100 <= n <= 999],
            "1000+": [n for n in numbers if n >= 1000]
        }
        
        print(f"\n📈 По диапазонам:")
        for range_name, range_numbers in ranges.items():
            if range_numbers:
                count = len(range_numbers)
                percentage = (count / len(numbers)) * 100
                bar = '█' * int(percentage / 2)
                print(f"   {range_name:12}: {count:3d} ({percentage:5.1f}%) {bar}")
        
        # Четность
        even = [n for n in numbers if n % 2 == 0]
        odd = [n for n in numbers if n % 2 != 0]
        
        print(f"\n🔢 По четности:")
        print(f"   Четные: {len(even)} ({len(even)/len(numbers)*100:.1f}%)")
        print(f"   Нечетные: {len(odd)} ({len(odd)/len(numbers)*100:.1f}%)")
        
        # Простые числа
        prime_numbers = [n for n in numbers if n > 1 and is_prime(n)]
        if prime_numbers:
            print(f"\n🔢 Простые числа: {prime_numbers}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def is_prime(n):
    """Проверяет, является ли число простым."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def extract_all_number_types():
    """
    Извлекает числа разных типов из текста.
    """
    print("\n" + "=" * 60)
    print("ИЗВЛЕЧЕНИЕ ЧИСЕЛ РАЗНЫХ ТИПОВ")
    print("=" * 60)
    
    try:
        text = input("Введите текст: ")
        
        if not text:
            print("❌ Текст пуст")
            return
        
        # Целые числа
        integers = [int(m) for m in re.findall(r'-?\b\d+\b', text)]
        
        # Числа с плавающей точкой
        floats = [float(m) for m in re.findall(r'-?\b\d+\.\d+\b', text)]
        
        # Шестнадцатеричные числа (с префиксом 0x)
        hex_numbers = re.findall(r'\b0x[0-9a-fA-F]+\b', text)
        
        # Двоичные числа (с префиксом 0b)
        bin_numbers = re.findall(r'\b0b[01]+\b', text)
        
        print(f"\n📊 РЕЗУЛЬТАТЫ:")
        print(f"   Целые числа: {len(integers)}")
        if integers:
            print(f"      Минимальное: {min(integers)}")
            print(f"      Максимальное: {max(integers)}")
            print(f"      Все: {integers[:10]}{'...' if len(integers) > 10 else ''}")
        
        print(f"\n   Числа с плавающей точкой: {len(floats)}")
        if floats:
            print(f"      Минимальное: {min(floats)}")
            print(f"      Максимальное: {max(floats)}")
            print(f"      Все: {floats[:10]}{'...' if len(floats) > 10 else ''}")
        
        print(f"\n   Шестнадцатеричные: {len(hex_numbers)}")
        if hex_numbers:
            print(f"      {', '.join(hex_numbers)}")
        
        print(f"\n   Двоичные: {len(bin_numbers)}")
        if bin_numbers:
            print(f"      {', '.join(bin_numbers)}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def find_numbers_in_phrases():
    """
    Находит числа в составе фраз и выражений.
    """
    print("\n" + "=" * 60)
    print("ПОИСК ЧИСЕЛ В СОСТАВЕ ФРАЗ")
    print("=" * 60)
    
    try:
        text = input("Введите текст: ")
        
        if not text:
            print("❌ Текст пуст")
            return
        
        # Поиск фраз вида "число + слово"
        number_word_pattern = r'(\d+)\s+([а-яА-Яa-zA-Z]+)'
        number_word_pairs = re.findall(number_word_pattern, text)
        
        if number_word_pairs:
            print(f"\n📝 Числа со следующими за ними словами:")
            for num, word in number_word_pairs[:10]:
                print(f"   {num} → {word}")
        
        # Поиск выражений вида "число + знак + число"
        expression_pattern = r'(\d+)\s*([+\-*/])\s*(\d+)'
        expressions = re.findall(expression_pattern, text)
        
        if expressions:
            print(f"\n🧮 Математические выражения:")
            for num1, op, num2 in expressions:
                print(f"   {num1} {op} {num2}")
        
        # Поиск диапазонов вида "число-число"
        range_pattern = r'(\d+)\s*[-–—]\s*(\d+)'
        ranges = re.findall(range_pattern, text)
        
        if ranges:
            print(f"\n📏 Диапазоны:")
            for start, end in ranges:
                print(f"   от {start} до {end}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def demonstrate_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ НА ПРИМЕРАХ")
    print("=" * 60)
    
    examples = [
        "В комнате было 5 стульев, 3 стола и 10 книг.",
        "Температура: -15 градусов, влажность: 80%",
        "Цены: 99, 150, 75, 2000 рублей",
        "Смешанный текст с числами 42 и -7 и 0",
        "Без чисел совсем",
        "Отрицательные: -5, -10, -3, -8"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n--- Пример {i} ---")
        print(f"Текст: '{example}'")
        
        # Поиск чисел
        pattern = r'-?\b\d+\b'
        numbers = re.findall(pattern, example)
        
        if numbers:
            int_numbers = [int(n) for n in numbers]
            print(f"Найденные числа: {numbers}")
            print(f"Минимальное: {min(int_numbers)}")
            print(f"Максимальное: {max(int_numbers)}")
        else:
            print("Числа не найдены")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("=" * 60)
        print("1 - Поиск минимального целого числа (основной)")
        print("2 - Поиск чисел с контекстом")
        print("3 - Анализ распределения чисел")
        print("4 - Извлечение чисел разных типов")
        print("5 - Поиск чисел в составе фраз")
        print("6 - Демонстрация на примерах")
        print("7 - Выйти")
        
        choice = input("Ваш выбор (1-7): ").strip()
        
        if choice == "1":
            find_min_integer()
        
        elif choice == "2":
            find_numbers_with_context()
        
        elif choice == "3":
            analyze_number_distribution()
        
        elif choice == "4":
            extract_all_number_types()
        
        elif choice == "5":
            find_numbers_in_phrases()
        
        elif choice == "6":
            demonstrate_examples()
        
        elif choice == "7":
            print("Программа завершена. До свидания!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 7")

if __name__ == "__main__":
    main()