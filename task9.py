# -*- coding: utf-8 -*-
"""
Задание 9: Прочитать список строк с клавиатуры и упорядочить по длине строки
Вариант 3
"""

def read_strings():
    """
    Читает список строк с клавиатуры.
    
    Returns:
        list: Список введенных строк
    """
    print("=" * 60)
    print("ЗАДАНИЕ 9: Ввод списка строк")
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

def sort_by_length(strings):
    """
    Сортирует список строк по длине (от коротких к длинным).
    
    Args:
        strings (list): Исходный список строк
        
    Returns:
        list: Отсортированный список строк
    """
    if not strings:
        return []
    
    # Сортировка по длине строки
    sorted_strings = sorted(strings, key=len)
    
    return sorted_strings

def sort_by_length_desc(strings):
    """
    Сортирует список строк по длине в обратном порядке (от длинных к коротким).
    
    Args:
        strings (list): Исходный список строк
        
    Returns:
        list: Отсортированный список строк
    """
    if not strings:
        return []
    
    # Сортировка по длине строки (по убыванию)
    sorted_strings = sorted(strings, key=len, reverse=True)
    
    return sorted_strings

def display_strings(strings, title="СПИСОК СТРОК"):
    """
    Отображает список строк с их длинами.
    
    Args:
        strings (list): Список строк для отображения
        title (str): Заголовок
    """
    if not strings:
        print("   Список пуст")
        return
    
    print(f"\n{title}:")
    print("-" * 50)
    
    for i, s in enumerate(strings, 1):
        length = len(s)
        # Визуализация длины строки
        bar = '█' * min(length, 30)  # Ограничиваем длину полоски
        print(f"{i:2}. '{s}'")
        print(f"     Длина: {length} симв. {bar}")
    
    print("-" * 50)

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
    
    lengths = [len(s) for s in strings]
    
    print(f"\n📊 СТАТИСТИКА:")
    print(f"   Всего строк: {len(strings)}")
    print(f"   Минимальная длина: {min(lengths)} симв.")
    print(f"   Максимальная длина: {max(lengths)} симв.")
    print(f"   Средняя длина: {sum(lengths) / len(lengths):.2f} симв.")
    print(f"   Медианная длина: {sorted(lengths)[len(lengths)//2]}")
    
    # Распределение по длинам
    print(f"\n📈 РАСПРЕДЕЛЕНИЕ ПО ДЛИНАМ:")
    length_counts = {}
    for length in lengths:
        length_counts[length] = length_counts.get(length, 0) + 1
    
    for length in sorted(length_counts.keys()):
        count = length_counts[length]
        bar = '█' * count
        print(f"   Длина {length:2}: {count} стр. {bar}")
    
    # Самая длинная и короткая строки
    longest = max(strings, key=len)
    shortest = min(strings, key=len)
    
    print(f"\n🏆 САМАЯ ДЛИННАЯ СТРОКА:")
    print(f"   '{longest}'")
    print(f"   Длина: {len(longest)} симв.")
    
    print(f"\n🥇 САМАЯ КОРОТКАЯ СТРОКА:")
    print(f"   '{shortest}'")
    print(f"   Длина: {len(shortest)} симв.")

def filter_by_length(strings, min_length=None, max_length=None):
    """
    Фильтрует строки по длине.
    
    Args:
        strings (list): Исходный список строк
        min_length (int, optional): Минимальная длина
        max_length (int, optional): Максимальная длина
        
    Returns:
        list: Отфильтрованный список строк
    """
    if not strings:
        return []
    
    filtered = strings.copy()
    
    if min_length is not None:
        filtered = [s for s in filtered if len(s) >= min_length]
    
    if max_length is not None:
        filtered = [s for s in filtered if len(s) <= max_length]
    
    return filtered

