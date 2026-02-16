# -*- coding: utf-8 -*-
"""
Задания с массивами, Задача 15: Дан целочисленный массив и натуральный индекс.
Определить, является ли элемент по указанному индексу локальным минимумом.
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

def is_local_minimum(array, index):
    """
    Проверяет, является ли элемент по индексу локальным минимумом.
    
    Локальный минимум - элемент, который меньше своих соседей.
    Для крайних элементов сравнивается только с одним соседом.
    
    Args:
        array (list): Исходный массив
        index (int): Проверяемый индекс
        
    Returns:
        bool: True если элемент является локальным минимумом
    """
    if not array or index < 0 or index >= len(array):
        return False
    
    n = len(array)
    
    # Для массива из одного элемента
    if n == 1:
        return True
    
    # Для первого элемента
    if index == 0:
        return array[index] < array[index + 1]
    
    # Для последнего элемента
    if index == n - 1:
        return array[index] < array[index - 1]
    
    # Для остальных элементов
    return array[index] < array[index - 1] and array[index] < array[index + 1]

def check_local_minimum():
    """
    Основная функция для проверки локального минимума.
    """
    print("=" * 60)
    print("ЗАДАНИЯ С МАССИВАМИ, ЗАДАЧА 15: Проверка локального минимума")
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
    is_min = is_local_minimum(array, index)
    
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТ")
    print("=" * 60)
    
    print(f"\n📊 Анализируемый массив:")
    print_array_with_indices(array)
    
    print(f"\n🔍 Проверяемый элемент:")
    print(f"   Индекс: {index}")
    print(f"   Значение: {element}")
    
    # Показываем соседей
    n = len(array)
    if n == 1:
        print("   Соседи: нет (единственный элемент)")
    elif index == 0:
        print(f"   Сосед справа: [{index + 1}] = {array[index + 1]}")
    elif index == n - 1:
        print(f"   Сосед слева: [{index - 1}] = {array[index - 1]}")
    else:
        print(f"   Сосед слева: [{index - 1}] = {array[index - 1]}")
        print(f"   Сосед справа: [{index + 1}] = {array[index + 1]}")
    
    if is_min:
        print(f"\n✅ РЕЗУЛЬТАТ: Элемент [{index}] = {element} ЯВЛЯЕТСЯ локальным минимумом!")
    else:
        print(f"\n❌ РЕЗУЛЬТАТ: Элемент [{index}] = {element} НЕ ЯВЛЯЕТСЯ локальным минимумом")

def find_all_local_minima(array):
    """
    Находит все локальные минимумы в массиве.
    
    Args:
        array (list): Исходный массив
        
    Returns:
        list: Список индексов локальных минимумов
    """
    if not array:
        return []
    
    minima = []
    n = len(array)
    
    for i in range(n):
        if is_local_minimum(array, i):
            minima.append(i)
    
    return minima

def find_all_local_maxima(array):
    """
    Находит все локальные максимумы в массиве.
    
    Args:
        array (list): Исходный массив
        
    Returns:
        list: Список индексов локальных максимумов
    """
    if not array:
        return []
    
    maxima = []
    n = len(array)
    
    for i in range(n):
        # Проверка на локальный максимум
        if n == 1:
            maxima.append(i)
        elif i == 0:
            if array[i] > array[i + 1]:
                maxima.append(i)
        elif i == n - 1:
            if array[i] > array[i - 1]:
                maxima.append(i)
        else:
            if array[i] > array[i - 1] and array[i] > array[i + 1]:
                maxima.append(i)
    
    return maxima

def demonstrate_examples():
    """
    Демонстрирует работу на примерах.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ НА ПРИМЕРАХ")
    print("=" * 60)
    
    examples = [
        ([5, 3, 7, 2, 9, 4], 1),    # 3 - локальный минимум?
        ([5, 3, 7, 2, 9, 4], 3),    # 2 - локальный минимум
        ([1, 2, 3, 4, 5], 0),        # 1 - локальный минимум (крайний)
        ([5, 4, 3, 2, 1], 4),        # 1 - локальный минимум (крайний)
        ([10, 10, 10, 10], 2),       # 10 - не минимум (равен соседям)
        ([42], 0)                     # Единственный элемент
    ]
    
    for i, (array, index) in enumerate(examples, 1):
        print(f"\n--- Пример {i} ---")
        print(f"Массив: {array}")
        print(f"Индекс: {index}")
        
        element = array[index]
        is_min = is_local_minimum(array, index)
        
        print(f"Элемент [{index}] = {element}")
        
        # Показываем соседей
        n = len(array)
        if n == 1:
            print("   Соседи: нет")
        elif index == 0:
            print(f"   Сосед справа: [{index + 1}] = {array[index + 1]}")
        elif index == n - 1:
            print(f"   Сосед слева: [{index - 1}] = {array[index - 1]}")
        else:
            print(f"   Слева: {array[index - 1]}, Справа: {array[index + 1]}")
        
        if is_min:
            print(f"✅ Элемент ЯВЛЯЕТСЯ локальным минимумом")
        else:
            print(f"❌ Элемент НЕ ЯВЛЯЕТСЯ локальным минимумом")

