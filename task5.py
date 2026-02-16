# -*- coding: utf-8 -*-
"""
Задание 5: Найти все даты, описанные в виде "31 февраля 2007"
Вариант 3
"""

import re
from datetime import datetime

def find_dates_in_text():
    """
    Находит в тексте даты формата "день месяц год" (например, "31 февраля 2007").
    
    Returns:
        list: Список найденных дат в виде кортежей (день, месяц, год)
    """
    print("=" * 60)
    print("ЗАДАНИЕ 5: Поиск дат в тексте")
    print("Формат: 'день месяц год' (например, '31 февраля 2007')")
    print("=" * 60)
    
    print("\nВведите текст для анализа (для завершения ввода введите пустую строку):")
    
    # Сбор многострочного текста
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    
    text = ' '.join(lines)
    
    if not text or not text.strip():
        print("❌ Текст не введен")
        return []
    
    print(f"\n📄 Анализируемый текст:")
    print(f"   {text[:100]}..." if len(text) > 100 else f"   {text}")
    print(f"   Длина текста: {len(text)} символов")
    
    # Регулярное выражение для поиска дат
    # День: 1-31, месяц: слово на русском, год: 4 цифры
    date_pattern = r'\b(3[01]|[12][0-9]|[1-9])\s+([а-яА-Я]+)\s+(\d{4})\b'
    
    matches = re.findall(date_pattern, text)
    
    if not matches:
        print("\n🔍 Даты в указанном формате не найдены")
        return []
    
    print(f"\n🔍 Найдено {len(matches)} дат:")
    
    # Словарь месяцев для проверки корректности
    months = {
        "января": 31, "февраля": 29, "марта": 31, "апреля": 30,
        "мая": 31, "июня": 30, "июля": 31, "августа": 31,
        "сентября": 30, "октября": 31, "ноября": 30, "декабря": 31,
        "январь": 31, "февраль": 29, "март": 31, "апрель": 30,
        "май": 31, "июнь": 30, "июль": 31, "август": 31,
        "сентябрь": 30, "октябрь": 31, "ноябрь": 30, "декабрь": 31
    }
    
    valid_dates = []
    invalid_dates = []
    
    for i, (day, month, year) in enumerate(matches, 1):
        day_int = int(day)
        month_lower = month.lower()
        year_int = int(year)
        
        # Проверка корректности даты
        is_valid = False
        error_reason = ""
        
        if month_lower in months:
            max_days = months[month_lower]
            
            # Особая проверка для февраля в високосные годы
            if month_lower in ["февраля", "февраль"]:
                if year_int % 400 == 0 or (year_int % 4 == 0 and year_int % 100 != 0):
                    max_days = 29  # Високосный год
                else:
                    max_days = 28  # Невисокосный год
            
            if day_int <= max_days:
                is_valid = True
            else:
                error_reason = f"в {month} максимум {max_days} дней"
        else:
            error_reason = f"неизвестный месяц '{month}'"
        
        # Форматированный вывод
        date_str = f"{day} {month} {year}"
        if is_valid:
            print(f"  {i}. ✓ {date_str} - корректная дата")
            valid_dates.append((day, month, year))
        else:
            print(f"  {i}. ✗ {date_str} - {error_reason}")
            invalid_dates.append((day, month, year, error_reason))
    
    # Статистика
    print(f"\n📊 Статистика:")
    print(f"  Всего найдено: {len(matches)}")
    print(f"  ✅ Корректных дат: {len(valid_dates)}")
    print(f"  ❌ Некорректных дат: {len(invalid_dates)}")
    
    return valid_dates

def find_dates_with_context():
    """
    Находит даты и показывает контекст вокруг них.
    """
    print("\n" + "=" * 60)
    print("ПОИСК ДАТ С КОНТЕКСТОМ")
    print("=" * 60)
    
    text = input("Введите текст: ")
    
    if not text or not text.strip():
        print("❌ Текст не введен")
        return
    
    # Поиск дат с контекстом (до и после)
    date_pattern = r'(.{0,30})(\b(3[01]|[12][0-9]|[1-9])\s+([а-яА-Я]+)\s+(\d{4})\b)(.{0,30})'
    
    matches = re.findall(date_pattern, text)
    
    if not matches:
        print("🔍 Даты не найдены")
        return
    
    print(f"\n🔍 Найдено {len(matches)} дат с контекстом:")
    
    for i, (before, day, month, year, after) in enumerate(matches, 1):
        print(f"\n--- Дата {i} ---")
        print(f"Контекст: ...{before}【{day} {month} {year}】{after}...")
        print(f"Дата: {day} {month} {year}")