def group_by_length(strings):
    """
    Группирует строки по длине.
    
    Args:
        strings (list): Список строк
        
    Returns:
        dict: Словарь {длина: [строки этой длины]}
    """
    groups = {}
    for s in strings:
        length = len(s)
        if length not in groups:
            groups[length] = []
        groups[length].append(s)
    
    return groups

def demonstrate_with_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ НА ПРИМЕРАХ")
    print("=" * 60)
    
    examples = [
        ["кот", "собака", "мышь", "слон", "тигр"],
        ["python", "java", "c++", "javascript", "php"],
        ["а", "аб", "абв", "абвг", "абвгд"],
        ["очень длинная строка с пробелами", "короткая", "средняя по длине строка"]
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n--- Пример {i} ---")
        print(f"Исходный список:")
        for j, s in enumerate(example, 1):
            print(f"  {j}. '{s}' (длина {len(s)})")
        
        sorted_example = sort_by_length(example)
        print(f"\nОтсортированный по длине (возрастание):")
        for j, s in enumerate(sorted_example, 1):
            print(f"  {j}. '{s}' (длина {len(s)})")

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
        print("1 - Показать исходный список")
        print("2 - Сортировка по возрастанию длины")
        print("3 - Сортировка по убыванию длины")
        print("4 - Анализ списка")
        print("5 - Фильтрация по длине")
        print("6 - Группировка по длине")
        print("7 - Добавить новую строку")
        print("8 - Удалить строку")
        print("9 - Вернуться в главное меню")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            display_strings(strings, "ИСХОДНЫЙ СПИСОК")
        
        elif choice == "2":
            sorted_strings = sort_by_length(strings)
            display_strings(sorted_strings, "СОРТИРОВКА ПО ВОЗРАСТАНИЮ ДЛИНЫ")
        
        elif choice == "3":
            sorted_strings = sort_by_length_desc(strings)
            display_strings(sorted_strings, "СОРТИРОВКА ПО УБЫВАНИЮ ДЛИНЫ")
        
        elif choice == "4":
            analyze_strings(strings)
        
        elif choice == "5":
            try:
                print("\nФильтрация строк по длине")
                min_len = input("Минимальная длина (Enter - без ограничения): ").strip()
                max_len = input("Максимальная длина (Enter - без ограничения): ").strip()
                
                min_len = int(min_len) if min_len else None
                max_len = int(max_len) if max_len else None
                
                filtered = filter_by_length(strings, min_len, max_len)
                
                if filtered:
                    display_strings(filtered, f"СТРОКИ ДЛИНОЙ {min_len or '?'} - {max_len or '?'}")
                else:
                    print("❌ Нет строк, удовлетворяющих условиям")
                    
            except ValueError:
                print("❌ Ошибка: введите целое число")
        
        elif choice == "6":
            groups = group_by_length(strings)
            print("\n📊 ГРУППИРОВКА ПО ДЛИНЕ:")
            for length in sorted(groups.keys()):
                print(f"\nДлина {length} ({len(groups[length])} строк):")
                for s in groups[length]:
                    print(f"  • '{s}'")
        
        elif choice == "7":
            new_string = input("Введите новую строку: ")
            if new_string:
                strings.append(new_string)
                print(f"✅ Строка добавлена. Всего строк: {len(strings)}")
        
        elif choice == "8":
            display_strings(strings, "ТЕКУЩИЙ СПИСОК")
            try:
                idx = int(input("Введите номер строки для удаления: ")) - 1
                if 0 <= idx < len(strings):
                    removed = strings.pop(idx)
                    print(f"✅ Удалена строка: '{removed}'")
                else:
                    print("❌ Неверный номер")
            except ValueError:
                print("❌ Ошибка: введите число")
        
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
        print("ЗАДАНИЕ 9: Сортировка строк по длине")
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
                
                display_strings(strings, "ИСХОДНЫЙ СПИСОК")
                
                sorted_strings = sort_by_length(strings)
                display_strings(sorted_strings, "ОТСОРТИРОВАННЫЙ ПО ДЛИНЕ")
                
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