import random

superheroes = ["Batman", "Superman", "Harry Potter", "Xena", "Thor"]
villains = ["Joker", "Darth Vader", "Voldemort", "Dracula", "Thanos"]

def calculate_attack(character):
    return 10 + random.randint(0, len(character))


hero = random.choice(superheroes)
villain = random.choice(villains)

hero_attack = calculate_attack(hero)
villain_attack = calculate_attack (villain)



print(f"{hero} fights {villain}.")
print(f"{hero} hits {hero_attack}.")
print(f"{villain} hits {villain_attack}.")

if hero_attack > villain_attack:
    print(f"{hero} saves the day!")
elif hero_attack < villain_attack:
    print(f"The Dark Side Wins!")
else:
    print("It's a draw!")
