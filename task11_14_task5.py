# -*- coding: utf-8 -*-
"""
Задания 11-14, Задача 5: Сортировка в порядке увеличения квадратичного отклонения
частоты встречаемости самого часто встречаемого в строке символа от частоты
его встречаемости в текстах на этом алфавите
Вариант 3
"""

import math
from collections import Counter

def read_strings():
    """
    Читает список строк с клавиатуры.
    
    Returns:
        list: Список введенных строк
    """
    print("=" * 60)
    print("ЗАДАНИЯ 11-14, ЗАДАЧА 5: Ввод списка строк")
    print("=" * 60)
    
    print("\n📝 Введите строки (по одной в строке).")
    print("   Для завершения ввода оставьте строку пустой и нажмите Enter")
    print("-" * 40)
    
    strings = []
    line_number = 1
    
    while True:
        line = input(f"Строка {line_number}: ")
        if not line:  # Пустая строка - завершение ввода
            break
        strings.append(line)
        line_number += 1
    
    if not strings:
        print("\n❌ Список строк пуст")
        return []
    
    print(f"\n✅ Введено строк: {len(strings)}")
    return strings

def calculate_alphabet_frequencies(strings):
    """
    Вычисляет частоты символов во всех строках (эталонные частоты).
    
    Args:
        strings (list): Список строк
        
    Returns:
        dict: Словарь с частотами символов
    """
    # Объединяем все строки
    all_text = ''.join(strings).lower()
    
    if not all_text:
        return {}
    
    total_chars = len(all_text)
    counter = Counter(all_text)
    
    # Вычисляем частоты
    frequencies = {char: count / total_chars for char, count in counter.items()}
    
    return frequencies

def char_frequency_in_string(s):
    """
    Вычисляет частоту символов в отдельной строке.
    
    Args:
        s (str): Исходная строка
        
    Returns:
        dict: Словарь с частотами символов
    """
    if not s:
        return {}
    
    s_lower = s.lower()
    length = len(s_lower)
    counter = Counter(s_lower)
    
    frequencies = {char: count / length for char, count in counter.items()}
    
    return frequencies

def get_most_frequent_char_info(s):
    """
    Получает информацию о наиболее частом символе в строке.
    
    Args:
        s (str): Исходная строка
        
    Returns:
        tuple: (самый_частый_символ, его_частота)
    """
    if not s:
        return None, 0
    
    freq = char_frequency_in_string(s)
    
    if not freq:
        return None, 0
    
    most_common_char = max(freq, key=freq.get)
    most_common_freq = freq[most_common_char]
    
    return most_common_char, most_common_freq

def calculate_quadratic_deviation(s, reference_frequencies):
    """
    Вычисляет квадратичное отклонение для строки.
    
    Args:
        s (str): Исходная строка
        reference_frequencies (dict): Эталонные частоты
        
    Returns:
        float: Квадратичное отклонение
    """
    if not s or not reference_frequencies:
        return 0
    
    most_common_char, freq_in_string = get_most_frequent_char_info(s)
    
    if not most_common_char:
        return 0
    
    # Частота этого символа в эталонном распределении
    freq_in_reference = reference_frequencies.get(most_common_char, 0)
    
    # Квадратичное отклонение
    deviation = (freq_in_string - freq_in_reference) ** 2
    
    return deviation

def calculate_sort_key(s, reference_frequencies):
    """
    Вычисляет ключ сортировки для строки.
    
    Args:
        s (str): Исходная строка
        reference_frequencies (dict): Эталонные частоты
        
    Returns:
        float: Квадратичное отклонение
    """
    return calculate_quadratic_deviation(s, reference_frequencies)

def sort_strings(strings, reference_frequencies):
    """
    Сортирует строки по заданному критерию.
    
    Args:
        strings (list): Исходный список строк
        reference_frequencies (dict): Эталонные частоты
        
    Returns:
        list: Отсортированный список строк
    """
    if not strings:
        return []
    
    # Создаем список кортежей (строка, ключ сортировки)
    strings_with_keys = [(s, calculate_sort_key(s, reference_frequencies)) for s in strings]
    
    # Сортируем по ключу
    sorted_strings_with_keys = sorted(strings_with_keys, key=lambda x: x[1])
    
    # Извлекаем только строки
    sorted_strings = [item[0] for item in sorted_strings_with_keys]
    
    return sorted_strings