def validate_date(day, month, year):
    """
    Проверяет корректность даты.
    
    Args:
        day (str): День
        month (str): Месяц
        year (str): Год
        
    Returns:
        tuple: (is_valid, error_message)
    """
    months = {
        "января": 31, "февраля": 29, "марта": 31, "апреля": 30,
        "мая": 31, "июня": 30, "июля": 31, "августа": 31,
        "сентября": 30, "октября": 31, "ноября": 30, "декабря": 31
    }
    
    try:
        day_int = int(day)
        year_int = int(year)
        month_lower = month.lower()
        
        if month_lower not in months:
            return False, f"Неизвестный месяц '{month}'"
        
        max_days = months[month_lower]
        
        # Проверка февраля в високосные годы
        if month_lower == "февраля":
            if year_int % 400 == 0 or (year_int % 4 == 0 and year_int % 100 != 0):
                max_days = 29
            else:
                max_days = 28
        
        if day_int < 1 or day_int > max_days:
            return False, f"День {day} не может быть в {month} (макс. {max_days})"
        
        return True, "Дата корректна"
        
    except ValueError:
        return False, "Ошибка преобразования числа"

def extract_all_dates(text):
    """
    Извлекает все возможные форматы дат из текста.
    
    Args:
        text (str): Исходный текст
        
    Returns:
        dict: Словарь с найденными датами в разных форматах
    """
    results = {}
    
    # Формат: ДД.ММ.ГГГГ
    dot_pattern = r'\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b'
    dot_dates = re.findall(dot_pattern, text)
    results['dot'] = [f"{d}.{m}.{y}" for d, m, y in dot_dates]
    
    # Формат: ДД/ММ/ГГГГ
    slash_pattern = r'\b(\d{1,2})/(\d{1,2})/(\d{4})\b'
    slash_dates = re.findall(slash_pattern, text)
    results['slash'] = [f"{d}/{m}/{y}" for d, m, y in slash_dates]
    
    # Формат: ДД месяц ГГГГ (как в задании)
    word_pattern = r'\b(3[01]|[12][0-9]|[1-9])\s+([а-яА-Я]+)\s+(\d{4})\b'
    word_dates = re.findall(word_pattern, text)
    results['word'] = [f"{d} {m} {y}" for d, m, y in word_dates]
    
    return results

def analyze_date_distribution(text):
    """
    Анализирует распределение дат по годам и месяцам.
    
    Args:
        text (str): Исходный текст
    """
    print("\n" + "=" * 60)
    print("АНАЛИЗ РАСПРЕДЕЛЕНИЯ ДАТ")
    print("=" * 60)
    
    date_pattern = r'\b(3[01]|[12][0-9]|[1-9])\s+([а-яА-Я]+)\s+(\d{4})\b'
    matches = re.findall(date_pattern, text)
    
    if not matches:
        print("Даты не найдены")
        return
    
    # Статистика по годам
    years = {}
    months_count = {}
    
    for day, month, year in matches:
        # По годам
        years[year] = years.get(year, 0) + 1
        
        # По месяцам
        month_lower = month.lower()
        months_count[month_lower] = months_count.get(month_lower, 0) + 1
    
    print(f"\n📅 Распределение по годам:")
    for year in sorted(years.keys()):
        count = years[year]
        bar = '█' * count
        print(f"  {year}: {count:2d} дат {bar}")
    
    print(f"\n📅 Распределение по месяцам:")
    month_order = ["января", "февраля", "марта", "апреля", "мая", "июня",
                   "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    
    for month in month_order:
        if month in months_count:
            count = months_count[month]
            bar = '█' * count
            print(f"  {month:10}: {count:2d} дат {bar}")

def demonstrate_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ НА ПРИМЕРАХ")
    print("=" * 60)
    
    examples = [
        "Встреча назначена на 31 февраля 2007 года, но это некорректная дата.",
        "Важные даты: 1 января 2020, 29 февраля 2024, 31 апреля 2023 и 15 мая 2025.",
        "События произошли 7 ноября 1917 и 9 мая 1945 года.",
        "Високосный год: 29 февраля 2000, 29 февраля 2020, 29 февраля 2021.",
        "Разные форматы: 31.12.2023, 01/01/2024 и 25 декабря 2025."
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n--- Пример {i} ---")
        print(f"Текст: {example}")
        
        dates = find_dates_in_text(example)
        
        if dates:
            print(f"Найденные даты: {len(dates)}")
        else:
            print("Даты не найдены")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("=" * 60)
        print("1 - Поиск дат в тексте (основной режим)")
        print("2 - Поиск дат с контекстом")
        print("3 - Анализ распределения дат")
        print("4 - Извлечение всех форматов дат")
        print("5 - Демонстрация на примерах")
        print("6 - Выйти")
        
        choice = input("Ваш выбор (1-6): ").strip()
        
        if choice == "1":
            find_dates_in_text()
        
        elif choice == "2":
            find_dates_with_context()
        
        elif choice == "3":
            text = input("Введите текст для анализа: ")
            if text:
                analyze_date_distribution(text)
        
        elif choice == "4":
            text = input("Введите текст: ")
            if text:
                results = extract_all_dates(text)
                print(f"\n📊 Найденные даты:")
                for format_name, dates in results.items():
                    if dates:
                        print(f"  {format_name}: {dates}")
                    else:
                        print(f"  {format_name}: не найдены")
        
        elif choice == "5":
            demonstrate_examples()
        
        elif choice == "6":
            print("Программа завершена. До свидания!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6")

if __name__ == "__main__":
    main()