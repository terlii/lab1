# -*- coding: utf-8 -*-
"""
Задания с массивами, Задача 3: Дан целочисленный массив и натуральный индекс.
Определить, является ли элемент по указанному индексу глобальным максимумом.
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
    print("Например: 5 12 7 3 9 1")
    
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

def print_array_with_indices(array):
    """
    Выводит массив с индексами.
    
    Args:
        array (list): Исходный массив
    """
    print("   Индексы: ", end="")
    for i in range(len(array)):
        print(f"{i:4}", end=" ")
    print()
    
    print("   Значения:", end="")
    for x in array:
        print(f"{x:4}", end=" ")
    print()

def read_index(array):
    """
    Читает индекс с клавиатуры.
    
    Args:
        array (list): Исходный массив
        
    Returns:
        int: Введенный индекс
    """
    print("\n" + "=" * 60)
    print("ВВОД ИНДЕКСА")
    print("=" * 60)
    
    max_index = len(array) - 1
    
    while True:
        try:
            print(f"\nВведите индекс элемента (от 0 до {max_index}):")
            index = int(input("➡ ").strip())
            
            if 0 <= index <= max_index:
                print(f"\n✅ Выбран индекс: {index}")
                return index
            else:
                print(f"❌ Индекс должен быть от 0 до {max_index}")
                
        except ValueError:
            print("❌ Ошибка: введите целое число")
        except Exception as e:
            print(f"❌ Ошибка: {e}")

def is_global_maximum(array, index):
    """
    Проверяет, является ли элемент по индексу глобальным максимумом.
    
    Args:
        array (list): Исходный массив
        index (int): Проверяемый индекс
        
    Returns:
        bool: True если элемент является глобальным максимумом
    """
    if not array or index < 0 or index >= len(array):
        return False
    
    element = array[index]
    max_element = max(array)
    
    return element == max_element

def check_global_maximum():
    """
    Основная функция для проверки глобального максимума.
    """
    print("=" * 60)
    print("ЗАДАНИЕ С МАССИВАМИ, ЗАДАЧА 3: Проверка глобального максимума")
    print("=" * 60)
    
    # Ввод массива
    array = read_array()
    
    if not array:
        print("❌ Массив пуст")
        return
    
    # Ввод индекса
    index = read_index(array)
    
    # Проверка
    element = array[index]
    is_max = is_global_maximum(array, index)
    max_element = max(array)
    
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТ")
    print("=" * 60)
    
    print(f"\n📊 Анализируемый массив:")
    print_array_with_indices(array)
    
    print(f"\n🔍 Проверяемый элемент:")
    print(f"   Индекс: {index}")
    print(f"   Значение: {element}")
    print(f"   Максимальный элемент в массиве: {max_element}")
    
    if is_max:
        print(f"\n✅ РЕЗУЛЬТАТ: Элемент [{index}] = {element} ЯВЛЯЕТСЯ глобальным максимумом!")
        
        # Находим все индексы с максимальным значением
        max_indices = [i for i, x in enumerate(array) if x == max_element]
        if len(max_indices) > 1:
            print(f"   (максимум встречается также на индексах: {max_indices})")
    else:
        print(f"\n❌ РЕЗУЛЬТАТ: Элемент [{index}] = {element} НЕ ЯВЛЯЕТСЯ глобальным максимумом")
        print(f"   Максимум = {max_element} на индексе {array.index(max_element)}")

def demonstrate_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ НА ПРИМЕРАХ")
    print("=" * 60)
    
    examples = [
        ([5, 12, 7, 3, 9, 1], 1),    # 12 - максимум
        ([5, 12, 7, 3, 9, 1], 0),    # 5 - не максимум
        ([1, 2, 3, 4, 5], 4),         # 5 - максимум
        ([10, 10, 10, 10], 2),        # 10 - максимум (повторяется)
        ([-5, -2, -8, -1], 3)         # -1 - максимум
    ]
    
    for i, (array, index) in enumerate(examples, 1):
        print(f"\n--- Пример {i} ---")
        print(f"Массив: {array}")
        print(f"Индекс: {index}")
        
        element = array[index]
        is_max = is_global_maximum(array, index)
        max_element = max(array)
        
        print(f"Элемент [{index}] = {element}")
        print(f"Максимум в массиве = {max_element}")
        
        if is_max:
            print(f"✅ Элемент ЯВЛЯЕТСЯ глобальным максимумом")
        else:
            print(f"❌ Элемент НЕ ЯВЛЯЕТСЯ глобальным максимумом")

def find_all_maxima(array):
    """
    Находит все индексы, где достигается максимум.
    
    Args:
        array (list): Исходный массив
        
    Returns:
        list: Список индексов максимальных элементов
    """
    if not array:
        return []
    
    max_val = max(array)
    return [i for i, x in enumerate(array) if x == max_val]

def compare_with_threshold(array, threshold):
    """
    Сравнивает элементы с пороговым значением.
    
    Args:
        array (list): Исходный массив
        threshold (int): Пороговое значение
        
    Returns:
        dict: Статистика сравнения
    """
    above = [x for x in array if x > threshold]
    equal = [x for x in array if x == threshold]
    below = [x for x in array if x < threshold]
    
    return {
        'above': above,
        'equal': equal,
        'below': below,
        'count_above': len(above),
        'count_equal': len(equal),
        'count_below': len(below)
    }

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
        print("1 - Проверить элемент по индексу")
        print("2 - Найти все максимумы")
        print("3 - Сравнить с пороговым значением")
        print("4 - Показать статистику массива")
        print("5 - Ввести новый массив")
        print("6 - Вернуться в главное меню")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            index = read_index(array)
            element = array[index]
            is_max = is_global_maximum(array, index)
            max_element = max(array)
            
            print(f"\n📊 Результат:")
            print(f"   Элемент [{index}] = {element}")
            print(f"   Максимум = {max_element}")
            
            if is_max:
                print(f"   ✅ Элемент ЯВЛЯЕТСЯ глобальным максимумом")
            else:
                print(f"   ❌ Элемент НЕ ЯВЛЯЕТСЯ глобальным максимумом")
        
        elif choice == "2":
            max_indices = find_all_maxima(array)
            max_value = max(array)
            
            print(f"\n📊 Максимальное значение: {max_value}")
            print(f"   Встречается на индексах: {max_indices}")
            print(f"   Количество вхождений: {len(max_indices)}")
        
        elif choice == "3":
            try:
                threshold = int(input("Введите пороговое значение: "))
                stats = compare_with_threshold(array, threshold)
                
                print(f"\n📊 Сравнение с порогом {threshold}:")
                print(f"   Больше порога: {stats['count_above']} элементов {stats['above']}")
                print(f"   Равно порогу: {stats['count_equal']} элементов {stats['equal']}")
                print(f"   Меньше порога: {stats['count_below']} элементов {stats['below']}")
                
            except ValueError:
                print("❌ Ошибка: введите целое число")
        
        elif choice == "4":
            print(f"\n📊 Статистика массива:")
            print(f"   Размер: {len(array)} элементов")
            print(f"   Минимум: {min(array)}")
            print(f"   Максимум: {max(array)}")
            print(f"   Сумма: {sum(array)}")
            print(f"   Среднее: {sum(array) / len(array):.2f}")
            
            # Уникальные значения
            unique_values = set(array)
            print(f"   Уникальных значений: {len(unique_values)}")
        
        elif choice == "5":
            array = read_array()
            if not array:
                return
        
        elif choice == "6":
            break
        
        else:
            print("❌ Неверный выбор")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ЗАДАНИЯ С МАССИВАМИ, ЗАДАЧА 3: Проверка глобального максимума")
        print("=" * 60)
        print("\nВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("1 - Основной режим")
        print("2 - Интерактивный режим")
        print("3 - Демонстрация на примерах")
        print("4 - Выйти")
        
        choice = input("Ваш выбор (1-4): ").strip()
        
        if choice == "1":
            check_global_maximum()
        
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