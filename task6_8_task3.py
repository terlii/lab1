# -*- coding: utf-8 -*-
"""
Задания 6-8, Задача 3: Найти общее количество русских символов в строке
Вариант 3
"""

import re

def count_russian_chars():
    """
    Подсчитывает количество русских символов в строке.
    
    Returns:
        int: Количество русских символов или None в случае ошибки
    """
    print("=" * 60)
    print("ЗАДАНИЯ 6-8, ЗАДАЧА 3: Подсчет русских символов в строке")
    print("=" * 60)
    
    try:
        # Ввод строки от пользователя
        text = input("Введите строку для анализа: ")
        
        # Проверка на пустую строку
        if not text:
            print("❌ Строка пуста")
            return 0
        
        print(f"\n📄 Анализируемая строка: '{text}'")
        print(f"   Длина строки: {len(text)} символов")
        
        # Подсчет русских символов
        count = 0
        russian_chars = []
        other_chars = []
        
        for char in text:
            # Проверка на русские буквы (включая ё)
            if ('а' <= char <= 'я') or ('А' <= char <= 'Я') or char in 'ёЁ':
                count += 1
                russian_chars.append(char)
            else:
                other_chars.append(char)
        
        # Вывод результатов
        if russian_chars:
            print(f"\n✅ Найденные русские символы ({len(russian_chars)} шт.):")
            
            # Группируем по регистру для наглядности
            lowercase = [c for c in russian_chars if 'а' <= c <= 'я' or c == 'ё']
            uppercase = [c for c in russian_chars if 'А' <= c <= 'Я' or c == 'Ё']
            
            if lowercase:
                print(f"   Строчные: {', '.join(lowercase)}")
            if uppercase:
                print(f"   Заглавные: {', '.join(uppercase)}")
            
            # Уникальные символы
            unique_chars = sorted(set(russian_chars))
            print(f"   Уникальные символы: {', '.join(unique_chars)}")
        else:
            print("❌ Русские символы не найдены")
        
        print(f"\n📊 Итог:")
        print(f"   Русских символов: {count}")
        print(f"   Других символов: {len(other_chars)}")
        
        if count > 0:
            percentage = (count / len(text)) * 100
            print(f"   Процент русских символов: {percentage:.1f}%")
        
        return count
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        return None

def count_russian_with_unicode():
    """
    Подсчет русских символов с использованием Unicode категорий.
    """
    print("\n" + "=" * 60)
    print("РАСШИРЕННАЯ ВЕРСИЯ: Подсчет с Unicode категориями")
    print("=" * 60)
    
    try:
        text = input("Введите строку для анализа: ")
        
        if not text:
            print("❌ Строка пуста")
            return 0
        
        # Диапазоны Unicode для русских букв
        # Кириллица: 0x0400-0x04FF
        russian_count = 0
        other_count = 0
        
        for char in text:
            code = ord(char)
            # Основной диапазон кириллицы
            if 0x0400 <= code <= 0x04FF:
                russian_count += 1
            else:
                other_count += 1
        
        print(f"\n📊 Результаты (по Unicode):")
        print(f"   Русских символов: {russian_count}")
        print(f"   Других символов: {other_count}")
        
        return russian_count
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return None

