# -*- coding: utf-8 -*-
"""
Задания 11-14, Задача 3: Сортировка строк в порядке увеличения разницы между 
частотой наиболее часто встречаемого символа в строке и частотой его появления в алфавите
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
    print("ЗАДАНИЯ 11-14, ЗАДАЧА 3: Ввод списка строк")
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

def char_frequency(s):
    """
    Вычисляет частоту символов в строке.
    
    Args:
        s (str): Исходная строка
        
    Returns:
        dict: Словарь с частотами символов
    """
    if not s:
        return {}
    
    # Приводим к нижнему регистру для единообразия
    s_lower = s.lower()
    length = len(s_lower)
    
    # Считаем количество каждого символа
    counter = Counter(s_lower)
    
    # Преобразуем в частоты
    frequencies = {char: count / length for char, count in counter.items()}
    
    return frequencies

def get_most_frequent_char_info(s):
    """
    Получает информацию о наиболее частом символе в строке.
    
    Args:
        s (str): Исходная строка
        
    Returns:
        tuple: (самый_частый_символ, его_частота, разница_с_алфавитом)
    """
    if not s:
        return None, 0, 0
    
    freq = char_frequency(s)
    
    if not freq:
        return None, 0, 0
    
    # Находим символ с максимальной частотой
    most_common_char = max(freq, key=freq.get)
    most_common_freq = freq[most_common_char]
    
    # Частота символа в алфавите (для латиницы - 1/26, для кириллицы - 1/33)
    # Определяем алфавит по символу
    if 'a' <= most_common_char <= 'z':
        alphabet_freq = 1 / 26  # латиница
    elif 'а' <= most_common_char <= 'я':
        alphabet_freq = 1 / 33  # кириллица
    else:
        # Для небуквенных символов используем 0
        alphabet_freq = 0
    
    diff = abs(most_common_freq - alphabet_freq)
    
    return most_common_char, most_common_freq, diff

def calculate_sort_key(s):
    """
    Вычисляет ключ сортировки для строки.
    
    Args:
        s (str): Исходная строка
        
    Returns:
        float: Разница между частотой самого частого символа и частотой в алфавите
    """
    _, _, diff = get_most_frequent_char_info(s)
    return diff

def sort_strings(strings):
    """
    Сортирует строки по заданному критерию.
    
    Args:
        strings (list): Исходный список строк
        
    Returns:
        list: Отсортированный список строк
    """
    if not strings:
        return []
    
    # Создаем список кортежей (строка, ключ сортировки)
    strings_with_keys = [(s, calculate_sort_key(s)) for s in strings]
    
    # Сортируем по ключу
    sorted_strings_with_keys = sorted(strings_with_keys, key=lambda x: x[1])
    
    # Извлекаем только строки
    sorted_strings = [item[0] for item in sorted_strings_with_keys]
    
    return sorted_strings

def display_strings_with_stats(strings, title="СПИСОК СТРОК"):
    """
    Отображает строки с их статистикой.
    
    Args:
        strings (list): Список строк для отображения
        title (str): Заголовок
    """
    if not strings:
        print("   Список пуст")
        return
    
    print(f"\n{title}:")
    print("=" * 80)
    
    for i, s in enumerate(strings, 1):
        most_common_char, freq, diff = get_most_frequent_char_info(s)
        
        print(f"{i:2}. '{s}'")
        
        if most_common_char:
            # Определяем алфавит
            if 'a' <= most_common_char <= 'z':
                alphabet = "латиница"
                alphabet_freq = 1/26
            elif 'а' <= most_common_char <= 'я':
                alphabet = "кириллица"
                alphabet_freq = 1/33
            else:
                alphabet = "другое"
                alphabet_freq = 0
            
            print(f"     Самый частый символ: '{most_common_char}'")
            print(f"     Его частота: {freq:.4f}")
            print(f"     Частота в алфавите ({alphabet}): {alphabet_freq:.4f}")
            print(f"     Разница: {diff:.4f}")
            
            # Визуализация разницы
            bar_length = int(diff * 50)
            bar = '█' * bar_length
            print(f"     {bar} {diff:.4f}")
        else:
            print("     Нет символов для анализа")
        
        print()
    
    print("=" * 80)

def analyze_strings(strings):
    """
    Проводит анализ списка строк.
    
    Args:
        strings (list): Список строк для анализа
    """
    if not strings:
        return
    
    print("\n" + "=" * 60)
    print("АНАЛИЗ СПИСКА СТРОК")
    print("=" * 60)
    
    # Собираем статистику по всем строкам
    stats = []
    for s in strings:
        most_common_char, freq, diff = get_most_frequent_char_info(s)
        if most_common_char:
            stats.append({
                'string': s,
                'char': most_common_char,
                'freq': freq,
                'diff': diff
            })
    
    if not stats:
        print("❌ Нет данных для анализа")
        return
    
    print(f"\n📊 ОБЩАЯ СТАТИСТИКА:")
    print(f"   Всего строк: {len(strings)}")
    print(f"   Строк с данными: {len(stats)}")
    
    # Статистика по разницам
    diffs = [s['diff'] for s in stats]
    print(f"\n📈 РАСПРЕДЕЛЕНИЕ РАЗНИЦ:")
    print(f"   Минимальная разница: {min(diffs):.4f}")
    print(f"   Максимальная разница: {max(diffs):.4f}")
    print(f"   Средняя разница: {sum(diffs) / len(diffs):.4f}")
    
    # Гистограмма разниц
    print(f"\n📊 ГИСТОГРАММА РАЗНИЦ:")
    diff_ranges = [(0, 0.1), (0.1, 0.2), (0.2, 0.3), (0.3, 0.4), (0.4, 0.5), (0.5, 1.0)]
    for low, high in diff_ranges:
        count = sum(1 for d in diffs if low <= d < high)
        if count > 0:
            bar = '█' * count
            print(f"   {low:.1f}-{high:.1f}: {count:2d} строк {bar}")
    
    # Самые частые символы
    print(f"\n🏆 САМЫЕ ЧАСТЫЕ СИМВОЛЫ:")
    char_counts = {}
    for s in stats:
        char = s['char']
        char_counts[char] = char_counts.get(char, 0) + 1
    
    for char, count in sorted(char_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"   '{char}': встречается в {count} строках")

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
        most_common_char, freq, diff = get_most_frequent_char_info(s)
        print(f"{i:2}. '{s}'")
        print(f"     Самый частый: '{most_common_char}' (частота {freq:.3f}, разница {diff:.3f})")
    
    sorted_examples = sort_strings(examples)
    
    print(f"\n📊 Отсортировано по разнице (возрастание):")
    for i, s in enumerate(sorted_examples, 1):
        most_common_char, freq, diff = get_most_frequent_char_info(s)
        print(f"{i:2}. (разница {diff:.3f}) '{s}'")

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
    
    while True:
        print("\n" + "-" * 40)
        print("ВЫБЕРИТЕ ДЕЙСТВИЕ:")
        print("1 - Показать исходный список со статистикой")
        print("2 - Сортировать по разнице с алфавитом")
        print("3 - Показать отсортированный список")
        print("4 - Анализ списка")
        print("5 - Сравнить исходный и отсортированный")
        print("6 - Добавить новую строку")
        print("7 - Удалить строку")
        print("8 - Вернуться в главное меню")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            display_strings_with_stats(strings, "ИСХОДНЫЙ СПИСОК")
        
        elif choice == "2":
            sorted_strings = sort_strings(strings)
            print("✅ Строки отсортированы")
            # Не сохраняем сортировку, только показываем
        
        elif choice == "3":
            sorted_strings = sort_strings(strings)
            display_strings_with_stats(sorted_strings, "ОТСОРТИРОВАННЫЙ СПИСОК")
        
        elif choice == "4":
            analyze_strings(strings)
        
        elif choice == "5":
            sorted_strings = sort_strings(strings)
            
            print("\n📊 СРАВНЕНИЕ:")
            print("-" * 60)
            print("Исходный порядок -> Отсортированный порядок")
            print("-" * 60)
            
            for i, (orig, sorted_s) in enumerate(zip(strings, sorted_strings), 1):
                orig_diff = calculate_sort_key(orig)
                sorted_diff = calculate_sort_key(sorted_s)
                print(f"{i:2}. '{orig[:30]}' ({orig_diff:.3f})")
                print(f"    -> '{sorted_s[:30]}' ({sorted_diff:.3f})")
                print()
        
        elif choice == "6":
            new_string = input("Введите новую строку: ")
            if new_string:
                strings.append(new_string)
                print(f"✅ Строка добавлена. Всего строк: {len(strings)}")
        
        elif choice == "7":
            display_strings_with_stats(strings, "ТЕКУЩИЙ СПИСОК")
            try:
                idx = int(input("Введите номер строки для удаления: ")) - 1
                if 0 <= idx < len(strings):
                    removed = strings.pop(idx)
                    print(f"✅ Удалена строка: '{removed}'")
                else:
                    print("❌ Неверный номер")
            except ValueError:
                print("❌ Ошибка: введите число")
        
        elif choice == "8":
            break
        
        else:
            print("❌ Неверный выбор")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ЗАДАНИЯ 11-14, ЗАДАЧА 3: Сортировка по разнице с частотой в алфавите")
        print("=" * 60)
        print("\nВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("1 - Основной режим (ввод и сортировка)")
        print("2 - Интерактивный режим")
        print("3 - Демонстрация на примерах")
        print("4 - Выйти")
        
        choice = input("Ваш выбор (1-4): ").strip()
        
        if choice == "1":
            # Основной режим
            strings = read_strings()
            
            if strings:
                print("\n" + "=" * 60)
                print("РЕЗУЛЬТАТЫ")
                print("=" * 60)
                
                display_strings_with_stats(strings, "ИСХОДНЫЙ СПИСОК")
                
                sorted_strings = sort_strings(strings)
                display_strings_with_stats(sorted_strings, "ОТСОРТИРОВАННЫЙ СПИСОК")
                
                analyze_strings(strings)
        
        elif choice == "2":
            interactive_mode()
        
        elif choice == "3":
            demonstrate_with_examples()
        
        elif choice == "4":
            print("Программа завершена. До свидания!")
            break
        
        else:
            print("❌ Неверный выбор. Пожалуйста, введите 1, 2, 3 или 4")

if __name__ == "__main__":
    main()