def display_strings_with_stats(strings, reference_frequencies, title="СПИСОК СТРОК"):
    """
    Отображает строки с их статистикой.
    
    Args:
        strings (list): Список строк для отображения
        reference_frequencies (dict): Эталонные частоты
        title (str): Заголовок
    """
    if not strings:
        print("   Список пуст")
        return
    
    print(f"\n{title}:")
    print("=" * 90)
    
    for i, s in enumerate(strings, 1):
        most_common_char, freq_in_string = get_most_frequent_char_info(s)
        
        print(f"{i:2}. '{s}'")
        
        if most_common_char and reference_frequencies:
            freq_in_reference = reference_frequencies.get(most_common_char, 0)
            deviation = (freq_in_string - freq_in_reference) ** 2
            
            print(f"     Самый частый символ: '{most_common_char}'")
            print(f"     Частота в строке: {freq_in_string:.4f}")
            print(f"     Частота в эталоне: {freq_in_reference:.4f}")
            print(f"     Квадратичное отклонение: {deviation:.6f}")
            
            # Визуализация отклонения
            bar_length = int(deviation * 1000)
            bar = '█' * min(bar_length, 50)
            print(f"     {bar} {deviation:.6f}")
        else:
            print("     Нет данных для анализа")
        
        print()
    
    print("=" * 90)

def analyze_strings(strings, reference_frequencies):
    """
    Проводит анализ списка строк.
    
    Args:
        strings (list): Список строк для анализа
        reference_frequencies (dict): Эталонные частоты
    """
    if not strings:
        return
    
    print("\n" + "=" * 60)
    print("АНАЛИЗ СПИСКА СТРОК")
    print("=" * 60)
    
    # Эталонные частоты
    print(f"\n📊 ЭТАЛОННЫЕ ЧАСТОТЫ (по всем строкам):")
    total_chars = sum(len(s) for s in strings)
    print(f"   Всего символов: {total_chars}")
    print(f"   Уникальных символов: {len(reference_frequencies)}")
    
    # Топ-10 самых частых символов в эталоне
    sorted_ref = sorted(reference_frequencies.items(), key=lambda x: x[1], reverse=True)[:10]
    print(f"\n🏆 ТОП-10 СИМВОЛОВ В ЭТАЛОНЕ:")
    for char, freq in sorted_ref:
        bar = '█' * int(freq * 50)
        print(f"   '{char}': {freq:.4f} {bar}")
    
    # Статистика по отклонениям
    deviations = []
    for s in strings:
        most_common_char, freq_in_string = get_most_frequent_char_info(s)
        if most_common_char:
            freq_in_reference = reference_frequencies.get(most_common_char, 0)
            deviation = (freq_in_string - freq_in_reference) ** 2
            deviations.append(deviation)
    
    if deviations:
        print(f"\n📈 СТАТИСТИКА ОТКЛОНЕНИЙ:")
        print(f"   Минимальное отклонение: {min(deviations):.6f}")
        print(f"   Максимальное отклонение: {max(deviations):.6f}")
        print(f"   Среднее отклонение: {sum(deviations) / len(deviations):.6f}")
        
        # Гистограмма отклонений
        print(f"\n📊 ГИСТОГРАММА ОТКЛОНЕНИЙ:")
        deviation_ranges = [(0, 0.01), (0.01, 0.05), (0.05, 0.1), (0.1, 0.2), (0.2, 0.5)]
        for low, high in deviation_ranges:
            count = sum(1 for d in deviations if low <= d < high)
            if count > 0:
                bar = '█' * count
                print(f"   {low:.2f}-{high:.2f}: {count:2d} строк {bar}")

