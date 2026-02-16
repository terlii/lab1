# -*- coding: utf-8 -*-
"""
Задание 1, Функция 1: Найти максимальный простой делитель числа
Вариант 3
"""

import math

def is_prime(n):
    """
    Проверяет, является ли число простым.

    Аргументы:
    n (int): Проверяемое число

    Returns:
    bool: True если число простое, False если составное
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Проверяем делители до квадратного корня из n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def find_divisors(n):
    """
    Находит все положительные делители числа.
    
    Аргументы:
        n (int): Исходное число
        
    Returns:
        list: Отсортированный список всех делителей
    """
    divisors = []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    return sorted(divisors)

def max_prime_divisor():
    """
    Основная функция: находит максимальный простой делитель числа.
    """
    print("=" * 60)
    print("ЗАДАНИЕ 1, ФУНКЦИЯ 1: Максимальный простой делитель числа")
    print("=" * 60)
    
    try:
        num = int(input("Введите целое число: "))
        print(f"\nАнализируем число: {num}")
        
        if num <= 1:
            print(f"Число {num} не имеет простых делителей (должно быть > 1)")
            return None
        
        all_divisors = find_divisors(num)
        print(f"Все делители числа {num}: {all_divisors}")
        
        prime_divisors = []
        for d in all_divisors:
            if is_prime(d):
                prime_divisors.append(d)
        
        if not prime_divisors:
            print(f"У числа {num} нет простых делителей")
            return None
        
        result = max(prime_divisors)
        
        print(f"Простые делители числа {num}: {prime_divisors}")
        print(f"Максимальный простой делитель: {result}")
        print(f"\nПроверка: {num} / {result} = {num // result}")
        
        return result
        
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число")
        return None
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
    
    test_numbers = [84, 97, 100, 13, 24, 49]
    
    for num in test_numbers:
        print(f"\n--- Тест с числом {num} ---")
        all_divisors = find_divisors(num)
        prime_divisors = [d for d in all_divisors if is_prime(d)]
        
        print(f"Делители: {all_divisors}")
        print(f"Простые делители: {prime_divisors}")
        
        if prime_divisors:
            max_prime = max(prime_divisors)
            print(f"Максимальный простой делитель: {max_prime}")
        else:
            print(f"У числа {num} нет простых делителей")

def main():
    """
    Главная функция программы.
    """
    while True:
        print("\n" + "=" * 60)
        print("ВЫБЕРИТЕ РЕЖИМ РАБОТЫ:")
        print("=" * 60)
        print("1 - Ввести свое число")
        print("2 - Посмотреть демонстрацию на примерах")
        print("3 - Выйти")
        
        choice = input("Ваш выбор (1/2/3): ").strip()
        
        if choice == "1":
            max_prime_divisor()
        elif choice == "2":
            demonstrate_examples()
        elif choice == "3":
            print("Программа завершена. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 3")

if __name__ == "__main__":
    main()