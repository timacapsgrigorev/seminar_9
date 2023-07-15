import csv
import json
import math
from functools import wraps
from random import randint


def find_roots(a, b, c):
    """Нахождение корней квадратного уравнения"""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return None


def generate_csv(filename, rows):
    """Генерация csv файла"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(rows):
            row = [randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

def run_with_csv(func):
    """Декоратор для выполнения функции с каждой тройкой чисел из csv файла"""
    @wraps(func)
    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) == 3:
                    a, b, c = map(int, row)
                    result = func(a, b, c)
                    print(f"Roots for {a}, {b}, {c}: {result}")
    return wrapper

def save_to_json(filename):
    """Декоратор для сохранения параметров и результатов работы функции в json файл"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                'args': args,
                'kwargs': kwargs,
                'result': result
            }
            with open(filename, 'w') as jsonfile:
                json.dump(data, jsonfile)
            return result
        return wrapper
    return decorator
 """Пример использования функции нахождения корней квадратного уравнения"""
roots = find_roots(1, -5, 6)
print(roots)  # (3.0, 2.0)

"""Пример использования функции генерации csv файла"""
generate_csv('random_numbers.csv', 10)

"""Пример использования декоратора для выполнения функции с каждой тройкой чисел из csv файла"""
@run_with_csv
def find_roots_csv(a, b, c):
    return find_roots(a, b, c)

find_roots_csv('random_numbers.csv')

"""Пример использования декоратора для сохранения параметров и результатов работы функции в json файл"""
@save_to_json('result.json')
def square(x):
    return x ** 2

square(5)
