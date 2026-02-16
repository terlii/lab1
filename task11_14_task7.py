# -*- coding: utf-8 -*-
"""
Задания 11-14, Задача 7: Сортировка в порядке увеличения разницы между 
количеством сочетаний «гласная-согласная» и «согласная-гласная» в строке
Вариант 3
"""

import re

def read_strings():
    """
    Читает список строк с клавиатуры.
    
    Returns:
        list: Список введенных строк
    """
    print("=" * 60)
    print("ЗАДАНИЯ 11-14, ЗАДАЧА 7: Ввод списка строк")
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

def is_vowel(char):
    """
    Проверяет, является ли символ гласной буквой.
    
    Args:
        char (str): Проверяемый символ
        
    Returns:
        bool: True если гласная, False если нет
    """
    if not char or not char.isalpha():
        return False
    
    char_lower = char.lower()
    
    # Гласные в русском и английском языках
    vowels = set('aeiouyаеёиоуыэюя')
    
    return char_lower in vowels

def is_consonant(char):
    """
    Проверяет, является ли символ согласной буквой.
    
    Args:
        char (str): Проверяемый символ
        
    Returns:
        bool: True если согласная, False если нет
    """
    if not char or not char.isalpha():
        return False
    
    return not is_vowel(char)

def calculate_vc_cv_diff(s):
    """
    Вычисляет разницу между количеством сочетаний "гласная-согласная" и "согласная-гласная".
    
    Args:
        s (str): Исходная строка
        
    Returns:
        int: Разница (VC - CV)
    """
    if len(s) < 2:
        return 0
    
    s_lower = s.lower()
    vc_count = 0  # гласная-согласная
    cv_count = 0  # согласная-гласная
    
    # Анализируем все пары соседних символов
    for i in range(len(s_lower) - 1):
        first, second = s_lower[i], s_lower[i+1]
        
        # Проверяем, что оба символа - буквы
        if first.isalpha() and second.isalpha():
            if is_vowel(first) and is_consonant(second):
                vc_count += 1
            elif is_consonant(first) and is_vowel(second):
                cv_count += 1
    
    return vc_count - cv_count

def calculate_vc_cv_diff_with_details(s):
    """
    Вычисляет разницу с детальной информацией.
    
    Args:
        s (str): Исходная строка
        
    Returns:
        tuple: (разница, vc_count, cv_count, список_сочетаний)
    """
    if len(s) < 2:
        return 0, 0, 0, []
    
    s_lower = s.lower()
    vc_count = 0
    cv_count = 0
    combinations = []
    
    for i in range(len(s_lower) - 1):
        first, second = s_lower[i], s_lower[i+1]
        
        if first.isalpha() and second.isalpha():
            if is_vowel(first) and is_consonant(second):
                vc_count += 1
                combinations.append(f"VC: {first}{second}")
            elif is_consonant(first) and is_vowel(second):
                cv_count += 1
                combinations.append(f"CV: {first}{second}")
    
    return vc_count - cv_count, vc_count, cv_count, combinations

