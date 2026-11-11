
n = int(input("Enter number of facts: "))

facts = set()

for i in range(n):
    fact = input("Enter fact: ")
    facts.add(fact)

r = int(input("\nEnter number of rules: "))

rules = []

for i in range(r):
    print("\nRule", i + 1)

    conditions = input("Enter conditions (comma separated): ")
    conclusion = input("Enter conclusion: ")

    conditions = set(conditions.split(";"))

    rules.append((conditions, conclusion))

query = input("\nEnter query to prove: ")

def forward_chaining(facts, rules, query):

    while True:
        new_facts = set()

        for conditions, conclusion in rules:

            if conditions.issubset(facts):
                if conclusion not in facts:
                    new_facts.add(conclusion)

        if not new_facts:
            break

        facts.update(new_facts)

        print("New Facts:", new_facts)

        if query in facts:
            return True

    return query in facts


if forward_chaining(facts, rules, query):
    print("\nQuery Proved!")
else:
    print("\nQuery Cannot Be Proved!")
