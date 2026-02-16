# -*- coding: utf-8 -*-
"""
Задания 11-14, Задача 12: Сортировка в порядке увеличения квадратичного отклонения
частоты встречаемости самого распространенного символа в наборе строк 
от частоты его встречаемости в данной строке
Вариант 3
"""

from collections import Counter
import math

def read_strings():
    """
    Читает список строк с клавиатуры.
    
    Returns:
        list: Список введенных строк
    """
    print("=" * 60)
    print("ЗАДАНИЯ 11-14, ЗАДАЧА 12: Ввод списка строк")
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

def find_most_common_char_in_set(strings):
    """
    Находит самый распространенный символ во всем наборе строк.
    
    Args:
        strings (list): Список строк
        
    Returns:
        tuple: (самый_частый_символ, его_частота_в_наборе)
    """
    if not strings:
        return None, 0
    
    # Объединяем все строки
    all_text = ''.join(strings).lower()
    
    if not all_text:
        return None, 0
    
    # Считаем частоту символов
    counter = Counter(all_text)
    total_chars = len(all_text)
    
    # Находим самый частый символ
    most_common_char = counter.most_common(1)[0][0]
    most_common_count = counter[most_common_char]
    
    # Частота в наборе
    frequency_in_set = most_common_count / total_chars
    
    return most_common_char, frequency_in_set

def char_frequency_in_string(s, char):
    """
    Вычисляет частоту конкретного символа в строке.
    
    Args:
        s (str): Исходная строка
        char (str): Искомый символ
        
    Returns:
        float: Частота символа в строке
    """
    if not s:
        return 0
    
    s_lower = s.lower()
    count = s_lower.count(char.lower())
    
    if count == 0:
        return 0
    
    return count / len(s_lower)

def calculate_quadratic_deviation(s, target_char, target_freq):
    """
    Вычисляет квадратичное отклонение для строки.
    
    Args:
        s (str): Исходная строка
        target_char (str): Целевой символ
        target_freq (float): Целевая частота
        
    Returns:
        float: Квадратичное отклонение
    """
    if not s or not target_char:
        return 0
    
    freq_in_string = char_frequency_in_string(s, target_char)
    
    # Квадратичное отклонение
    deviation = (freq_in_string - target_freq) ** 2
    
    return deviation

def calculate_sort_key(s, target_char, target_freq):
    """
    Вычисляет ключ сортировки для строки.
    
    Args:
        s (str): Исходная строка
        target_char (str): Целевой символ
        target_freq (float): Целевая частота
        
    Returns:
        float: Квадратичное отклонение
    """
    return calculate_quadratic_deviation(s, target_char, target_freq)

def sort_strings(strings, target_char, target_freq):
    """
    Сортирует строки по заданному критерию.
    
    Args:
        strings (list): Исходный список строк
        target_char (str): Целевой символ
        target_freq (float): Целевая частота
        
    Returns:
        list: Отсортированный список строк
    """
    if not strings:
        return []
    
    # Создаем список кортежей (строка, ключ сортировки)
    strings_with_keys = [(s, calculate_sort_key(s, target_char, target_freq)) for s in strings]
    
    # Сортируем по ключу
    sorted_strings_with_keys = sorted(strings_with_keys, key=lambda x: x[1])
    
    # Извлекаем только строки
    sorted_strings = [item[0] for item in sorted_strings_with_keys]
    
    return sorted_strings

