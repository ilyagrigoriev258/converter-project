"""Конвертер величин: длина."""

def km_to_miles(km):
    return km * 0.621371

if __name__ == "__main__":
    print("10 км =", km_to_miles(10), "миль")
"""Конвертер величин: длина и масса."""

def km_to_miles(km):
    return km * 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

if __name__ == "__main__":
    print("10 км =", km_to_miles(10), "миль")
    print("5 кг =", kg_to_pounds(5), "фунтов")