def demonstrate_with_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ НА ПРИМЕРАХ")
    print("=" * 60)
    
    examples = [
        "aaaaa bbbbb ccccc",  # Очень частая 'a'
        "abcde fghij klmno",   # Равномерное распределение
        "aaa bbb ccc ddd eee", # Несколько частых символов
        "Hello World!",         # Смешанный текст
        "Python Programming",   # Английский текст
        "Привет мир",          # Русский текст
        "ааааа ббббб ввввв"    # Частые русские буквы
    ]
    
    print("\n📋 Исходные строки:")
    for i, s in enumerate(examples, 1):
        most_common_char, freq = get_most_frequent_char_info(s)
        print(f"{i:2}. '{s}'")
        print(f"     Самый частый: '{most_common_char}' (частота {freq:.3f})")
    
    # Вычисляем эталонные частоты
    reference_freq = calculate_alphabet_frequencies(examples)
    
    print(f"\n📊 Эталонные частоты (по всем примерам):")
    for char, freq in sorted(reference_freq.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"   '{char}': {freq:.4f}")
    
    sorted_examples = sort_strings(examples, reference_freq)
    
    print(f"\n📊 Отсортировано по квадратичному отклонению (возрастание):")
    for i, s in enumerate(sorted_examples, 1):
        deviation = calculate_quadratic_deviation(s, reference_freq)
        print(f"{i:2}. (отклонение {deviation:.6f}) '{s}'")

def compare_with_different_references():
    """
    Сравнивает сортировку с разными эталонными частотами.
    """
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ С РАЗНЫМИ ЭТАЛОНАМИ")
    print("=" * 60)
    
    # Тестовые строки
    test_strings = [
        "aaaaa bbbbb",
        "abcde fghij",
        "Hello World",
        "Python Code"
    ]
    
    # Разные эталоны
    print("\n📚 ВЫБЕРИТЕ ЭТАЛОН:")
    print("1 - Частоты из самих строк")
    print("2 - Равномерное распределение (латиница)")
    print("3 - Равномерное распределение (кириллица)")
    print("4 - Частоты английского языка")
    
    choice = input("Ваш выбор (1-4): ").strip()
    
    if choice == "1":
        reference_freq = calculate_alphabet_frequencies(test_strings)
        print("\n✅ Используются частоты из самих строк")
    
    elif choice == "2":
        reference_freq = {chr(c): 1/26 for c in range(ord('a'), ord('z')+1)}
        print("\n✅ Используется равномерное распределение для латиницы")
    
    elif choice == "3":
        # Кириллица (приблизительно)
        cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        reference_freq = {c: 1/len(cyrillic) for c in cyrillic}
        print("\n✅ Используется равномерное распределение для кириллицы")
    
    elif choice == "4":
        # Приблизительные частоты букв в английском языке
        english_freq = {
            'e': 0.127, 't': 0.091, 'a': 0.082, 'o': 0.075, 'i': 0.070,
            'n': 0.067, 's': 0.063, 'h': 0.061, 'r': 0.060, 'd': 0.043
        }
        reference_freq = english_freq
        print("\n✅ Используются частоты английского языка")
    
    else:
        print("❌ Неверный выбор")
        return
    
    print(f"\n📊 Эталонные частоты:")
    for char, freq in sorted(reference_freq.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"   '{char}': {freq:.4f}")
    
    print(f"\n📊 Результаты сортировки:")
    sorted_strings = sort_strings(test_strings, reference_freq)
    
    for i, s in enumerate(sorted_strings, 1):
        deviation = calculate_quadratic_deviation(s, reference_freq)
        most_common_char, freq = get_most_frequent_char_info(s)
        print(f"{i:2}. (откл. {deviation:.6f}) '{s}' - самый частый '{most_common_char}' ({freq:.3f})")

