
import random



def calculate_cost(state):
    n = len(state)
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts



def display_board(state):
    n = len(state)

    for row in range(n):
        print(" ".join(
            "Q" if state[col] == row else "."
            for col in range(n)
        ))



def get_coordinates(state):
    return [(col, state[col]) for col in range(len(state))]



def get_neighbors(state):
    n = len(state)
    neighbors = []

    for i in range(n):
        for j in range(i + 1, n):
            new_state = state.copy()
            new_state[i], new_state[j] = (
                new_state[j], new_state[i]
            )

            neighbors.append(
                (new_state, (i, j), calculate_cost(new_state))
            )

    return neighbors



def hill_climbing(n):
    if n in (2, 3):
        print("No solution exists for N =", n)
        return

    total_steps = 0

    while True:
        current = list(range(n))
        random.shuffle(current)

        path = [current.copy()]
        swaps = []

        while True:
            current_cost = calculate_cost(current)

            if current_cost == 0:
                print("\nINITIAL STATE:")
                display_board(path[0])
                print("Coordinates:", get_coordinates(path[0]))

                print("\nSOLUTION PATH:")

                for step, state in enumerate(path):
                    print(f"\nStep {step}")
                    print("Coordinates:", get_coordinates(state))
                    display_board(state)
                    print("Cost:", calculate_cost(state))

                    if step < len(swaps):
                        print("Swap:", swaps[step])

                print("\nFINAL SOLUTION:")
                display_board(current)
                print("Final coordinates:", get_coordinates(current))
                print("Final cost:", calculate_cost(current))
                print("Total moves:", len(swaps))
                print("Total steps across attempts:", total_steps)
                return

            neighbors = get_neighbors(current)

            best_state, best_pair, best_cost = min(
                neighbors, key=lambda x: (x[2], x[1])
            )

            if best_cost >= current_cost:
                total_steps += len(swaps)
                break

            current = best_state
            swaps.append(best_pair)
            path.append(current.copy())




n = int(input("Enter the value of N: "))

if n < 1:
    print("N must be positive.")
else:
    hill_climbing(n)