def calculate_sort_key(s):
    """
    Вычисляет ключ сортировки для строки.
    
    Args:
        s (str): Исходная строка
        
    Returns:
        int: Разница VC - CV
    """
    return calculate_vc_cv_diff(s)

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
    print("=" * 90)
    
    for i, s in enumerate(strings, 1):
        diff, vc_count, cv_count, combinations = calculate_vc_cv_diff_with_details(s)
        
        print(f"{i:2}. '{s}'")
        print(f"     Длина строки: {len(s)} символов")
        print(f"     Сочетаний гласная-согласная (VC): {vc_count}")
        print(f"     Сочетаний согласная-гласная (CV): {cv_count}")
        print(f"     Разница (VC - CV): {diff}")
        
        if combinations:
            # Показываем первые 10 сочетаний
            print(f"     Найденные сочетания: {', '.join(combinations[:10])}")
            if len(combinations) > 10:
                print(f"     ... и еще {len(combinations) - 10} сочетаний")
        
        # Визуализация разницы
        if diff != 0:
            bar = '█' * min(abs(diff) * 2, 30)
            if diff > 0:
                print(f"     VC больше на {diff}: {bar}")
            else:
                print(f"     CV больше на {abs(diff)}: {bar}")
        else:
            print("     VC = CV")
        
        print()
    
    print("=" * 90)

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
    
    # Собираем статистику
    stats = []
    for s in strings:
        diff, vc, cv, _ = calculate_vc_cv_diff_with_details(s)
        stats.append({
            'string': s,
            'diff': diff,
            'vc': vc,
            'cv': cv,
            'total_pairs': vc + cv
        })
    
    print(f"\n📊 ОБЩАЯ СТАТИСТИКА:")
    print(f"   Всего строк: {len(strings)}")
    
    # Статистика по разницам
    diffs = [s['diff'] for s in stats]
    print(f"\n📈 РАСПРЕДЕЛЕНИЕ РАЗНИЦ:")
    print(f"   Минимальная разница: {min(diffs)}")
    print(f"   Максимальная разница: {max(diffs)}")
    print(f"   Средняя разница: {sum(diffs) / len(diffs):.2f}")
    
    # Гистограмма разниц
    print(f"\n📊 ГИСТОГРАММА РАЗНИЦ:")
    diff_ranges = [(-10, -5), (-5, -2), (-2, 0), (0, 2), (2, 5), (5, 10)]
    for low, high in diff_ranges:
        count = sum(1 for d in diffs if low <= d < high)
        if count > 0:
            bar = '█' * count
            print(f"   {low:2d}..{high:2d}: {count:2d} строк {bar}")
    
    # Строки с максимальной положительной и отрицательной разницей
    max_positive = max(diffs)
    max_negative = min(diffs)
    
    print(f"\n🏆 СТРОКИ С МАКСИМАЛЬНОЙ ПОЛОЖИТЕЛЬНОЙ РАЗНИЦЕЙ (VC > CV на {max_positive}):")
    for s in stats:
        if s['diff'] == max_positive:
            print(f"   • '{s['string']}' (VC={s['vc']}, CV={s['cv']})")
    
    print(f"\n🥇 СТРОКИ С МАКСИМАЛЬНОЙ ОТРИЦАТЕЛЬНОЙ РАЗНИЦЕЙ (CV > VC на {abs(max_negative)}):")
    for s in stats:
        if s['diff'] == max_negative:
            print(f"   • '{s['string']}' (VC={s['vc']}, CV={s['cv']})")
    
    # Строки с нулевой разницей
    zero_diff = [s for s in stats if s['diff'] == 0]
    if zero_diff:
        print(f"\n⚖ СТРОКИ С НУЛЕВОЙ РАЗНИЦЕЙ ({len(zero_diff)} шт.):")
        for s in zero_diff[:5]:
            print(f"   • '{s['string']}'")
        if len(zero_diff) > 5:
            print(f"   ... и еще {len(zero_diff) - 5} строк")

def extract_all_pairs(s):
    """
    Извлекает все пары символов из строки.
    
    Args:
        s (str): Исходная строка
        
    Returns:
        list: Список всех пар
    """
    pairs = []
    for i in range(len(s) - 1):
        pairs.append(s[i:i+2])
    return pairs

def analyze_by_language(strings):
    """
    Анализирует строки отдельно для русского и английского языков.
    
    Args:
        strings (list): Список строк
    """
    print("\n" + "=" * 60)
    print("АНАЛИЗ ПО ЯЗЫКАМ")
    print("=" * 60)
    
    russian_strings = []
    english_strings = []
    mixed_strings = []
    
    for s in strings:
        has_russian = any('а' <= c.lower() <= 'я' for c in s if c.isalpha())
        has_english = any('a' <= c.lower() <= 'z' for c in s if c.isalpha())
        
        if has_russian and not has_english:
            russian_strings.append(s)
        elif has_english and not has_russian:
            english_strings.append(s)
        else:
            mixed_strings.append(s)
    
    print(f"\n📊 РАСПРЕДЕЛЕНИЕ ПО ЯЗЫКАМ:")
    print(f"   Русские строки: {len(russian_strings)}")
    print(f"   Английские строки: {len(english_strings)}")
    print(f"   Смешанные строки: {len(mixed_strings)}")
    
    if russian_strings:
        print(f"\n🇷🇺 АНАЛИЗ РУССКИХ СТРОК:")
        russian_diffs = [calculate_vc_cv_diff(s) for s in russian_strings]
        print(f"   Средняя разница: {sum(russian_diffs) / len(russian_diffs):.2f}")
    
    if english_strings:
        print(f"\n🇬🇧 АНАЛИЗ АНГЛИЙСКИХ СТРОК:")
        english_diffs = [calculate_vc_cv_diff(s) for s in english_strings]
        print(f"   Средняя разница: {sum(english_diffs) / len(english_diffs):.2f}")

