# -*- coding: utf-8 -*-
"""
Задания с массивами, Задача 51: Для введенного списка построить два списка L1 и L2,
где элементы L1 - неповторяющиеся элементы исходного списка,
а элемент списка L2 с номером i показывает, сколько раз элемент списка L1
с таким номером повторяется в исходном.
Вариант 3
"""

from collections import Counter

def read_list():
    """
    Читает список элементов с клавиатуры.
    
    Returns:
        list: Список введенных элементов
    """
    print("=" * 60)
    print("ВВОД СПИСКА ЭЛЕМЕНТОВ")
    print("=" * 60)
    
    print("\nВведите элементы списка, разделенные пробелом:")
    print("Например: 5 3 2 5 3 5 1 2 3 5")
    
    while True:
        try:
            line = input("➡ ").strip()
            if not line:
                print("❌ Список не может быть пустым")
                continue
            
            # Разбиваем строку на элементы
            elements = line.split()
            
            # Пробуем преобразовать в числа, если возможно
            try:
                # Пытаемся преобразовать в int
                elements = [int(x) for x in elements]
                print("   (Интерпретируем как целые числа)")
            except ValueError:
                try:
                    # Пытаемся преобразовать в float
                    elements = [float(x) for x in elements]
                    print("   (Интерпретируем как числа с плавающей точкой)")
                except ValueError:
                    # Оставляем как строки
                    print("   (Интерпретируем как строки)")
            
            print(f"\n✅ Введен список из {len(elements)} элементов:")
            print(f"   {elements}")
            
            return elements
            
        except Exception as e:
            print(f"❌ Ошибка: {e}")

def build_frequency_lists(lst):
    """
    Строит списки L1 (уникальные элементы) и L2 (их частоты).
    
    Args:
        lst (list): Исходный список
        
    Returns:
        tuple: (L1, L2) - списки уникальных элементов и их частот
    """
    # Считаем частоту каждого элемента
    counter = Counter(lst)
    
    # L1 - уникальные элементы в порядке первого появления
    L1 = []
    seen = set()
    
    for item in lst:
        if item not in seen:
            L1.append(item)
            seen.add(item)
    
    # L2 - соответствующие частоты
    L2 = [counter[item] for item in L1]
    
    return L1, L2

def build_frequency_lists_sorted(lst):
    """
    Строит списки L1 и L2, отсортированные по убыванию частоты.
    
    Args:
        lst (list): Исходный список
        
    Returns:
        tuple: (L1, L2) - отсортированные списки
    """
    counter = Counter(lst)
    
    # Сортируем элементы по убыванию частоты
    sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    L1 = [item for item, _ in sorted_items]
    L2 = [count for _, count in sorted_items]
    
    return L1, L2

def display_frequency_lists(lst, title="РЕЗУЛЬТАТ"):
    """
    Отображает исходный список и построенные L1 и L2.
    
    Args:
        lst (list): Исходный список
        title (str): Заголовок
    """
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
    
    L1, L2 = build_frequency_lists(lst)
    
    print(f"\n📋 Исходный список:")
    print(f"   {lst}")
    print(f"   Длина: {len(lst)}")
    
    print(f"\n📊 Результат:")
    print(f"   L1 (уникальные элементы):")
    for i, item in enumerate(L1, 1):
        print(f"      {i}. {item}")
    
    print(f"\n   L2 (частоты):")
    for i, count in enumerate(L2, 1):
        bar = '█' * count
        print(f"      {i}. {count} {bar}")
    
    print(f"\n📈 Таблица соответствия:")
    print(f"   {'№':3} | {'Элемент':15} | {'Частота':8} | Визуализация")
    print(f"   {'-' * 45}")
    
    for i, (item, count) in enumerate(zip(L1, L2), 1):
        bar = '█' * count
        print(f"   {i:2} | {str(item):15} | {count:8} | {bar}")
    
    # Проверка
    total_elements = sum(L2)
    unique_elements = len(L1)
    
    print(f"\n✅ Проверка:")
    print(f"   Сумма частот: {total_elements} (должна равняться {len(lst)})")
    print(f"   Уникальных элементов: {unique_elements}")