def display_strings_with_stats(strings, target_char, target_freq, title="СПИСОК СТРОК"):
    """
    Отображает строки с их статистикой.
    
    Args:
        strings (list): Список строк для отображения
        target_char (str): Целевой символ
        target_freq (float): Целевая частота
        title (str): Заголовок
    """
    if not strings:
        print("   Список пуст")
        return
    
    print(f"\n{title}:")
    print("=" * 90)
    print(f"🎯 Целевой символ: '{target_char}' (частота в наборе: {target_freq:.4f})")
    print("=" * 90)
    
    for i, s in enumerate(strings, 1):
        freq_in_string = char_frequency_in_string(s, target_char)
        deviation = (freq_in_string - target_freq) ** 2
        
        print(f"{i:2}. '{s}'")
        print(f"     Длина строки: {len(s)} символов")
        print(f"     Вхождений '{target_char}': {s.lower().count(target_char)}")
        print(f"     Частота в строке: {freq_in_string:.4f}")
        print(f"     Квадратичное отклонение: {deviation:.6f}")
        
        # Визуализация отклонения
        bar_length = int(deviation * 1000)
        bar = '█' * min(bar_length, 50)
        
        if freq_in_string > target_freq:
            arrow = "↑"
        elif freq_in_string < target_freq:
            arrow = "↓"
        else:
            arrow = "="
        
        print(f"     {arrow} {bar} {deviation:.6f}")
        print()
    
    print("=" * 90)

def analyze_strings(strings, target_char, target_freq):
    """
    Проводит анализ списка строк.
    
    Args:
        strings (list): Список строк для анализа
        target_char (str): Целевой символ
        target_freq (float): Целевая частота
    """
    if not strings:
        return
    
    print("\n" + "=" * 60)
    print("АНАЛИЗ СПИСКА СТРОК")
    print("=" * 60)
    
    print(f"\n🎯 Анализ для символа '{target_char}' (частота в наборе: {target_freq:.4f})")
    
    # Собираем статистику
    stats = []
    for s in strings:
        freq = char_frequency_in_string(s, target_char)
        deviation = (freq - target_freq) ** 2
        stats.append({
            'string': s,
            'freq': freq,
            'deviation': deviation,
            'count': s.lower().count(target_char)
        })
    
    # Статистика по отклонениям
    deviations = [s['deviation'] for s in stats]
    frequencies = [s['freq'] for s in stats]
    
    print(f"\n📊 СТАТИСТИКА ОТКЛОНЕНИЙ:")
    print(f"   Минимальное отклонение: {min(deviations):.6f}")
    print(f"   Максимальное отклонение: {max(deviations):.6f}")
    print(f"   Среднее отклонение: {sum(deviations) / len(deviations):.6f}")
    
    print(f"\n📈 СТАТИСТИКА ЧАСТОТ:")
    print(f"   Минимальная частота: {min(frequencies):.4f}")
    print(f"   Максимальная частота: {max(frequencies):.4f}")
    print(f"   Средняя частота: {sum(frequencies) / len(frequencies):.4f}")
    
    # Гистограмма отклонений
    print(f"\n📊 ГИСТОГРАММА ОТКЛОНЕНИЙ:")
    deviation_ranges = [(0, 0.01), (0.01, 0.05), (0.05, 0.1), (0.1, 0.2), (0.2, 0.5)]
    for low, high in deviation_ranges:
        count = sum(1 for d in deviations if low <= d < high)
        if count > 0:
            bar = '█' * count
            print(f"   {low:.2f}-{high:.2f}: {count:2d} строк {bar}")
    
    # Строки с максимальным и минимальным отклонением
    max_dev = max(deviations)
    min_dev = min(deviations)
    
    print(f"\n🏆 СТРОКИ С МАКСИМАЛЬНЫМ ОТКЛОНЕНИЕМ ({max_dev:.6f}):")
    for s in stats:
        if s['deviation'] == max_dev:
            direction = "выше" if s['freq'] > target_freq else "ниже"
            print(f"   • '{s['string']}' - частота {s['freq']:.4f} ({direction} на {abs(s['freq'] - target_freq):.4f})")
    
    print(f"\n🥇 СТРОКИ С МИНИМАЛЬНЫМ ОТКЛОНЕНИЕМ ({min_dev:.6f}):")
    for s in stats:
        if s['deviation'] == min_dev:
            print(f"   • '{s['string']}' - частота {s['freq']:.4f}")

