# -*- coding: utf-8 -*-
"""
Задания с массивами, Задача 39: Вывести вначале элементы с четными индексами, а затем – с нечетными
Вариант 3
"""

def read_array():
    """
    Читает массив чисел с клавиатуры.
    
    Returns:
        list: Список введенных чисел
    """
    print("=" * 60)
    print("ВВОД МАССИВА ЧИСЕЛ")
    print("=" * 60)
    
    print("\nВведите элементы массива (целые числа), разделенные пробелом:")
    print("Например: 10 20 30 40 50 60")
    
    while True:
        try:
            line = input("➡ ").strip()
            if not line:
                print("❌ Массив не может быть пустым")
                continue
            
            # Разбиваем строку на части и преобразуем в целые числа
            elements = line.split()
            array = [int(x) for x in elements]
            
            print(f"\n✅ Введен массив из {len(array)} элементов:")
            print_array_with_indices(array)
            
            return array
            
        except ValueError:
            print("❌ Ошибка: все элементы должны быть целыми числами")
        except Exception as e:
            print(f"❌ Ошибка: {e}")

def print_array_with_indices(array, title="Массив"):
    """
    Выводит массив с индексами.
    
    Args:
        array (list): Исходный массив
        title (str): Заголовок
    """
    print(f"\n{title}:")
    print("   Индексы: ", end="")
    for i in range(len(array)):
        print(f"{i:4}", end=" ")
    print()
    
    print("   Значения:", end="")
    for x in array:
        print(f"{x:4}", end=" ")
    print()

def split_by_index_parity(array):
    """
    Разделяет массив на элементы с четными и нечетными индексами.
    
    Args:
        array (list): Исходный массив
        
    Returns:
        tuple: (элементы_с_четными_индексами, элементы_с_нечетными_индексами)
    """
    even_index_elements = []
    odd_index_elements = []
    
    for i, value in enumerate(array):
        if i % 2 == 0:
            even_index_elements.append(value)
        else:
            odd_index_elements.append(value)
    
    return even_index_elements, odd_index_elements

def combine_by_index_parity(array):
    """
    Объединяет элементы: сначала четные индексы, потом нечетные.
    
    Args:
        array (list): Исходный массив
        
    Returns:
        list: Новый массив с элементами, переставленными по индексам
    """
    even_elements, odd_elements = split_by_index_parity(array)
    return even_elements + odd_elements

