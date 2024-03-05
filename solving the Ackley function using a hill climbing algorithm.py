import numpy as np


def ackley_function(x, y):

    a = 20
    b = 0.2
    c = 2 * np.pi
    d = 2
    return -a * np.exp(-b * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(
        c * np.cos(d * x) + c * np.cos(d * y)
    ) + a + np.exp(1)


def hill_climbing(function, bounds, step_size, tekrar):
    x = np.random.uniform(low=bounds[:, 0], high=bounds[:, 1])

    best_x = x.copy()
    best_value = function(*x)

    for _ in range(tekrar):
        for i in range(len(x)):
            new_x = x.copy()
            new_x[i] += step_size
            if new_x[i] <= bounds[i, 1]:
                new_value = function(*new_x)
                if new_value > best_value:
                    best_x = new_x.copy()
                    best_value = new_value

            new_x = x.copy()
            new_x[i] -= step_size
            if new_x[i] >= bounds[i, 0]:
                new_value = function(*new_x)
                if new_value > best_value:
                    best_x = new_x.copy()
                    best_value = new_value

        x = best_x.copy()

    return best_x, best_value


length = float(input("Enter the length of the search space: "))
width = float(input("Enter the width of the search space: "))
bounds = np.array([[-length, length], [-width, width]])
step_size = float(input("Enter the step size: "))
tekrar = int(input("Enter the number of tekrar: "))

best_solution, best_value = hill_climbing(ackley_function, bounds, step_size, tekrar)

print(f"Behtarin javab: {best_solution}")
print(f"Behtarin meghdar tabeh: {best_value}")