def analyze_local_extrema(array):
    """
    Анализирует все локальные экстремумы в массиве.
    
    Args:
        array (list): Исходный массив
    """
    if not array:
        return
    
    print("\n" + "=" * 60)
    print("АНАЛИЗ ЛОКАЛЬНЫХ ЭКСТРЕМУМОВ")
    print("=" * 60)
    
    minima = find_all_local_minima(array)
    maxima = find_all_local_maxima(array)
    
    print(f"\n📊 Массив: {array}")
    print(f"\n🔽 Локальные минимумы:")
    if minima:
        for i in minima:
            print(f"   [{i}] = {array[i]}")
    else:
        print("   Не найдены")
    
    print(f"\n🔼 Локальные максимумы:")
    if maxima:
        for i in maxima:
            print(f"   [{i}] = {array[i]}")
    else:
        print("   Не найдены")
    
    # Визуализация
    print(f"\n📈 Визуализация:")
    print("   Индексы: ", end="")
    for i in range(len(array)):
        print(f"{i:4}", end=" ")
    print()
    
    print("   Значения:", end="")
    for i, x in enumerate(array):
        if i in minima:
            print(f"↓{x:3}", end=" ")
        elif i in maxima:
            print(f"↑{x:3}", end=" ")
        else:
            print(f" {x:3}", end=" ")
    print()

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
        print("2 - Найти все локальные минимумы")
        print("3 - Найти все локальные максимумы")
        print("4 - Полный анализ экстремумов")
        print("5 - Показать статистику массива")
        print("6 - Ввести новый массив")
        print("7 - Вернуться в главное меню")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            index = read_index(array)
            element = array[index]
            is_min = is_local_minimum(array, index)
            
            print(f"\n📊 Результат для индекса {index}:")
            print(f"   Элемент = {element}")
            
            # Показываем соседей
            n = len(array)
            if n == 1:
                print("   Соседи: нет")
            elif index == 0:
                print(f"   Сосед справа: {array[index + 1]}")
            elif index == n - 1:
                print(f"   Сосед слева: {array[index - 1]}")
            else:
                print(f"   Слева: {array[index - 1]}, Справа: {array[index + 1]}")
            
            if is_min:
                print(f"   ✅ Элемент ЯВЛЯЕТСЯ локальным минимумом")
            else:
                print(f"   ❌ Элемент НЕ ЯВЛЯЕТСЯ локальным минимумом")
        
        elif choice == "2":
            minima = find_all_local_minima(array)
            print(f"\n📊 Локальные минимумы:")
            if minima:
                for i in minima:
                    print(f"   [{i}] = {array[i]}")
                print(f"   Всего: {len(minima)}")
            else:
                print("   Не найдены")
        
        elif choice == "3":
            maxima = find_all_local_maxima(array)
            print(f"\n📊 Локальные максимумы:")
            if maxima:
                for i in maxima:
                    print(f"   [{i}] = {array[i]}")
                print(f"   Всего: {len(maxima)}")
            else:
                print("   Не найдены")
        
        elif choice == "4":
            analyze_local_extrema(array)
        
        elif choice == "5":
            print(f"\n📊 Статистика массива:")
            print(f"   Размер: {len(array)} элементов")
            print(f"   Минимум: {min(array)} на индексе {array.index(min(array))}")
            print(f"   Максимум: {max(array)} на индексе {array.index(max(array))}")
            print(f"   Сумма: {sum(array)}")
            print(f"   Среднее: {sum(array) / len(array):.2f}")
            
            # Проверка на монотонность
            is_increasing = all(array[i] <= array[i+1] for i in range(len(array)-1))
            is_decreasing = all(array[i] >= array[i+1] for i in range(len(array)-1))
            
            if is_increasing:
                print(f"   Массив монотонно возрастает")
            elif is_decreasing:
                print(f"   Массив монотонно убывает")
            else:
                print(f"   Массив не монотонен")
        
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
        print("ЗАДАНИЯ С МАССИВАМИ, ЗАДАЧА 15: Проверка локального минимума")
        print("=" * 60)
        print("\nВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("1 - Основной режим")
        print("2 - Интерактивный режим")
        print("3 - Демонстрация на примерах")
        print("4 - Выйти")
        
        choice = input("Ваш выбор (1-4): ").strip()
        
        if choice == "1":
            check_local_minimum()
        
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