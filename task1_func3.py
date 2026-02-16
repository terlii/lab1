# -*- coding: utf-8 -*-
"""
Задание 1, Функция 3: Найти НОД максимального нечетного непростого делителя 
                     и произведения цифр числа
Вариант 3
"""

import math

def is_prime(n):
    """Проверяет, является ли число простым."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_divisors(n):
    """Возвращает список всех положительных делителей числа."""
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

def gcd(a, b):
    """Находит наибольший общий делитель (НОД)."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def gcd_odd_composite_divisor_and_digit_product():
    """
    Функция 3: Найти НОД максимального нечетного непростого делителя числа
              и произведения цифр данного числа.
    """
    print("=" * 60)
    print("ЗАДАНИЕ 1, ФУНКЦИЯ 3: НОД нечетного непростого делителя и произведения цифр")
    print("=" * 60)
    
    try:
        num = int(input("Введите число: "))
        
        if num <= 1:
            print(f"Число {num} не имеет составных делителей")
            return None
        
        # Находим все делители
        divisors = find_divisors(num)
        print(f"Все делители числа {num}: {divisors}")
        
        # Нечетные, не простые и не 1
        odd_composite_divisors = [d for d in divisors if d % 2 != 0 and not is_prime(d) and d > 1]
        
        if not odd_composite_divisors:
            print(f"У числа {num} нет нечетных непростых делителей (кроме 1)")
            return None
        
        max_odd_composite = max(odd_composite_divisors)
        print(f"Нечетные непростые делители: {odd_composite_divisors}")
        print(f"Максимальный нечетный непростой делитель: {max_odd_composite}")
        
        # Произведение всех цифр числа
        if num == 0:
            all_digit_product = 0
        else:
            all_digit_product = 1
            for digit_char in str(abs(num)):
                all_digit_product *= int(digit_char)
        
        print(f"Произведение всех цифр числа {num}: {all_digit_product}")
        
        if all_digit_product == 0:
            print("Произведение цифр равно 0, НОД = 0")
            return 0
        
        result = gcd(max_odd_composite, all_digit_product)
        print(f"НОД({max_odd_composite}, {all_digit_product}) = {result}")
        
        return result
        
    except ValueError:
        print("Ошибка: введите корректное целое число")
        return None

if __name__ == "__main__":
    gcd_odd_composite_divisor_and_digit_product()