def analyze_russian_text():
    """
    Детальный анализ текста на русском языке.
    """
    print("\n" + "=" * 60)
    print("ДЕТАЛЬНЫЙ АНАЛИЗ РУССКОГО ТЕКСТА")
    print("=" * 60)
    
    try:
        text = input("Введите текст для анализа: ")
        
        if not text:
            print("❌ Текст пуст")
            return
        
        # Общая статистика
        total_chars = len(text)
        russian_chars = [c for c in text if ('а' <= c <= 'я') or ('А' <= c <= 'Я') or c in 'ёЁ']
        russian_count = len(russian_chars)
        
        print(f"\n📊 ОБЩАЯ СТАТИСТИКА:")
        print(f"   Всего символов: {total_chars}")
        print(f"   Русских символов: {russian_count}")
        print(f"   Доля русских: {russian_count/total_chars*100:.1f}%")
        
        # Статистика по буквам
        print(f"\n📈 ЧАСТОТА БУКВ:")
        letter_freq = {}
        for char in russian_chars:
            char_lower = char.lower()
            letter_freq[char_lower] = letter_freq.get(char_lower, 0) + 1
        
        # Сортируем по частоте
        sorted_letters = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
        
        for letter, freq in sorted_letters[:10]:  # Топ-10 букв
            percentage = (freq / russian_count) * 100
            bar = '█' * int(percentage)
            print(f"   '{letter}': {freq:3d} раз ({percentage:4.1f}%) {bar}")
        
        # Соотношение регистров
        lowercase = [c for c in russian_chars if 'а' <= c <= 'я' or c == 'ё']
        uppercase = [c for c in russian_chars if 'А' <= c <= 'Я' or c == 'Ё']
        
        print(f"\n🔤 РЕГИСТРЫ:")
        print(f"   Строчные буквы: {len(lowercase)} ({len(lowercase)/russian_count*100:.1f}%)")
        print(f"   Заглавные буквы: {len(uppercase)} ({len(uppercase)/russian_count*100:.1f}%)")
        
        # Слова в тексте
        words = re.findall(r'[а-яА-ЯёЁ]+', text)
        if words:
            print(f"\n📝 СЛОВА:")
            print(f"   Количество слов: {len(words)}")
            print(f"   Средняя длина слова: {sum(len(w) for w in words)/len(words):.1f} букв")
            
            # Самое длинное слово
            longest_word = max(words, key=len)
            print(f"   Самое длинное слово: '{longest_word}' ({len(longest_word)} букв)")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def filter_russian_text():
    """
    Фильтрует текст, оставляя только русские символы.
    """
    print("\n" + "=" * 60)
    print("ФИЛЬТРАЦИЯ ТЕКСТА: только русские символы")
    print("=" * 60)
    
    try:
        text = input("Введите текст: ")
        
        if not text:
            print("❌ Текст пуст")
            return
        
        # Оставляем только русские символы
        russian_only = ''.join([c for c in text if ('а' <= c <= 'я') or ('А' <= c <= 'Я') or c in 'ёЁ'])
        
        # Оставляем только русские буквы и пробелы
        russian_with_spaces = ''.join([c if ('а' <= c <= 'я') or ('А' <= c <= 'Я') or c in 'ёЁ' or c.isspace() else ' ' for c in text])
        # Убираем лишние пробелы
        russian_with_spaces = ' '.join(russian_with_spaces.split())
        
        print(f"\n📥 Исходный текст: '{text}'")
        print(f"📤 Только русские буквы: '{russian_only}'")
        print(f"📤 Русские буквы с пробелами: '{russian_with_spaces}'")
        
        print(f"\n📊 Статистика фильтрации:")
        print(f"   Исходная длина: {len(text)}")
        print(f"   Длина после фильтрации: {len(russian_only)}")
        print(f"   Удалено символов: {len(text) - len(russian_only)}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def compare_languages():
    """
    Сравнивает количество русских и других символов.
    """
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ РУССКИХ И ДРУГИХ СИМВОЛОВ")
    print("=" * 60)
    
    try:
        text = input("Введите текст: ")
        
        if not text:
            print("❌ Текст пуст")
            return
        
        # Категории символов
        russian = 0
        latin = 0
        digits = 0
        punctuation = 0
        spaces = 0
        other = 0
        
        for char in text:
            if ('а' <= char <= 'я') or ('А' <= char <= 'Я') or char in 'ёЁ':
                russian += 1
            elif ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
                latin += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1
            elif char in '.,!?;:-()[]{}"\'»«':
                punctuation += 1
            else:
                other += 1
        
        # Визуализация
        total = len(text)
        categories = [
            ("Русские", russian),
            ("Латиница", latin),
            ("Цифры", digits),
            ("Знаки", punctuation),
            ("Пробелы", spaces),
            ("Другое", other)
        ]
        
        print(f"\n📊 РАСПРЕДЕЛЕНИЕ СИМВОЛОВ:")
        print(f"   Всего символов: {total}")
        print()
        
        for name, count in categories:
            if count > 0:
                percentage = (count / total) * 100
                bar_length = int(percentage / 2)  # Масштабируем для наглядности
                bar = '█' * bar_length
                print(f"   {name:10}: {count:4d} ({percentage:5.1f}%) {bar}")
        
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
        "Привет, мир! Hello, world!",
        "Русский текст с цифрами 123 и символами !@#",
        "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
        "Смешанный текст Mix text 123!",
        "Только русский текст без латиницы",
        "1234567890 !@#$%^&*()"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n--- Пример {i} ---")
        print(f"Текст: '{example}'")
        
        count = 0
        russian_chars = []
        
        for char in example:
            if ('а' <= char <= 'я') or ('А' <= char <= 'Я') or char in 'ёЁ':
                count += 1
                russian_chars.append(char)
        
        print(f"Русских символов: {count}")
        if russian_chars:
            print(f"Найденные русские символы: {', '.join(russian_chars)}")
        else:
            print("Русских символов нет")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("=" * 60)
        print("1 - Подсчет русских символов (основной)")
        print("2 - Подсчет с Unicode категориями")
        print("3 - Детальный анализ текста")
        print("4 - Фильтрация русского текста")
        print("5 - Сравнение языков")
        print("6 - Демонстрация на примерах")
        print("7 - Выйти")
        
        choice = input("Ваш выбор (1-7): ").strip()
        
        if choice == "1":
            count_russian_chars()
        
        elif choice == "2":
            count_russian_with_unicode()
        
        elif choice == "3":
            analyze_russian_text()
        
        elif choice == "4":
            filter_russian_text()
        
        elif choice == "5":
            compare_languages()
        
        elif choice == "6":
            demonstrate_examples()
        
        elif choice == "7":
            print("Программа завершена. До свидания!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 7")

if __name__ == "__main__":
    main()