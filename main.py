import numpy as np

from helper import DecisionHelper

if __name__ == '__main__':
    weights = [0.09,  # Уровень производительности
               0.13,  # Совместимость
               0.2,  # Удобство использования
               0.05,  # Модифицируемость
               0.1,  # Эстетика пользовательского интерфейса
               0.16,  # Функциональная полнота
               0.06,  # Изучаемость
               0.03]  # Используемость ресурсов

    print("Введите количество продуктов:")
    n = int(input())
    m = [[] for y in range(n)]
    for i in range(n):
        print("Продукт", i)
        for j in range(len(weights)):
            m[i].append(int(input()))
        print("\n")

    dh = DecisionHelper(m, weights)
    print(dh.saw())
    print(dh.topsis())
    print(dh.electre())