def find_all_common_chars(strings):
    """
    Находит все частые символы в наборе.
    
    Args:
        strings (list): Список строк
        
    Returns:
        list: Список кортежей (символ, частота)
    """
    if not strings:
        return []
    
    all_text = ''.join(strings).lower()
    total_chars = len(all_text)
    counter = Counter(all_text)
    
    # Возвращаем топ-5 символов
    return [(char, count / total_chars) for char, count in counter.most_common(5)]

def compare_multiple_targets(strings):
    """
    Сравнивает сортировку для разных целевых символов.
    
    Args:
        strings (list): Список строк
    """
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ ДЛЯ РАЗНЫХ ЦЕЛЕВЫХ СИМВОЛОВ")
    print("=" * 60)
    
    # Находим топ-5 самых частых символов
    top_chars = find_all_common_chars(strings)
    
    if not top_chars:
        print("❌ Нет данных для анализа")
        return
    
    print(f"\n📊 ТОП-5 САМЫХ ЧАСТЫХ СИМВОЛОВ В НАБОРЕ:")
    for i, (char, freq) in enumerate(top_chars, 1):
        print(f"   {i}. '{char}': {freq:.4f}")
    
    print("\n🔍 Выберите символ для анализа:")
    for i, (char, _) in enumerate(top_chars, 1):
        print(f"   {i} - '{char}'")
    print(f"   {len(top_chars) + 1} - Ввести свой символ")
    
    try:
        choice = int(input("Ваш выбор: ").strip())
        
        if 1 <= choice <= len(top_chars):
            target_char, target_freq = top_chars[choice - 1]
        elif choice == len(top_chars) + 1:
            target_char = input("Введите символ: ").strip().lower()
            if not target_char:
                print("❌ Символ не введен")
                return
            # Вычисляем частоту для этого символа
            all_text = ''.join(strings).lower()
            total_chars = len(all_text)
            count = all_text.count(target_char)
            target_freq = count / total_chars if total_chars > 0 else 0
            print(f"   Частота '{target_char}' в наборе: {target_freq:.4f}")
        else:
            print("❌ Неверный выбор")
            return
        
        # Сортируем для выбранного символа
        sorted_strings = sort_strings(strings, target_char, target_freq)
        
        print(f"\n📊 РЕЗУЛЬТАТЫ ДЛЯ СИМВОЛА '{target_char}':")
        display_strings_with_stats(sorted_strings, target_char, target_freq, "ОТСОРТИРОВАННЫЙ СПИСОК")
        
    except ValueError:
        print("❌ Ошибка: введите число")

