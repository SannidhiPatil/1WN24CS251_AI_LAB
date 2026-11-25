
def eliminate_implication(expr):
    expr = expr.replace("->", "|")
    return expr


def move_negation(expr):
    expr = expr.replace("~~", "")

    expr = expr.replace("~(A & B)", "(~A | ~B)")
    expr = expr.replace("~(A | B)", "(~A & ~B)")

    return expr


def distribute_or(expr):
    expr = expr.replace(
        "A | (B & C)",
        "(A | B) & (A | C)"
    )

    return expr


def fol_to_cnf():
    print("FOL to CNF Conversion")
    print("Use symbols: ~ for NOT, & for AND, | for OR")
    print("Use -> for implication")

    expr = input("Enter logical expression: ")

    print("\nOriginal Expression:", expr)

    expr = eliminate_implication(expr)
    print("After implication elimination:", expr)

    expr = move_negation(expr)
    print("After moving negation:", expr)

    expr = distribute_or(expr)
    print("After distribution:", expr)

    print("\nCNF Expression:", expr)


fol_to_cnf()
