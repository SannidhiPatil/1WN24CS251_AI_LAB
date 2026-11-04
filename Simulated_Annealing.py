import random
import math

def objective(x):
    return x ** 2

def simulated_annealing():
    current = float(input("Enter initial solution: "))
    T = float(input("Enter initial temperature: "))
    cooling_rate = float(input("Enter cooling rate (0 to 1): "))
    iterations = int(input("Enter number of iterations: "))

    best = current

    for i in range(iterations):
        neighbour = current + random.uniform(-1, 1)

        delta = objective(neighbour) - objective(current)

        if delta < 0:
            current = neighbour
        else:
            probability = math.exp(-delta / T)

            if random.random() < probability:
                current = neighbour

        if objective(current) < objective(best):
            best = current

        T = T * cooling_rate

        if T < 0.001:
            break

    print("\nSIMULATED ANNEALING RESULT")
    print("--------------------------")
    print("Best Solution:", round(best, 4))
    print("Minimum Cost:", round(objective(best), 4))


simulated_annealing()
