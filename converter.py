"""Конвертер величин: длина, масса, температура."""
import os

ROUND_DIGITS = int(os.environ.get("ROUND_DIGITS", 2))

def km_to_miles(km):
    return round(km * 0.621371, ROUND_DIGITS)

def kg_to_pounds(kg):
    return kg * 2.20462

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def read_values(path):
    """Читает файл, по одному числу на строку."""
    with open(path, encoding="utf-8") as f:
        return [float(line.strip()) for line in f if line.strip()]

def batch_convert(values, func):
    """Применяет func к каждому значению."""
    return [func(v) for v in values]

if __name__ == "__main__":
    print("10 км =", km_to_miles(10), "миль")
    print("5 кг =", kg_to_pounds(5), "фунтов")
    print("25 °C =", celsius_to_fahrenheit(25), "°F")

    values = read_values("values.txt")
    print("Пакетно в мили:", batch_convert(values, km_to_miles))