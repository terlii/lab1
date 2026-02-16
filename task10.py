# -*- coding: utf-8 -*-
"""
Задание 10: Дан список строк с клавиатуры. Упорядочить по количеству слов в строке.
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
    print("ЗАДАНИЕ 10: Ввод списка строк")
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

def count_words(text):
    """
    Подсчитывает количество слов в строке.
    
    Args:
        text (str): Исходная строка
        
    Returns:
        int: Количество слов
    """
    if not text or not text.strip():
        return 0
    
    # Разбиваем по пробелам и фильтруем пустые элементы
    words = text.split()
    return len(words)

def count_words_advanced(text):
    """
    Подсчитывает количество слов с учетом знаков препинания.
    
    Args:
        text (str): Исходная строка
        
    Returns:
        int: Количество слов
    """
    if not text or not text.strip():
        return 0
    
    # Удаляем знаки препинания и разбиваем по пробелам
    clean_text = re.sub(r'[^\w\s]', ' ', text)
    words = clean_text.split()
    return len(words)

def sort_by_word_count(strings, advanced=False):
    """
    Сортирует список строк по количеству слов.
    
    Args:
        strings (list): Исходный список строк
        advanced (bool): Использовать расширенный подсчет
        
    Returns:
        list: Отсортированный список строк
    """
    if not strings:
        return []
    
    if advanced:
        sorted_strings = sorted(strings, key=lambda s: count_words_advanced(s))
    else:
        sorted_strings = sorted(strings, key=lambda s: count_words(s))
    
    return sorted_strings

def sort_by_word_count_desc(strings, advanced=False):
    """
    Сортирует список строк по количеству слов в обратном порядке.
    
    Args:
        strings (list): Исходный список строк
        advanced (bool): Использовать расширенный подсчет
        
    Returns:
        list: Отсортированный список строк
    """
    if not strings:
        return []
    
    if advanced:
        sorted_strings = sorted(strings, key=lambda s: count_words_advanced(s), reverse=True)
    else:
        sorted_strings = sorted(strings, key=lambda s: count_words(s), reverse=True)
    
    return sorted_strings

def display_strings_with_word_count(strings, title="СПИСОК СТРОК", advanced=False):
    """
    Отображает список строк с количеством слов в каждой.
    
    Args:
        strings (list): Список строк для отображения
        title (str): Заголовок
        advanced (bool): Использовать расширенный подсчет
    """
    if not strings:
        print("   Список пуст")
        return
    
    print(f"\n{title}:")
    print("-" * 70)
    
    # Находим максимальное количество слов для визуализации
    if advanced:
        word_counts = [count_words_advanced(s) for s in strings]
    else:
        word_counts = [count_words(s) for s in strings]
    
    max_count = max(word_counts) if word_counts else 0
    
    for i, s in enumerate(strings, 1):
        if advanced:
            word_count = count_words_advanced(s)
        else:
            word_count = count_words(s)
        
        # Визуализация количества слов
        bar_length = int(30 * word_count / max_count) if max_count > 0 else 0
        bar = '█' * bar_length
        
        print(f"{i:2}. '{s}'")
        print(f"     Слов: {word_count:2d} {bar}")
        if advanced and word_count != count_words(s):
            print(f"     (простой подсчет: {count_words(s)} слов)")
    
    print("-" * 70)

def analyze_strings(strings, advanced=False):
    """
    Проводит анализ списка строк по количеству слов.
    
    Args:
        strings (list): Список строк для анализа
        advanced (bool): Использовать расширенный подсчет
    """
    if not strings:
        return
    
    print("\n" + "=" * 60)
    print("АНАЛИЗ СПИСКА СТРОК")
    print("=" * 60)
    
    if advanced:
        word_counts = [count_words_advanced(s) for s in strings]
    else:
        word_counts = [count_words(s) for s in strings]
    
    print(f"\n📊 СТАТИСТИКА:")
    print(f"   Всего строк: {len(strings)}")
    print(f"   Всего слов: {sum(word_counts)}")
    print(f"   Минимальное количество слов: {min(word_counts)}")
    print(f"   Максимальное количество слов: {max(word_counts)}")
    print(f"   Среднее количество слов: {sum(word_counts) / len(word_counts):.2f}")
    print(f"   Медианное количество слов: {sorted(word_counts)[len(word_counts)//2]}")
    
    # Распределение по количеству слов
    print(f"\n📈 РАСПРЕДЕЛЕНИЕ ПО КОЛИЧЕСТВУ СЛОВ:")
    count_distribution = {}
    for count in word_counts:
        count_distribution[count] = count_distribution.get(count, 0) + 1
    
    for count in sorted(count_distribution.keys()):
        num_strings = count_distribution[count]
        bar = '█' * num_strings
        print(f"   {count:2} слов: {num_strings} стр. {bar}")
    
    # Строки с максимальным и минимальным количеством слов
    max_count = max(word_counts)
    min_count = min(word_counts)
    
    print(f"\n🏆 СТРОКИ С МАКСИМАЛЬНЫМ КОЛИЧЕСТВОМ СЛОВ ({max_count} слов):")
    for s in strings:
        if (advanced and count_words_advanced(s) == max_count) or (not advanced and count_words(s) == max_count):
            print(f"   • '{s}'")
    
    print(f"\n🥇 СТРОКИ С МИНИМАЛЬНЫМ КОЛИЧЕСТВОМ СЛОВ ({min_count} слов):")
    for s in strings:
        if (advanced and count_words_advanced(s) == min_count) or (not advanced and count_words(s) == min_count):
            print(f"   • '{s}'")

def filter_by_word_count(strings, min_words=None, max_words=None, advanced=False):
    """
    Фильтрует строки по количеству слов.
    
    Args:
        strings (list): Исходный список строк
        min_words (int, optional): Минимальное количество слов
        max_words (int, optional): Максимальное количество слов
        advanced (bool): Использовать расширенный подсчет
        
    Returns:
        list: Отфильтрованный список строк
    """
    if not strings:
        return []
    
    filtered = strings.copy()
    
    if min_words is not None:
        if advanced:
            filtered = [s for s in filtered if count_words_advanced(s) >= min_words]
        else:
            filtered = [s for s in filtered if count_words(s) >= min_words]
    
    if max_words is not None:
        if advanced:
            filtered = [s for s in filtered if count_words_advanced(s) <= max_words]
        else:
            filtered = [s for s in filtered if count_words(s) <= max_words]
    
    return filtered

def group_by_word_count(strings, advanced=False):
    """
    Группирует строки по количеству слов.
    
    Args:
        strings (list): Список строк
        advanced (bool): Использовать расширенный подсчет
        
    Returns:
        dict: Словарь {количество_слов: [строки]}
    """
    groups = {}
    for s in strings:
        if advanced:
            word_count = count_words_advanced(s)
        else:
            word_count = count_words(s)
        
        if word_count not in groups:
            groups[word_count] = []
        groups[word_count].append(s)
    
    return groups

def extract_vocabulary(strings):
    """
    Извлекает все уникальные слова из списка строк.
    
    Args:
        strings (list): Список строк
        
    Returns:
        set: Множество уникальных слов
    """
    vocabulary = set()
    
    for s in strings:
        # Очищаем от знаков препинания и разбиваем на слова
        words = re.findall(r'\b\w+\b', s.lower())
        vocabulary.update(words)
    
    return vocabulary

def demonstrate_with_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ НА ПРИМЕРАХ")
    print("=" * 60)
    
    examples = [
        "Привет мир",
        "Это строка с несколькими словами для примера",
        "Короткая строка",
        "Одно слово",
        "Строка с тремя словами",
        "А это очень длинная строка, которая содержит много-много различных слов для демонстрации работы программы"
    ]
    
    print("\n📋 Исходные строки:")
    for i, s in enumerate(examples, 1):
        word_count = count_words(s)
        print(f"{i:2}. '{s}'")
        print(f"     Слов: {word_count}")
    
    sorted_examples = sort_by_word_count(examples)
    
    print(f"\n📊 Отсортировано по количеству слов (возрастание):")
    for i, s in enumerate(sorted_examples, 1):
        word_count = count_words(s)
        print(f"{i:2}. ({word_count} слов) '{s}'")
    
    # Анализ
    print(f"\n📈 Анализ примеров:")
    word_counts = [count_words(s) for s in examples]
    print(f"   Всего слов в примерах: {sum(word_counts)}")
    print(f"   Уникальных слов: {len(extract_vocabulary(examples))}")

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
    
    use_advanced = False
    
    while True:
        print("\n" + "-" * 40)
        print(f"ТЕКУЩИЙ РЕЖИМ ПОДСЧЕТА: {'расширенный' if use_advanced else 'простой'}")
        print("ВЫБЕРИТЕ ДЕЙСТВИЕ:")
        print("1 - Показать исходный список")
        print("2 - Сортировка по возрастанию количества слов")
        print("3 - Сортировка по убыванию количества слов")
        print("4 - Анализ списка")
        print("5 - Фильтрация по количеству слов")
        print("6 - Группировка по количеству слов")
        print("7 - Переключить режим подсчета")
        print("8 - Показать словарь уникальных слов")
        print("9 - Добавить новую строку")
        print("10 - Удалить строку")
        print("11 - Вернуться в главное меню")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            display_strings_with_word_count(strings, "ИСХОДНЫЙ СПИСОК", use_advanced)
        
        elif choice == "2":
            sorted_strings = sort_by_word_count(strings, use_advanced)
            display_strings_with_word_count(sorted_strings, "СОРТИРОВКА ПО ВОЗРАСТАНИЮ КОЛИЧЕСТВА СЛОВ", use_advanced)
        
        elif choice == "3":
            sorted_strings = sort_by_word_count_desc(strings, use_advanced)
            display_strings_with_word_count(sorted_strings, "СОРТИРОВКА ПО УБЫВАНИЮ КОЛИЧЕСТВА СЛОВ", use_advanced)
        
        elif choice == "4":
            analyze_strings(strings, use_advanced)
        
        elif choice == "5":
            try:
                print("\nФильтрация строк по количеству слов")
                min_words = input("Минимальное количество слов (Enter - без ограничения): ").strip()
                max_words = input("Максимальное количество слов (Enter - без ограничения): ").strip()
                
                min_words = int(min_words) if min_words else None
                max_words = int(max_words) if max_words else None
                
                filtered = filter_by_word_count(strings, min_words, max_words, use_advanced)
                
                if filtered:
                    display_strings_with_word_count(filtered, f"СТРОКИ С {min_words or '?'} - {max_words or '?'} СЛОВАМИ", use_advanced)
                else:
                    print("❌ Нет строк, удовлетворяющих условиям")
                    
            except ValueError:
                print("❌ Ошибка: введите целое число")
        
        elif choice == "6":
            groups = group_by_word_count(strings, use_advanced)
            print("\n📊 ГРУППИРОВКА ПО КОЛИЧЕСТВУ СЛОВ:")
            for word_count in sorted(groups.keys()):
                print(f"\n{word_count} слов ({len(groups[word_count])} строк):")
                for s in groups[word_count][:3]:  # Показываем первые 3 строки
                    print(f"  • '{s}'")
                if len(groups[word_count]) > 3:
                    print(f"  ... и еще {len(groups[word_count]) - 3} строк")
        
        elif choice == "7":
            use_advanced = not use_advanced
            print(f"✅ Режим подсчета переключен на {'расширенный' if use_advanced else 'простой'}")
        
        elif choice == "8":
            vocabulary = extract_vocabulary(strings)
            print(f"\n📚 СЛОВАРЬ УНИКАЛЬНЫХ СЛОВ:")
            print(f"   Всего уникальных слов: {len(vocabulary)}")
            if vocabulary:
                sorted_vocab = sorted(vocabulary)
                print(f"   Слова: {', '.join(sorted_vocab[:20])}")
                if len(vocabulary) > 20:
                    print(f"   ... и еще {len(vocabulary) - 20} слов")
        
        elif choice == "9":
            new_string = input("Введите новую строку: ")
            if new_string:
                strings.append(new_string)
                print(f"✅ Строка добавлена. Всего строк: {len(strings)}")
        
        elif choice == "10":
            display_strings_with_word_count(strings, "ТЕКУЩИЙ СПИСОК", use_advanced)
            try:
                idx = int(input("Введите номер строки для удаления: ")) - 1
                if 0 <= idx < len(strings):
                    removed = strings.pop(idx)
                    print(f"✅ Удалена строка: '{removed}'")
                else:
                    print("❌ Неверный номер")
            except ValueError:
                print("❌ Ошибка: введите число")
        
        elif choice == "11":
            break
        
        else:
            print("❌ Неверный выбор")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ЗАДАНИЕ 10: Сортировка строк по количеству слов")
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
                
                display_strings_with_word_count(strings, "ИСХОДНЫЙ СПИСОК")
                
                sorted_strings = sort_by_word_count(strings)
                display_strings_with_word_count(sorted_strings, "ОТСОРТИРОВАННЫЙ ПО КОЛИЧЕСТВУ СЛОВ")
                
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