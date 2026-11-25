
def alpha_beta(node, depth, alpha, beta, values, maximizing):

    if depth == 0:
        print("Visited node:", values[node])
        return values[node]

    if maximizing:
        best = float('-inf')

        for i in range(2):
            val = alpha_beta(node * 2 + i, depth - 1,
                             alpha, beta, values, False)

            best = max(best, val)
            alpha = max(alpha, best)

            if alpha >= beta:
                print("Branch pruned at MAX")
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alpha_beta(node * 2 + i, depth - 1,
                             alpha, beta, values, True)

            best = min(best, val)
            beta = min(beta, best)

            if alpha >= beta:
                print("Branch pruned at MIN")
                break

        return best


n = int(input("Enter number of leaf nodes: "))

values = []
print("Enter leaf node values:")

for i in range(n):
    values.append(int(input()))

depth = 0
temp = n

while temp > 1:
    temp //= 2
    depth += 1

if n < 2 or n != 2 ** depth:
    print("Enter a power of 2")
else:
    print("\n--- Alpha Beta Pruning ---")

    result = alpha_beta(0, depth, float('-inf'),
                        float('inf'), values, True)

    print("\nOptimal value:", result)
