# -*- coding: utf-8 -*-
"""
Задания 2-4, Задача 8: Подсчет количества слов с четным количеством символов
Вариант 3
"""

import re

def count_even_length_words():
    """
    Подсчитывает количество слов с четным количеством символов в строке.
    
    Returns:
        int: Количество слов с четной длиной или None в случае ошибки
    """
    print("=" * 60)
    print("ЗАДАНИЕ 2-4, ЗАДАЧА 8: Подсчет слов с четным количеством символов")
    print("=" * 60)
    
    try:
        # Ввод строки от пользователя
        text = input("Введите строку из слов, разделенных пробелами: ")
        
        # Проверка на пустую строку
        if not text or not text.strip():
            print("Ошибка: строка не может быть пустой")
            return 0
        
        # Разбиваем строку на слова
        words = text.split()
        print(f"\nВсего слов в строке: {len(words)}")
        print(f"Слова: {words}")
        
        # Подсчет слов с четной длиной
        even_length_words = []
        odd_length_words = []
        
        for word in words:
            # Очищаем слово от знаков препинания для точного подсчета
            clean_word = re.sub(r'[^\w\s]', '', word)
            length = len(clean_word)
            
            if length % 2 == 0:
                even_length_words.append(f"'{word}' (длина {length})")
            else:
                odd_length_words.append(f"'{word}' (длина {length})")
        
        count = len(even_length_words)
        
        # Вывод результатов
        print(f"\nСлова с четной длиной ({len(even_length_words)} шт.):")
        if even_length_words:
            for word_info in even_length_words:
                print(f"  • {word_info}")
        else:
            print("  Нет слов с четной длиной")
        
        print(f"\nСлова с нечетной длиной ({len(odd_length_words)} шт.):")
        if odd_length_words:
            for word_info in odd_length_words[:5]:  # Показываем только первые 5
                print(f"  • {word_info}")
            if len(odd_length_words) > 5:
                print(f"  ... и еще {len(odd_length_words) - 5} слов")
        
        print(f"\n✅ Количество слов с четным количеством символов: {count}")
        
        # Дополнительная статистика
        if count > 0:
            percentage = (count / len(words)) * 100
            print(f"📊 Процент от всех слов: {percentage:.1f}%")
        
        return count
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def count_with_punctuation_handling():
    """
    Версия с обработкой знаков препинания.
    """
    print("\n" + "=" * 60)
    print("РАСШИРЕННАЯ ВЕРСИЯ: С обработкой знаков препинания")
    print("=" * 60)
    
    try:
        text = input("Введите строку (можно со знаками препинания): ")
        
        if not text or not text.strip():
            print("Ошибка: строка не может быть пустой")
            return 0
        
        print(f"\nИсходная строка: '{text}'")
        
        # Вариант 1: считаем символы без знаков препинания
        words_clean = []
        words_punctuation = []
        
        # Разбиваем на слова с учетом знаков препинания
        raw_words = text.split()
        
        for word in raw_words:
            # Удаляем знаки препинания в конце и начале слова
            clean_word = re.sub(r'^[^\w]+|[^\w]+$', '', word)
            words_clean.append(clean_word)
            
            # Сохраняем слово как есть для сравнения
            words_punctuation.append(word)
        
        print(f"\nСлова без знаков препинания: {words_clean}")
        
        # Подсчет для чистых слов
        even_clean = [w for w in words_clean if len(w) % 2 == 0]
        
        print(f"\n📊 Результаты:")
        print(f"  Слова с четной длиной (без учета знаков): {len(even_clean)}")
        print(f"  Чистые слова: {even_clean}")
        
        return len(even_clean)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def analyze_text_statistics():
    """
    Проводит подробный анализ текста.
    """
    print("\n" + "=" * 60)
    print("ПОДРОБНЫЙ АНАЛИЗ ТЕКСТА")
    print("=" * 60)
    
    try:
        text = input("Введите текст для анализа: ")
        
        if not text or not text.strip():
            print("Ошибка: текст не может быть пустым")
            return
        
        words = text.split()
        
        print(f"\n📊 СТАТИСТИКА:")
        print(f"  Всего слов: {len(words)}")
        print(f"  Общая длина текста: {len(text)} символов")
        
        # Анализ по длине слов
        length_stats = {}
        even_count = 0
        odd_count = 0
        
        for word in words:
            length = len(word)
            length_stats[length] = length_stats.get(length, 0) + 1
            
            if length % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        print(f"\n📈 Распределение по длине слов:")
        for length in sorted(length_stats.keys()):
            count = length_stats[length]
            bar = '█' * count
            print(f"  Длина {length:2d}: {count:2d} слов {bar}")
        
        print(f"\n  ✅ Четные: {even_count}")
        print(f"  ❌ Нечетные: {odd_count}")
        print(f"  ➗ Соотношение: {even_count/odd_count:.2f}" if odd_count > 0 else "  ➗ Все слова четные")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def demonstrate_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ НА ПРИМЕРАХ")
    print("=" * 60)
    
    test_strings = [
        "яблоко груша банан апельсин",
        "кот собака мышь слон",
        "hello world python programming code",
        "one two three four five six seven",
        "а роза упала на лапу азора"
    ]
    
    for i, test_str in enumerate(test_strings, 1):
        print(f"\n--- Пример {i} ---")
        print(f"Строка: '{test_str}'")
        
        words = test_str.split()
        even_words = [w for w in words if len(w) % 2 == 0]
        
        print(f"Слова: {words}")
        print(f"Длины слов: {[len(w) for w in words]}")
        print(f"Слова с четной длиной: {even_words}")
        print(f"Количество: {len(even_words)}")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("=" * 60)
        print("1 - Подсчет слов с четной длиной (обычный)")
        print("2 - С обработкой знаков препинания")
        print("3 - Детальный анализ текста")
        print("4 - Демонстрация на примерах")
        print("5 - Выйти")
        
        choice = input("Ваш выбор (1-5): ").strip()
        
        if choice == "1":
            count_even_length_words()
        
        elif choice == "2":
            count_with_punctuation_handling()
        
        elif choice == "3":
            analyze_text_statistics()
        
        elif choice == "4":
            demonstrate_examples()
        
        elif choice == "5":
            print("Программа завершена. До свидания!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 5")

if __name__ == "__main__":
    main()