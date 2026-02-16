# -*- coding: utf-8 -*-
"""
Задания 2-4, Задача 3: Перемешать все слова строки в случайном порядке
Вариант 3
"""

import random

def shuffle_words():
    """
    Функция перемешивает слова в строке в случайном порядке.
    
    Returns:
        str: Строка с перемешанными словами или None в случае ошибки
    """
    print("=" * 60)
    print("ЗАДАНИЕ 2-4, ЗАДАЧА 3: Перемешивание слов в строке")
    print("=" * 60)
    
    try:
        # Ввод строки от пользователя
        text = input("Введите строку из слов, разделенных пробелами: ")
        
        # Проверка на пустую строку
        if not text or not text.strip():
            print("Ошибка: строка не может быть пустой")
            return None
        
        # Разбиваем строку на слова
        words = text.split()
        print(f"\nИсходные слова ({len(words)} шт.): {words}")
        
        # Сохраняем исходный порядок для сравнения
        original_words = words.copy()
        
        # Перемешиваем слова
        random.shuffle(words)
        
        # Формируем результат
        result = ' '.join(words)
        
        # Выводим результаты
        print(f"Перемешанные слова: {words}")
        print(f"Результат: '{result}'")
        
        # Проверка, что слова действительно перемешались
        if original_words != words:
            print("\n✓ Слова успешно перемешаны")
        else:
            print("\n⚠ Внимание: порядок слов не изменился (возможно, мало слов)")
        
        return result
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def demonstrate_examples():
    """
    Демонстрирует работу функции на нескольких примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ НА ПРИМЕРАХ")
    print("=" * 60)
    
    test_strings = [
        "яблоко груша банан апельсин",
        "один два три четыре пять",
        "кот собака мышь слон тигр",
        "hello world python programming"
    ]
    
    for i, test_str in enumerate(test_strings, 1):
        print(f"\n--- Пример {i} ---")
        print(f"Исходная строка: '{test_str}'")
        
        words = test_str.split()
        print(f"Слова: {words}")
        
        random.shuffle(words)
        result = ' '.join(words)
        print(f"Результат: '{result}'")

def advanced_shuffle():
    """
    Расширенная версия с дополнительными возможностями.
    """
    print("\n" + "=" * 60)
    print("РАСШИРЕННАЯ ВЕРСИЯ: Перемешивание с настройками")
    print("=" * 60)
    
    try:
        text = input("Введите строку из слов, разделенных пробелами: ")
        
        if not text or not text.strip():
            print("Ошибка: строка не может быть пустой")
            return None
        
        words = text.split()
        print(f"\nИсходные слова: {words}")
        
        print("\nВыберите режим перемешивания:")
        print("1 - Полное случайное перемешивание")
        print("2 - Обратный порядок слов")
        print("3 - Переставить первое и последнее слово")
        print("4 - Случайная перестановка с сохранением первого слова")
        
        choice = input("Ваш выбор (1/2/3/4): ").strip()
        
        if choice == "1":
            random.shuffle(words)
            print("Режим: полное случайное перемешивание")
        
        elif choice == "2":
            words.reverse()
            print("Режим: обратный порядок слов")
        
        elif choice == "3":
            if len(words) >= 2:
                words[0], words[-1] = words[-1], words[0]
                print("Режим: перестановка первого и последнего слова")
            else:
                print("В строке太少 слов для этой операции")
        
        elif choice == "4":
            if len(words) >= 2:
                first_word = words[0]
                rest_words = words[1:]
                random.shuffle(rest_words)
                words = [first_word] + rest_words
                print("Режим: случайное перемешивание остальных слов")
            else:
                print("В строке太少 слов для этой операции")
        
        else:
            print("Неверный выбор, используется обычное перемешивание")
            random.shuffle(words)
        
        result = ' '.join(words)
        print(f"\nРезультат: '{result}'")
        return result
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def count_statistics(text):
    """
    Подсчитывает статистику по строке.
    
    Аргументы:
        text (str): Исходная строка
    """
    words = text.split()
    
    print("\n" + "=" * 60)
    print("СТАТИСТИКА СТРОКИ")
    print("=" * 60)
    
    print(f"Количество слов: {len(words)}")
    print(f"Общая длина строки: {len(text)} символов")
    print(f"Средняя длина слова: {sum(len(w) for w in words) / len(words):.2f} символов")
    
    # Находим самое длинное и короткое слово
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    
    print(f"Самое длинное слово: '{longest_word}' ({len(longest_word)} симв.)")
    print(f"Самое короткое слово: '{shortest_word}' ({len(shortest_word)} симв.)")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("=" * 60)
        print("1 - Перемешать слова (обычный режим)")
        print("2 - Расширенное перемешивание")
        print("3 - Посмотреть демонстрацию на примерах")
        print("4 - Показать статистику строки")
        print("5 - Выйти")
        
        choice = input("Ваш выбор (1-5): ").strip()
        
        if choice == "1":
            shuffle_words()
        
        elif choice == "2":
            advanced_shuffle()
        
        elif choice == "3":
            demonstrate_examples()
        
        elif choice == "4":
            text = input("Введите строку для анализа: ")
            if text and text.strip():
                count_statistics(text)
            else:
                print("Строка не может быть пустой")
        
        elif choice == "5":
            print("Программа завершена. До свидания!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 5")

if __name__ == "__main__":
    # Устанавливаем seed для воспроизводимости (можно убрать)
    random.seed()  # Использует системное время для генерации
    
    main()