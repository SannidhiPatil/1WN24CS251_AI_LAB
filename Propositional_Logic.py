
from itertools import product

def implies(p, q):
    return not p or q


def KB(P, Q, R):
    return (implies(Q, P) and
            implies(P, not Q) and
            (Q or R))


def query(P, Q, R):
    return R


symbols = ['P', 'Q', 'R']

print("\n      TRUTH TABLE ENUMERATION")
print("=" * 72)

print("No. | P | Q | R | Q->P | P->~Q | Q|R | KB | Query")
print("-" * 72)

entails = True
row = 1
models = 0

for values in product([True, False], repeat=3):

    P, Q, R = values

    a = implies(Q, P)
    b = implies(P, not Q)
    c = Q or R

    kb = KB(P, Q, R)
    alpha = query(P, Q, R)

    if kb:
        models += 1

    if kb and not alpha:
        entails = False

    result = ['T' if x else 'F' for x in
              [P, Q, R, a, b, c, kb, alpha]]

    print(f"{row:^4} | {' | '.join(result)}")

    row += 1

print("=" * 72)

print("\nRESULT SUMMARY")
print("-" * 35)
print("Total models generated :", row - 1)
print("Models satisfying KB   :", models)

if entails:
    print("Query                  : R")
    print("Conclusion             : KB entails R")
else:
    print("Query                  : R")
    print("Conclusion             : KB does not entail R")

print("-" * 35)