def analyze_frequency_distribution(lst):
    """
    Анализирует распределение частот в списке.
    
    Args:
        lst (list): Исходный список
    """
    print("\n" + "=" * 60)
    print("АНАЛИЗ РАСПРЕДЕЛЕНИЯ ЧАСТОТ")
    print("=" * 60)
    
    L1, L2 = build_frequency_lists(lst)
    
    print(f"\n📊 СТАТИСТИКА:")
    print(f"   Всего элементов: {len(lst)}")
    print(f"   Уникальных элементов: {len(L1)}")
    
    if L2:
        print(f"   Минимальная частота: {min(L2)}")
        print(f"   Максимальная частота: {max(L2)}")
        print(f"   Средняя частота: {sum(L2) / len(L2):.2f}")
    
    # Распределение частот
    freq_of_freqs = Counter(L2)
    
    print(f"\n📈 РАСПРЕДЕЛЕНИЕ ЧАСТОТ:")
    for freq in sorted(freq_of_freqs.keys()):
        count = freq_of_freqs[freq]
        bar = '█' * count
        print(f"   Частота {freq}: {count} элемент(ов) {bar}")
    
    # Элементы с максимальной частотой
    max_freq = max(L2) if L2 else 0
    most_frequent = [(L1[i], L2[i]) for i in range(len(L1)) if L2[i] == max_freq]
    
    print(f"\n🏆 САМЫЕ ЧАСТЫЕ ЭЛЕМЕНТЫ (встречаются {max_freq} раз):")
    for item, freq in most_frequent:
        print(f"   • {item}")
    
    # Уникальные элементы (частота 1)
    unique_items = [(L1[i], L2[i]) for i in range(len(L1)) if L2[i] == 1]
    
    if unique_items:
        print(f"\n✨ УНИКАЛЬНЫЕ ЭЛЕМЕНТЫ (встречаются 1 раз):")
        for item, freq in unique_items[:10]:
            print(f"   • {item}")
        if len(unique_items) > 10:
            print(f"   ... и еще {len(unique_items) - 10}")

def find_duplicates(lst):
    """
    Находит все дублирующиеся элементы в списке.
    
    Args:
        lst (list): Исходный список
        
    Returns:
        dict: Словарь {элемент: количество_повторений} для элементов с частотой > 1
    """
    counter = Counter(lst)
    return {item: count for item, count in counter.items() if count > 1}

def find_unique_elements(lst):
    """
    Находит элементы, встречающиеся только один раз.
    
    Args:
        lst (list): Исходный список
        
    Returns:
        list: Элементы с частотой 1
    """
    counter = Counter(lst)
    return [item for item, count in counter.items() if count == 1]

def compare_with_sorted_version(lst):
    """
    Сравнивает обычную и отсортированную версии.
    
    Args:
        lst (list): Исходный список
    """
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ ВЕРСИЙ")
    print("=" * 60)
    
    L1_normal, L2_normal = build_frequency_lists(lst)
    L1_sorted, L2_sorted = build_frequency_lists_sorted(lst)
    
    print(f"\n📊 Обычная версия (порядок первого появления):")
    for i, (item, freq) in enumerate(zip(L1_normal, L2_normal), 1):
        print(f"   {i}. {item} -> {freq} раз")
    
    print(f"\n📊 Отсортированная версия (по убыванию частоты):")
    for i, (item, freq) in enumerate(zip(L1_sorted, L2_sorted), 1):
        print(f"   {i}. {item} -> {freq} раз")
    
    # Проверка эквивалентности
    if sorted(L1_normal) == sorted(L1_sorted):
        print(f"\n✅ Наборы уникальных элементов совпадают")
    else:
        print(f"\n❌ Наборы уникальных элементов различаются")

