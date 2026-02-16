# -*- coding: utf-8 -*-
"""
Задание 1, Функция 2: Найти произведение цифр числа, не делящихся на 5
Вариант 3
"""

def product_of_digits_not_divisible_by_5():
    """
    Функция 2: Найти произведение цифр числа, не делящихся на 5.
    """
    print("=" * 60)
    print("ЗАДАНИЕ 1, ФУНКЦИЯ 2: Произведение цифр, не делящихся на 5")
    print("=" * 60)
    
    try:
        num = int(input("Введите число: "))
        
        if num == 0:
            print("Число равно 0, произведение = 0")
            return 0
        
        product = 1
        found = False
        digits_info = []
        
        for digit_char in str(abs(num)):
            digit = int(digit_char)
            if digit % 5 != 0:
                product *= digit
                found = True
                digits_info.append(f"{digit}(не делится на 5)")
            else:
                digits_info.append(f"{digit}(делится на 5, пропускаем)")
        
        print(f"Цифры числа: {', '.join(digits_info)}")
        
        if not found:
            print("Все цифры делятся на 5, произведение = 0")
            return 0
        
        print(f"Произведение цифр, не делящихся на 5: {product}")
        return product
        
    except ValueError:
        print("Ошибка: введите корректное целое число")
        return None

if __name__ == "__main__":
    product_of_digits_not_divisible_by_5()