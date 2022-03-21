import numpy as np

from helper import DecisionHelper

if __name__ == '__main__':
    weights = [0.09,  # Уровень производительности
               0.13,  # Совместимость
               0.04,  # Удобство использования
               0.05,  # Модифицируемость
               0.1,  # Эстетика пользовательского интерфейса
               0.4,  # Функциональная полнота
               0.06,  # Изучаемость
               0.03]  # Используемость ресурсов

    # print("Введите количество продуктов:")
    # n = int(input())
    # m = [[] for y in range(n)]
    # for i in range(n):
    #     print("Продукт", i)
    #     for j in range(len(weights)):
    #         m[i].append(int(input()))
    #     print("\n")

    m = np.array([[3, 2, 3, 2, 1, 2, 3, 2],  # Blender
                  [2, 1, 3, 2, 1, 3, 1, 3],  # Zbrush
                  [1, 2, 1, 2, 3, 3, 1, 3, ], # Cinema 4D
                  [3, 1, 2, 1, 3, 2, 1, 2]])  # Adobe dimension

    dh = DecisionHelper(m, weights)
    print(dh.saw())
    print(dh.topsis())
    ar = dh.electre()
    for a in ar:
        for b in a:
            print(b, end=" ")
        print('\n')
