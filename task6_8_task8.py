# -*- coding: utf-8 -*-
"""
Задания 6-8, Задача 8: Найти все используемые строчные символы латиницы
Вариант 3
"""

import re
from collections import Counter

def find_lowercase_latin():
    """
    Находит все строчные латинские символы в строке.
    
    Returns:
        set: Множество найденных строчных латинских символов
    """
    print("=" * 60)
    print("ЗАДАНИЯ 6-8, ЗАДАЧА 8: Поиск строчных латинских символов")
    print("=" * 60)
    
    try:
        # Ввод строки от пользователя
        text = input("Введите строку для анализа: ")
        
        # Проверка на пустую строку
        if not text:
            print("❌ Строка пуста")
            return set()
        
        print(f"\n📄 Анализируемая строка: '{text}'")
        print(f"   Длина строки: {len(text)} символов")
        
        # Поиск строчных латинских символов
        lowercase_latin = set()
        all_chars = []
        
        for char in text:
            if 'a' <= char <= 'z':
                lowercase_latin.add(char)
                all_chars.append(char)
        
        # Вывод результатов
        if lowercase_latin:
            sorted_chars = sorted(lowercase_latin)
            print(f"\n✅ Найденные строчные латинские символы:")
            print(f"   {', '.join(sorted_chars)}")
            print(f"   Всего уникальных: {len(lowercase_latin)}")
            
            # Статистика по частоте
            char_freq = Counter(all_chars)
            print(f"\n📊 Частота встречаемости:")
            for char in sorted_chars:
                freq = char_freq[char]
                bar = '█' * freq
                print(f"   '{char}': {freq:2d} раз {bar}")
        else:
            print("❌ Строчные латинские символы не найдены")
        
        return lowercase_latin
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        return set()

