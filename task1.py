import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt

# Функция для проверки попадания точки в фигуру
def is_inside_figure(x, y):
    # Условия, ограничивающие область фигуры
    return (-x**2 + y**3 < -1) and (x + y < 1) and (-2 < x < 2) and (-2 < y < 2)

# Функция для выполнения метода Монте-Карло
def monte_carlo_area(N):
    inside_count = 0
    points_inside = []
    points_outside = []

    for _ in range(N):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)
        if is_inside_figure(x, y):
            inside_count += 1
            points_inside.append((x, y))
        else:
            points_outside.append((x, y))

    square_area = 16  # Площадь квадрата 4x4
    figure_area = (inside_count / N) * square_area

    return figure_area, points_inside, points_outside

# Функция для отображения результата
def show_result():
    try:
        N = int(entry_N.get())
        if N <= 0:
            raise ValueError

        area, points_inside, points_outside = monte_carlo_area(N)

        # Отображение результата
        messagebox.showinfo("Результат", f"Площадь фигуры: {area}")

        # Построение графика
        plt.figure(figsize=(6, 6))
        if points_inside: # Check if there are any points inside
            plt.scatter(*zip(*points_inside), color='blue', s=1, label='Внутри фигуры')
        if points_outside: # Check if there are any points outside
            plt.scatter(*zip(*points_outside), color='red', s=1, label='Снаружи фигуры')
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.legend()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.title('Метод Монте-Карло: Вычисление площади фигуры')
        plt.show()

    except ValueError:
        messagebox.showerror("Ошибка", "Введите положительное целое число для N")

# Создание графического интерфейса
root = tk.Tk()
root.title("Метод Монте-Карло: Вычисление площади фигуры")

tk.Label(root, text="Введите число испытаний N:").pack(pady=10)
entry_N = tk.Entry(root)
entry_N.pack(pady=5)

tk.Button(root, text="Рассчитать площадь", command=show_result).pack(pady=20)

root.mainloop()