def demonstrate_with_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ НА ПРИМЕРАХ")
    print("=" * 60)
    
    examples = [
        "абра кадабра",           # Русский текст
        "Hello World",             # Английский текст
        "aaee iioo uu",            # Много гласных
        "bcdf ghjk lmnp",           # Много согласных
        "Python Programming",       # Смешанный текст
        "гласная согласная",        # Чередование
        "ае ёи оу ыэ юя"            # Только гласные
    ]
    
    print("\n📋 Исходные строки:")
    for i, s in enumerate(examples, 1):
        diff, vc, cv, _ = calculate_vc_cv_diff_with_details(s)
        print(f"{i:2}. '{s}'")
        print(f"     VC={vc}, CV={cv}, разница={diff}")
    
    sorted_examples = sort_strings(examples)
    
    print(f"\n📊 Отсортировано по разнице (возрастание):")
    for i, s in enumerate(sorted_examples, 1):
        diff = calculate_vc_cv_diff(s)
        print(f"{i:2}. (разница {diff:2d}) '{s}'")

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
        print("2 - Сортировать по разнице VC-CV")
        print("3 - Показать отсортированный список")
        print("4 - Анализ списка")
        print("5 - Анализ по языкам")
        print("6 - Сравнить исходный и отсортированный")
        print("7 - Показать все пары символов")
        print("8 - Добавить новую строку")
        print("9 - Вернуться в главное меню")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            display_strings_with_stats(strings, "ИСХОДНЫЙ СПИСОК")
        
        elif choice == "2":
            sorted_strings = sort_strings(strings)
            print("✅ Строки отсортированы")
        
        elif choice == "3":
            sorted_strings = sort_strings(strings)
            display_strings_with_stats(sorted_strings, "ОТСОРТИРОВАННЫЙ СПИСОК")
        
        elif choice == "4":
            analyze_strings(strings)
        
        elif choice == "5":
            analyze_by_language(strings)
        
        elif choice == "6":
            sorted_strings = sort_strings(strings)
            
            print("\n📊 СРАВНЕНИЕ:")
            print("-" * 70)
            print("Исходный порядок -> Отсортированный порядок")
            print("-" * 70)
            
            for i, (orig, sorted_s) in enumerate(zip(strings, sorted_strings), 1):
                orig_diff = calculate_vc_cv_diff(orig)
                sorted_diff = calculate_vc_cv_diff(sorted_s)
                print(f"{i:2}. '{orig[:20]}' ({orig_diff:2d})")
                print(f"    -> '{sorted_s[:20]}' ({sorted_diff:2d})")
                print()
        
        elif choice == "7":
            s = input("Введите строку для анализа: ")
            if s:
                pairs = extract_all_pairs(s)
                print(f"\n📋 Все пары символов ({len(pairs)} шт.):")
                for i, pair in enumerate(pairs, 1):
                    print(f"   {i:2}. '{pair}'")
        
        elif choice == "8":
            new_string = input("Введите новую строку: ")
            if new_string:
                strings.append(new_string)
                print(f"✅ Строка добавлена. Всего строк: {len(strings)}")
        
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
        print("ЗАДАНИЯ 11-14, ЗАДАЧА 7: Сортировка по разнице VC-CV")
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
                display_strings_with_stats(sorted_strings, "ОТСОРТИРОВАННЫЙ ПО РАЗНИЦЕ VC-CV")
                
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