def demonstrate_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ НА ПРИМЕРАХ")
    print("=" * 60)
    
    examples = [
        [5, 3, 2, 5, 3, 5, 1, 2, 3, 5],
        ["яблоко", "груша", "яблоко", "банан", "груша", "яблоко"],
        [1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5],
        [2.5, 1.3, 2.5, 4.8, 1.3, 2.5]
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n--- Пример {i} ---")
        print(f"Исходный список: {example}")
        
        L1, L2 = build_frequency_lists(example)
        
        print(f"L1 (уникальные): {L1}")
        print(f"L2 (частоты):    {L2}")
        
        # Проверка
        reconstructed = []
        for item, count in zip(L1, L2):
            reconstructed.extend([item] * count)
        
        # Сортируем для сравнения
        if sorted(reconstructed) == sorted(example):
            print(f"✅ Проверка пройдена: список восстановлен")

def interactive_mode():
    """
    Интерактивный режим с дополнительными возможностями.
    """
    print("\n" + "=" * 60)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("=" * 60)
    
    lst = read_list()
    
    if not lst:
        return
    
    while True:
        print("\n" + "-" * 40)
        print("ВЫБЕРИТЕ ДЕЙСТВИЕ:")
        print("1 - Построить L1 и L2 (основное)")
        print("2 - Показать отсортированную версию")
        print("3 - Анализ распределения частот")
        print("4 - Найти дубликаты")
        print("5 - Найти уникальные элементы")
        print("6 - Сравнить версии")
        print("7 - Восстановить исходный список из L1 и L2")
        print("8 - Ввести новый список")
        print("9 - Вернуться в главное меню")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            display_frequency_lists(lst, "РЕЗУЛЬТАТ")
        
        elif choice == "2":
            L1_sorted, L2_sorted = build_frequency_lists_sorted(lst)
            print(f"\n📊 Отсортированная версия:")
            for i, (item, freq) in enumerate(zip(L1_sorted, L2_sorted), 1):
                bar = '█' * freq
                print(f"   {i}. {item} -> {freq} {bar}")
        
        elif choice == "3":
            analyze_frequency_distribution(lst)
        
        elif choice == "4":
            duplicates = find_duplicates(lst)
            if duplicates:
                print(f"\n🔍 Найденные дубликаты:")
                for item, count in duplicates.items():
                    print(f"   • {item} встречается {count} раз")
                print(f"   Всего дублирующихся элементов: {len(duplicates)}")
            else:
                print("❌ Дубликаты не найдены")
        
        elif choice == "5":
            unique = find_unique_elements(lst)
            if unique:
                print(f"\n✨ Уникальные элементы (встречаются 1 раз):")
                for item in unique:
                    print(f"   • {item}")
                print(f"   Всего: {len(unique)}")
            else:
                print("❌ Уникальные элементы не найдены")
        
        elif choice == "6":
            compare_with_sorted_version(lst)
        
        elif choice == "7":
            L1, L2 = build_frequency_lists(lst)
            reconstructed = []
            for item, count in zip(L1, L2):
                reconstructed.extend([item] * count)
            
            print(f"\n🔄 Восстановленный список:")
            print(f"   {reconstructed}")
            
            # Сортируем для сравнения
            if sorted(reconstructed) == sorted(lst):
                print(f"✅ Список успешно восстановлен")
            else:
                print(f"❌ Ошибка при восстановлении")
        
        elif choice == "8":
            lst = read_list()
            if not lst:
                return
        
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
        print("ЗАДАНИЯ С МАССИВАМИ, ЗАДАЧА 51: Построение списков частот")
        print("=" * 60)
        print("\nВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("1 - Основной режим")
        print("2 - Интерактивный режим")
        print("3 - Демонстрация на примерах")
        print("4 - Выйти")
        
        choice = input("Ваш выбор (1-4): ").strip()
        
        if choice == "1":
            # Основной режим
            lst = read_list()
            
            if lst:
                display_frequency_lists(lst, "РЕЗУЛЬТАТ")
                analyze_frequency_distribution(lst)
        
        elif choice == "2":
            interactive_mode()
        
        elif choice == "3":
            demonstrate_examples()
        
        elif choice == "4":
            print("Программа завершена. До свидания!")
            break
        
        else:
            print("❌ Неверный выбор. Пожалуйста, введите 1, 2, 3 или 4")

if __name__ == "__main__":
    main()