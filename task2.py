import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
import numpy as np

# Функция для интегрирования
def func(x):
    return x / (1 + x**2)

# Аналитическое решение интеграла
def analytical_integral():
    return 0.5 * np.log(2)

# Функция для выполнения метода Монте-Карло
def monte_carlo_integration(N):
    a, b = 0, 1
    inside_count = 0
    points_inside = []

    for _ in range(N):
        x = random.uniform(a, b)
        y = random.uniform(0, 1)  # Генерируем случайную высоту [0, 1]
        if y <= func(x):
            inside_count += 1
            points_inside.append((x, y))

    integral_value = (b - a) * (inside_count / N)
    return integral_value, points_inside

# Функция для отображения результата
def show_result():
    try:
        N = int(entry_N.get())
        if N <= 0:
            raise ValueError
        
        integral_value, points_inside = monte_carlo_integration(N)
        analytical_value = analytical_integral()
        relative_error = abs((integral_value - analytical_value) / analytical_value)

        # Отображение результата
        messagebox.showinfo("Результат", 
                            f"Интеграл (Метод Монте-Карло): {integral_value}\n"
                            f"Аналитическое значение: {analytical_value}\n"
                            f"Относительная погрешность: {relative_error}")

        # Построение графика
        x = np.linspace(0, 1, 400)
        y = func(x)

        plt.figure(figsize=(8, 5))
        plt.plot(x, y, label='x / (1 + x^2)')
        plt.fill_between(x, y, alpha=0.3)

        if points_inside:
            points_x, points_y = zip(*points_inside)
            plt.scatter(points_x, points_y, color='red', s=5, label='Точки Монте-Карло')

        plt.title('Интегрирование x / (1 + x^2) на [0, 1] методом Монте-Карло')
        plt.xlabel('x')
        plt.ylabel('x / (1 + x^2)')
        plt.legend(loc='upper left')
        plt.show()

    except ValueError:
        messagebox.showerror("Ошибка", "Введите положительное целое число для N")

# Создание графического интерфейса
root = tk.Tk()
root.title("Метод Монте-Карло: Вычисление интеграла")

tk.Label(root, text="Введите число испытаний N:").pack(pady=10)
entry_N = tk.Entry(root)
entry_N.pack(pady=5)

tk.Button(root, text="Рассчитать интеграл", command=show_result).pack(pady=20)

root.mainloop()