def print_split_result(array):
    """
    Выводит результат разделения массива.
    
    Args:
        array (list): Исходный массив
    """
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТ РАЗДЕЛЕНИЯ ПО ИНДЕКСАМ")
    print("=" * 60)
    
    print_array_with_indices(array, "Исходный массив")
    
    even_elements, odd_elements = split_by_index_parity(array)
    
    print(f"\n📊 Элементы с ЧЕТНЫМИ индексами (0, 2, 4, ...):")
    if even_elements:
        print(f"   Количество: {len(even_elements)}")
        print(f"   Значения: {even_elements}")
        
        # Показываем исходные индексы
        indices = [i for i in range(len(array)) if i % 2 == 0]
        print(f"   Индексы: {indices}")
    else:
        print("   Нет элементов с четными индексами")
    
    print(f"\n📊 Элементы с НЕЧЕТНЫМИ индексами (1, 3, 5, ...):")
    if odd_elements:
        print(f"   Количество: {len(odd_elements)}")
        print(f"   Значения: {odd_elements}")
        
        # Показываем исходные индексы
        indices = [i for i in range(len(array)) if i % 2 != 0]
        print(f"   Индексы: {indices}")
    else:
        print("   Нет элементов с нечетными индексами")
    
    # Объединенный результат
    combined = even_elements + odd_elements
    
    print(f"\n📦 ИТОГОВЫЙ МАССИВ (четные индексы, затем нечетные):")
    print(f"   {combined}")
    
    # Визуализация
    print(f"\n📈 Визуализация перестановки:")
    print(f"   Исходный:  {array}")
    print(f"   Результат: {combined}")
    
    # Показываем соответствие
    print(f"\n🔄 Соответствие элементов:")
    for i, val in enumerate(array):
        if i % 2 == 0:
            new_pos = i // 2
            print(f"   Элемент [{i}] = {val} → позиция {new_pos} в четной части")
        else:
            new_pos = len(even_elements) + (i // 2)
            print(f"   Элемент [{i}] = {val} → позиция {new_pos} в нечетной части")

def analyze_parity_distribution(array):
    """
    Анализирует распределение элементов по четности индексов.
    
    Args:
        array (list): Исходный массив
    """
    print("\n" + "=" * 60)
    print("АНАЛИЗ РАСПРЕДЕЛЕНИЯ ПО ИНДЕКСАМ")
    print("=" * 60)
    
    even_elements, odd_elements = split_by_index_parity(array)
    
    print(f"\n📊 СТАТИСТИКА:")
    print(f"   Всего элементов: {len(array)}")
    print(f"   Четные индексы: {len(even_elements)} ({len(even_elements)/len(array)*100:.1f}%)")
    print(f"   Нечетные индексы: {len(odd_elements)} ({len(odd_elements)/len(array)*100:.1f}%)")
    
    # Сравнение сумм
    sum_even = sum(even_elements)
    sum_odd = sum(odd_elements)
    
    print(f"\n💰 Суммы:")
    print(f"   Сумма четных индексов: {sum_even}")
    print(f"   Сумма нечетных индексов: {sum_odd}")
    print(f"   Разница: {abs(sum_even - sum_odd)}")
    
    if sum_even > sum_odd:
        print(f"   Сумма четных больше на {sum_even - sum_odd}")
    elif sum_odd > sum_even:
        print(f"   Сумма нечетных больше на {sum_odd - sum_even}")
    else:
        print(f"   Суммы равны")
    
    # Сравнение средних
    if even_elements:
        avg_even = sum_even / len(even_elements)
        print(f"   Среднее четных: {avg_even:.2f}")
    if odd_elements:
        avg_odd = sum_odd / len(odd_elements)
        print(f"   Среднее нечетных: {avg_odd:.2f}")

def filter_by_parity(array, keep_even_indices=True):
    """
    Фильтрует массив, оставляя элементы только с четными или нечетными индексами.
    
    Args:
        array (list): Исходный массив
        keep_even_indices (bool): True для четных индексов, False для нечетных
        
    Returns:
        list: Отфильтрованный массив
    """
    result = []
    for i, value in enumerate(array):
        if keep_even_indices and i % 2 == 0:
            result.append(value)
        elif not keep_even_indices and i % 2 != 0:
            result.append(value)
    
    return result

def compare_with_alternative(array):
    """
    Сравнивает разные способы разделения.
    
    Args:
        array (list): Исходный массив
    """
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ СПОСОБОВ РАЗДЕЛЕНИЯ")
    print("=" * 60)
    
    print_array_with_indices(array, "Исходный массив")
    
    # Способ 1: Наш метод
    even1, odd1 = split_by_index_parity(array)
    result1 = even1 + odd1
    
    # Способ 2: С использованием срезов
    even2 = array[::2]  # каждый второй, начиная с 0
    odd2 = array[1::2]  # каждый второй, начиная с 1
    result2 = even2 + odd2
    
    print(f"\n📊 Способ 1 (цикл):")
    print(f"   Четные: {even1}")
    print(f"   Нечетные: {odd1}")
    print(f"   Результат: {result1}")
    
    print(f"\n📊 Способ 2 (срезы):")
    print(f"   Четные: {even2}")
    print(f"   Нечетные: {odd2}")
    print(f"   Результат: {result2}")
    
    print(f"\n✅ Результаты совпадают: {result1 == result2}")

def demonstrate_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ НА ПРИМЕРАХ")
    print("=" * 60)
    
    examples = [
        [10, 20, 30, 40, 50, 60],
        [1, 2, 3, 4, 5],
        [100, 200, 300],
        [42],
        [1, -2, 3, -4, 5, -6, 7]
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n--- Пример {i} ---")
        print(f"Исходный массив: {example}")
        
        even, odd = split_by_index_parity(example)
        result = even + odd
        
        print(f"Четные индексы: {even}")
        print(f"Нечетные индексы: {odd}")
        print(f"Результат: {result}")

def interactive_mode():
    """
    Интерактивный режим с дополнительными возможностями.
    """
    print("\n" + "=" * 60)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("=" * 60)
    
    array = read_array()
    
    if not array:
        return
    
    while True:
        print("\n" + "-" * 40)
        print("ВЫБЕРИТЕ ДЕЙСТВИЕ:")
        print("1 - Разделить по четности индексов")
        print("2 - Показать только четные индексы")
        print("3 - Показать только нечетные индексы")
        print("4 - Анализ распределения")
        print("5 - Сравнить способы разделения")
        print("6 - Ввести новый массив")
        print("7 - Вернуться в главное меню")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            print_split_result(array)
        
        elif choice == "2":
            even = filter_by_parity(array, keep_even_indices=True)
            print(f"\n📊 Элементы с четными индексами:")
            print(f"   {even}")
            
            indices = [i for i in range(len(array)) if i % 2 == 0]
            print(f"   Индексы: {indices}")
        
        elif choice == "3":
            odd = filter_by_parity(array, keep_even_indices=False)
            print(f"\n📊 Элементы с нечетными индексами:")
            print(f"   {odd}")
            
            indices = [i for i in range(len(array)) if i % 2 != 0]
            print(f"   Индексы: {indices}")
        
        elif choice == "4":
            analyze_parity_distribution(array)
        
        elif choice == "5":
            compare_with_alternative(array)
        
        elif choice == "6":
            array = read_array()
            if not array:
                return
        
        elif choice == "7":
            break
        
        else:
            print("❌ Неверный выбор")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ЗАДАНИЯ С МАССИВАМИ, ЗАДАЧА 39: Вывод элементов по индексам")
        print("=" * 60)
        print("\nВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("1 - Основной режим")
        print("2 - Интерактивный режим")
        print("3 - Демонстрация на примерах")
        print("4 - Выйти")
        
        choice = input("Ваш выбор (1-4): ").strip()
        
        if choice == "1":
            # Основной режим
            array = read_array()
            
            if array:
                print_split_result(array)
        
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