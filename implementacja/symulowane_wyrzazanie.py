"""
The Simulated Annealing algorithm in the provided code follows these steps:

Initialization: The algorithm starts at a given point (x, y), calculates the score at this point using function f(x, y), and initializes the path with the start point.

Iteration: The algorithm enters a loop that runs for a maximum number of iterations. In each iteration:

Cooling: The temperature T is reduced by a factor of 0.99. This simulates the "cooling" process in annealing.

Neighbor Selection: A new neighbor point is generated by adding a random value between -1 and 1 to x and y. The score at this neighbor point is calculated.

Acceptance Criteria: If the score at the neighbor point is less than the current best score, the algorithm moves to the neighbor point. If the score is not less, the algorithm may still move to the neighbor point with a probability that depends on the difference in scores and the current temperature. This allows the algorithm to potentially escape local minima.

Update: If the algorithm moves to the neighbor point, it updates the best score and the current point (x, y), and adds the neighbor point to the path.

Result: After the loop finishes, the algorithm returns the final point (x, y), the best score, and the path it took to get there.
"""

import numpy as np
import matplotlib.pyplot as plt
import math


def f(x, y):
    return x**2 + y**2


def simulated_annealing(start, max_iter, T):
    x, y = start
    best_score = f(x, y)
    path = [start]

    for i in range(max_iter):
        T = T * 0.99  # cooling
        dx, dy = np.random.uniform(-1, 1, 2)
        neighbor = (x + dx, y + dy)
        score = f(*neighbor)
        if score < best_score or np.random.rand() < math.exp((best_score - score) / T):
            best_score = score
            x, y = neighbor
            path.append(neighbor)

    return x, y, best_score, path


start = (10, 10)
max_iter = 1000
T = 10

x, y, best_score, path = simulated_annealing(start, max_iter, T)

# Visualization
x_values = np.linspace(-10, 10, 100)
y_values = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_values, y_values)
Z = f(X, Y)

plt.figure(figsize=(10, 8))
plt.contourf(X, Y, Z, 50, cmap="viridis")
plt.plot(*start, "ro")  # start point
plt.plot(x, y, "bo")  # end point
plt.plot(*zip(*path), "w-")  # path
plt.colorbar()
plt.show()
