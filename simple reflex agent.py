
print("       VACUUM CLEANER AGENT")

location = input("Enter vacuum location (A/B): ")
room_A = input("Is Room A dirty? (yes/no): ")
room_B = input("Is Room B dirty? (yes/no): ")

print("\nInitial State")
print("Vacuum Location :", location)
print("Room A :", room_A)
print("Room B :", room_B)

print("        VACUUM CLEANING")

if location == "A":

    if room_A == "yes":
        print("Room A is dirty.")
        print("Vacuum is cleaning Room A...")
        room_A = "no"
        print("Room A is now clean.")

    else:
        print("Room A is already clean.")

    print("Moving vacuum from Room A to Room B...")
    location = "B"

    if room_B == "yes":
        print("Room B is dirty.")
        print("Vacuum is cleaning Room B...")
        room_B = "no"
        print("Room B is now clean.")
    else:
        print("Room B is already clean.")

elif location == "B":

    if room_B == "yes":
        print("Room B is dirty.")
        print("Vacuum is cleaning Room B...")
        room_B = "no"
        print("Room B is now clean.")

    else:
        print("Room B is already clean.")

    print("Moving vacuum from Room B to Room A...")
    location = "A"

    if room_A == "yes":
        print("Room A is dirty.")
        print("Vacuum is cleaning Room A...")
        room_A = "no"
        print("Room A is now clean.")
    else:
        print("Room A is already clean.")

else:
    print("Invalid location!")

print("          FINAL STATE")

print("Vacuum Location :", location)
print("Room A :", room_A)
print("Room B :", room_B)

if room_A == "no" and room_B == "no":
    print("\nSUCCESS: Both rooms are clean!")
else:
    print("\nSome room is still dirty.")
