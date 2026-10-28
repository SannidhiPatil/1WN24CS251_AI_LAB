
import heapq

initial = (2, 8, 3,
           1, 6, 4,
           7, '_', 5)

goal = (1, 2, 3,
        8, '_', 4,
        7, 6, 5)


def heuristic(state):
    return sum(
        1 for i in range(9)
        if state[i] != '_' and state[i] != goal[i]
    )


def display(state):
    for i in range(0, 9, 3):
        print(' '.join(str(x) for x in state[i:i + 3]))


def get_neighbors(state):
    neighbors = []
    blank = state.index('_')
    row, col = divmod(blank, 3)

    moves = [(-1, 0, "Up"),
             (1, 0, "Down"),
             (0, -1, "Left"),
             (0, 1, "Right")]

    for dr, dc, move in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_blank = r * 3 + c
            new_state = list(state)

            new_state[blank], new_state[new_blank] = (
                new_state[new_blank], new_state[blank]
            )

            neighbors.append((tuple(new_state), move))

    return neighbors


def astar(initial, goal):
    pq = []
    counter = 0

    heapq.heappush(
        pq, (heuristic(initial), counter, 0, initial)
    )

    cost = {initial: 0}
    parent = {initial: (None, None)}

    while pq:
        f, _, g, current = heapq.heappop(pq)

        if g != cost[current]:
            continue

        if current == goal:
            path = []
            state = current

            while state is not None:
                path.append(state)
                state = parent[state][0]

            path.reverse()

            print("INITIAL STATE:")
            display(initial)

            print("\nFINAL STATE:")
            display(goal)

            print("\nSOLUTION STEPS:")

            for step, state in enumerate(path):
                g_value = step
                h_value = heuristic(state)
                f_value = g_value + h_value

                print(f"\nStep {step}:")
                display(state)
                print(f"g(n) = {g_value}")
                print(f"h(n) = {h_value}")
                print(f"f(n) = {g_value} + {h_value} = {f_value}")

            print("\nTOTAL NUMBER OF MOVES:", len(path) - 1)
            return

        for neighbor, move in get_neighbors(current):
            new_g = g + 1

            if neighbor not in cost or new_g < cost[neighbor]:
                cost[neighbor] = new_g
                parent[neighbor] = (current, move)

                counter += 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    pq, (new_f, counter, new_g, neighbor)
                )

    print("No solution exists.")


astar(initial, goal)