def interactive_mode():
    """
    Интерактивный режим с дополнительными возможностями.
    """
    print("\n" + "=" * 60)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("=" * 60)
    
    strings = read_strings()
    
    if not strings:
        return
    
    # Вычисляем эталонные частоты
    reference_freq = calculate_alphabet_frequencies(strings)
    
    while True:
        print("\n" + "-" * 40)
        print("ВЫБЕРИТЕ ДЕЙСТВИЕ:")
        print("1 - Показать исходный список со статистикой")
        print("2 - Показать эталонные частоты")
        print("3 - Сортировать по отклонению")
        print("4 - Показать отсортированный список")
        print("5 - Анализ списка")
        print("6 - Сравнить исходный и отсортированный")
        print("7 - Добавить новую строку")
        print("8 - Пересчитать эталонные частоты")
        print("9 - Вернуться в главное меню")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            display_strings_with_stats(strings, reference_freq, "ИСХОДНЫЙ СПИСОК")
        
        elif choice == "2":
            print("\n📊 ЭТАЛОННЫЕ ЧАСТОТЫ:")
            for char, freq in sorted(reference_freq.items(), key=lambda x: x[1], reverse=True):
                bar = '█' * int(freq * 50)
                print(f"   '{char}': {freq:.4f} {bar}")
        
        elif choice == "3":
            sorted_strings = sort_strings(strings, reference_freq)
            print("✅ Строки отсортированы")
        
        elif choice == "4":
            sorted_strings = sort_strings(strings, reference_freq)
            display_strings_with_stats(sorted_strings, reference_freq, "ОТСОРТИРОВАННЫЙ СПИСОК")
        
        elif choice == "5":
            analyze_strings(strings, reference_freq)
        
        elif choice == "6":
            sorted_strings = sort_strings(strings, reference_freq)
            
            print("\n📊 СРАВНЕНИЕ:")
            print("-" * 70)
            print("Исходный порядок -> Отсортированный порядок")
            print("-" * 70)
            
            for i, (orig, sorted_s) in enumerate(zip(strings, sorted_strings), 1):
                orig_dev = calculate_quadratic_deviation(orig, reference_freq)
                sorted_dev = calculate_quadratic_deviation(sorted_s, reference_freq)
                print(f"{i:2}. '{orig[:20]}' ({orig_dev:.6f})")
                print(f"    -> '{sorted_s[:20]}' ({sorted_dev:.6f})")
                print()
        
        elif choice == "7":
            new_string = input("Введите новую строку: ")
            if new_string:
                strings.append(new_string)
                # Пересчитываем эталонные частоты
                reference_freq = calculate_alphabet_frequencies(strings)
                print(f"✅ Строка добавлена. Всего строк: {len(strings)}")
                print("✅ Эталонные частоты пересчитаны")
        
        elif choice == "8":
            reference_freq = calculate_alphabet_frequencies(strings)
            print("✅ Эталонные частоты пересчитаны")
        
        elif choice == "9":
            break
        
        else:
            print("❌ Неверный выбор")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ЗАДАНИЯ 11-14, ЗАДАЧА 5: Сортировка по отклонению от частоты в текстах")
        print("=" * 60)
        print("\nВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("1 - Основной режим (ввод и сортировка)")
        print("2 - Интерактивный режим")
        print("3 - Демонстрация на примерах")
        print("4 - Сравнение с разными эталонами")
        print("5 - Выйти")
        
        choice = input("Ваш выбор (1-5): ").strip()
        
        if choice == "1":
            # Основной режим
            strings = read_strings()
            
            if strings:
                print("\n" + "=" * 60)
                print("РЕЗУЛЬТАТЫ")
                print("=" * 60)
                
                # Вычисляем эталонные частоты
                reference_freq = calculate_alphabet_frequencies(strings)
                
                display_strings_with_stats(strings, reference_freq, "ИСХОДНЫЙ СПИСОК")
                
                sorted_strings = sort_strings(strings, reference_freq)
                display_strings_with_stats(sorted_strings, reference_freq, "ОТСОРТИРОВАННЫЙ СПИСОК")
                
                analyze_strings(strings, reference_freq)
        
        elif choice == "2":
            interactive_mode()
        
        elif choice == "3":
            demonstrate_with_examples()
        
        elif choice == "4":
            compare_with_different_references()
        
        elif choice == "5":
            print("Программа завершена. До свидания!")
            break
        
        else:
            print("❌ Неверный выбор. Пожалуйста, введите 1, 2, 3, 4 или 5")

if __name__ == "__main__":
    main()