def analyze_case_distribution():
    """
    Анализирует распределение строчных и заглавных латинских букв.
    """
    print("\n" + "=" * 60)
    print("АНАЛИЗ РАСПРЕДЕЛЕНИЯ РЕГИСТРОВ")
    print("=" * 60)
    
    try:
        text = input("Введите строку для анализа: ")
        
        if not text:
            print("❌ Строка пуста")
            return
        
        lowercase = []
        uppercase = []
        
        for char in text:
            if 'a' <= char <= 'z':
                lowercase.append(char)
            elif 'A' <= char <= 'Z':
                uppercase.append(char)
        
        print(f"\n📊 РЕЗУЛЬТАТЫ:")
        print(f"   Строчных букв: {len(lowercase)}")
        print(f"   Заглавных букв: {len(uppercase)}")
        
        if lowercase or uppercase:
            total = len(lowercase) + len(uppercase)
            print(f"\n   Соотношение:")
            if lowercase:
                print(f"   Строчные: {len(lowercase)/total*100:.1f}%")
            if uppercase:
                print(f"   Заглавные: {len(uppercase)/total*100:.1f}%")
        
        # Уникальные символы
        unique_lower = set(lowercase)
        unique_upper = set(uppercase)
        
        print(f"\n   Уникальных строчных: {len(unique_lower)}")
        print(f"   Уникальных заглавных: {len(unique_upper)}")
        
        # Буквы, которые есть в обоих регистрах
        both_cases = unique_lower & {c.lower() for c in unique_upper}
        if both_cases:
            print(f"\n   Буквы в обоих регистрах: {', '.join(sorted(both_cases))}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def find_missing_latin():
    """
    Находит строчные латинские буквы, отсутствующие в строке.
    """
    print("\n" + "=" * 60)
    print("ПОИСК ОТСУТСТВУЮЩИХ ЛАТИНСКИХ БУКВ")
    print("=" * 60)
    
    try:
        text = input("Введите строку для анализа: ")
        
        if not text:
            print("❌ Строка пуста")
            return
        
        # Все строчные латинские буквы
        all_lowercase = set('abcdefghijklmnopqrstuvwxyz')
        
        # Найденные буквы
        found = set()
        for char in text:
            if 'a' <= char <= 'z':
                found.add(char)
        
        # Отсутствующие буквы
        missing = all_lowercase - found
        
        print(f"\n📊 РЕЗУЛЬТАТЫ:")
        print(f"   Найдено букв: {len(found)} из 26")
        print(f"   Отсутствует: {len(missing)} букв")
        
        if found:
            print(f"\n✅ Присутствуют: {', '.join(sorted(found))}")
        
        if missing:
            print(f"\n❌ Отсутствуют: {', '.join(sorted(missing))}")
            
            # Визуализация алфавита
            print(f"\n📋 Алфавит:")
            alphabet_line = []
            for letter in all_lowercase:
                if letter in found:
                    alphabet_line.append(f"[{letter}]")
                else:
                    alphabet_line.append(f" {letter} ")
            print(''.join(alphabet_line))
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def extract_latin_words():
    """
    Извлекает слова, состоящие из латинских букв.
    """
    print("\n" + "=" * 60)
    print("ИЗВЛЕЧЕНИЕ ЛАТИНСКИХ СЛОВ")
    print("=" * 60)
    
    try:
        text = input("Введите текст: ")
        
        if not text:
            print("❌ Текст пуст")
            return
        
        # Находим слова из латинских букв
        latin_words = re.findall(r'\b[a-zA-Z]+\b', text)
        
        if not latin_words:
            print("❌ Латинские слова не найдены")
            return
        
        print(f"\n📊 Найдено слов: {len(latin_words)}")
        
        # Группируем по регистру
        lowercase_words = [w for w in latin_words if w.islower()]
        uppercase_words = [w for w in latin_words if w.isupper()]
        title_words = [w for w in latin_words if w.istitle()]
        mixed_words = [w for w in latin_words if not (w.islower() or w.isupper() or w.istitle())]
        
        if lowercase_words:
            print(f"\n✅ Слова в нижнем регистре ({len(lowercase_words)}):")
            print(f"   {', '.join(lowercase_words[:10])}")
            if len(lowercase_words) > 10:
                print(f"   ... и еще {len(lowercase_words) - 10}")
        
        if uppercase_words:
            print(f"\n✅ Слова в верхнем регистре ({len(uppercase_words)}):")
            print(f"   {', '.join(uppercase_words[:10])}")
        
        if title_words:
            print(f"\n✅ Слова с заглавной буквы ({len(title_words)}):")
            print(f"   {', '.join(title_words[:10])}")
        
        # Статистика по длине слов
        word_lengths = [len(w) for w in latin_words]
        print(f"\n📏 Статистика длины слов:")
        print(f"   Минимальная: {min(word_lengths)}")
        print(f"   Максимальная: {max(word_lengths)}")
        print(f"   Средняя: {sum(word_lengths)/len(word_lengths):.1f}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def latin_alphabet_coverage():
    """
    Показывает покрытие латинского алфавита в тексте.
    """
    print("\n" + "=" * 60)
    print("ПОКРЫТИЕ ЛАТИНСКОГО АЛФАВИТА")
    print("=" * 60)
    
    try:
        text = input("Введите текст: ")
        
        if not text:
            print("❌ Текст пуст")
            return
        
        # Статистика по буквам
        letter_stats = Counter()
        for char in text.lower():
            if 'a' <= char <= 'z':
                letter_stats[char] += 1
        
        if not letter_stats:
            print("❌ Латинские буквы не найдены")
            return
        
        print(f"\n📊 ПОКРЫТИЕ АЛФАВИТА:")
        print(f"   Всего букв: {sum(letter_stats.values())}")
        print(f"   Уникальных букв: {len(letter_stats)} из 26 ({len(letter_stats)/26*100:.1f}%)")
        
        # Таблица алфавита
        print(f"\n📋 ТАБЛИЦА ЧАСТОТНОСТИ:")
        print("   " + "-" * 40)
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            freq = letter_stats.get(letter, 0)
            if freq > 0:
                bar = '█' * min(freq, 20)
                print(f"   | {letter} | {freq:3d} | {bar}")
            else:
                print(f"   | {letter} |   0 |")
        print("   " + "-" * 40)
        
        # Топ-5 самых частых букв
        print(f"\n🏆 ТОП-5 САМЫХ ЧАСТЫХ БУКВ:")
        for letter, freq in letter_stats.most_common(5):
            percentage = (freq / sum(letter_stats.values())) * 100
            print(f"   {letter}: {freq} раз ({percentage:.1f}%)")
        
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
        "Hello World! Python is great.",
        "ABC abc XYZ xyz TEST test",
        "Only lowercase letters here",
        "MIXED case TEXT with Upper and Lower",
        "12345 !@#$% no letters",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n--- Пример {i} ---")
        print(f"Текст: '{example}'")
        
        lowercase = set()
        for char in example:
            if 'a' <= char <= 'z':
                lowercase.add(char)
        
        if lowercase:
            print(f"Строчные латинские буквы: {', '.join(sorted(lowercase))}")
            print(f"Количество: {len(lowercase)}")
        else:
            print("Строчные латинские буквы не найдены")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("=" * 60)
        print("1 - Поиск строчных латинских символов (основной)")
        print("2 - Анализ распределения регистров")
        print("3 - Поиск отсутствующих букв")
        print("4 - Извлечение латинских слов")
        print("5 - Покрытие латинского алфавита")
        print("6 - Демонстрация на примерах")
        print("7 - Выйти")
        
        choice = input("Ваш выбор (1-7): ").strip()
        
        if choice == "1":
            find_lowercase_latin()
        
        elif choice == "2":
            analyze_case_distribution()
        
        elif choice == "3":
            find_missing_latin()
        
        elif choice == "4":
            extract_latin_words()
        
        elif choice == "5":
            latin_alphabet_coverage()
        
        elif choice == "6":
            demonstrate_examples()
        
        elif choice == "7":
            print("Программа завершена. До свидания!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 7")

if __name__ == "__main__":
    main()