def demonstrate_with_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ НА ПРИМЕРАХ")
    print("=" * 60)
    
    examples = [
        "aaaaa bbbbb ccccc",  # Много 'a'
        "abcde fghij klmno",   # Равномерное распределение
        "aaa bbb ccc ddd eee", # Немного 'a'
        "Hello World!",         # Английский текст
        "Python Programming",   # Много 'p'
        "ааааа ббббб ввввв",    # Много 'а'
        "Привет мир"            # Русский текст
    ]
    
    print("\n📋 Исходные строки:")
    for i, s in enumerate(examples, 1):
        print(f"{i:2}. '{s}'")
    
    # Находим самый частый символ в наборе
    target_char, target_freq = find_most_common_char_in_set(examples)
    
    print(f"\n🎯 Самый частый символ в наборе: '{target_char}' (частота {target_freq:.4f})")
    
    print(f"\n📊 Статистика для символа '{target_char}':")
    for s in examples:
        freq = char_frequency_in_string(s, target_char)
        deviation = (freq - target_freq) ** 2
        print(f"   '{s[:20]}' - частота {freq:.4f}, отклонение {deviation:.6f}")
    
    sorted_examples = sort_strings(examples, target_char, target_freq)
    
    print(f"\n📊 Отсортировано по отклонению (возрастание):")
    for i, s in enumerate(sorted_examples, 1):
        deviation = calculate_quadratic_deviation(s, target_char, target_freq)
        freq = char_frequency_in_string(s, target_char)
        print(f"{i:2}. (откл. {deviation:.6f}) '{s}' - частота {freq:.4f}")

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
    
    # Находим самый частый символ в наборе
    target_char, target_freq = find_most_common_char_in_set(strings)
    
    if not target_char:
        print("❌ Не удалось определить целевой символ")
        return
    
    print(f"\n🎯 Автоматически выбран целевой символ: '{target_char}'")
    print(f"   Частота в наборе: {target_freq:.4f}")
    
    while True:
        print("\n" + "-" * 40)
        print("ВЫБЕРИТЕ ДЕЙСТВИЕ:")
        print("1 - Показать исходный список со статистикой")
        print("2 - Сортировать по отклонению")
        print("3 - Показать отсортированный список")
        print("4 - Анализ списка")
        print("5 - Сравнить с другим целевым символом")
        print("6 - Показать топ символов в наборе")
        print("7 - Сравнить исходный и отсортированный")
        print("8 - Добавить новую строку")
        print("9 - Пересчитать целевой символ")
        print("10 - Вернуться в главное меню")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            display_strings_with_stats(strings, target_char, target_freq, "ИСХОДНЫЙ СПИСОК")
        
        elif choice == "2":
            sorted_strings = sort_strings(strings, target_char, target_freq)
            print("✅ Строки отсортированы")
        
        elif choice == "3":
            sorted_strings = sort_strings(strings, target_char, target_freq)
            display_strings_with_stats(sorted_strings, target_char, target_freq, "ОТСОРТИРОВАННЫЙ СПИСОК")
        
        elif choice == "4":
            analyze_strings(strings, target_char, target_freq)
        
        elif choice == "5":
            compare_multiple_targets(strings)
        
        elif choice == "6":
            top_chars = find_all_common_chars(strings)
            print("\n📊 ТОП СИМВОЛОВ В НАБОРЕ:")
            for i, (char, freq) in enumerate(top_chars, 1):
                bar = '█' * int(freq * 50)
                print(f"   {i:2}. '{char}': {freq:.4f} {bar}")
        
        elif choice == "7":
            sorted_strings = sort_strings(strings, target_char, target_freq)
            
            print("\n📊 СРАВНЕНИЕ:")
            print("-" * 80)
            print("Исходный порядок -> Отсортированный порядок")
            print("-" * 80)
            
            for i, (orig, sorted_s) in enumerate(zip(strings, sorted_strings), 1):
                orig_dev = calculate_quadratic_deviation(orig, target_char, target_freq)
                sorted_dev = calculate_quadratic_deviation(sorted_s, target_char, target_freq)
                print(f"{i:2}. '{orig[:20]}' ({orig_dev:.6f})")
                print(f"    -> '{sorted_s[:20]}' ({sorted_dev:.6f})")
                print()
        
        elif choice == "8":
            new_string = input("Введите новую строку: ")
            if new_string:
                strings.append(new_string)
                # Пересчитываем целевой символ
                target_char, target_freq = find_most_common_char_in_set(strings)
                print(f"✅ Строка добавлена. Новый целевой символ: '{target_char}'")
        
        elif choice == "9":
            target_char, target_freq = find_most_common_char_in_set(strings)
            print(f"✅ Целевой символ пересчитан: '{target_char}' (частота {target_freq:.4f})")
        
        elif choice == "10":
            break
        
        else:
            print("❌ Неверный выбор")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ЗАДАНИЯ 11-14, ЗАДАЧА 12: Сортировка по отклонению от частоты в наборе")
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
                
                # Находим самый частый символ в наборе
                target_char, target_freq = find_most_common_char_in_set(strings)
                
                if target_char:
                    print(f"\n🎯 Самый частый символ в наборе: '{target_char}' (частота {target_freq:.4f})")
                    
                    display_strings_with_stats(strings, target_char, target_freq, "ИСХОДНЫЙ СПИСОК")
                    
                    sorted_strings = sort_strings(strings, target_char, target_freq)
                    display_strings_with_stats(sorted_strings, target_char, target_freq, "ОТСОРТИРОВАННЫЙ СПИСОК")
                    
                    analyze_strings(strings, target_char, target_freq)
                else:
                    print("❌ Не удалось определить целевой символ")
        
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