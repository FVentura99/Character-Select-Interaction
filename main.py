import random

# The avaliable fighters for character select
fighters = [
    "Ryu",
    "Ken",
    "Chun Li"
]

# Character-specific interactions.
interactions = {
    ("Ryu", "Ken"): [
    [
        "Ryu: 'You are early'",
        "Ken: 'Well you know me, lets do this'"
    ],
    [
        "Ryu: 'Let's go Ken!'",
        "Ken: 'I am ready Ryu!'"

    ]
    ],
    ("Ryu", "Chun Li"): [
    [
        "Ryu: 'Chun Li, I am ready!'",
        "Chun Li: 'Do not hold back Ryu!'"
    ]
    ]

}

#If fighters dont have special interactions defined between them.
generic_interactions = [
    "{f1}: 'Let’s see what you’ve got.'",
    "{f2}: 'Bring it on!'",
    "{f1}: 'This ends now.'",
    "{f2}: 'Only one of us walks away.'",
    "{f1}: 'Bring it on, chump.'",
    "{f2}: 'Let me speak in a language you can understand.'",
    "{f1}: 'Action speaks louder than words.'",
    "{f2}: 'Overconfidence is a flimsy shield'"
]

#The user input which fighter they would like to select for player 1 and player 2.
def select_fighter(prompt, taken=None):
    print(prompt)
    available = [f for f in fighters if f != taken]
    #Enumerate the fighter to show the user needs to pick the number and not write the name.
    for idx, name in enumerate(available, 1):
        print(f"{idx}. {name}")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            # Value must be between 1 and the number of fighters in fighters variable.
            if 1 <= choice <= len(available):
                return available[choice - 1]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a valid number.")

# Getting the interactions from character select
def get_interaction(f1, f2):
    pair1 = (f1, f2)
    pair2 = (f2, f1)
    #Check to see if selection is in the special ineraction.
    if pair1 in interactions:
        return random.choice(interactions[pair1])
    elif pair2 in interactions:
        # Swap names back for display if using reverse.
        reversed_lines = random.choice(interactions[pair2])
        return [line.replace(f2, "__TEMP__").replace(f1, f2).replace("__TEMP__", f1)
                for line in reversed_lines]
    else:
        # Return two random generic lines from generic interaction variable
        return [random.choice(generic_interactions).format(f1=f1, f2=f2),
                random.choice(generic_interactions).format(f1=f2, f2=f1)]

# What the user will see in the front-end
print("=== Please select a character ===")
fighter1 = select_fighter("Pick your first fighter:")
fighter2 = select_fighter("Pick your second fighter", taken=fighter1)

# The interaction when the user selects the two fighters
print(f"\n=== {fighter1} vs {fighter2} ===")
dialogue = get_interaction(fighter1, fighter2)
for line in dialogue:
    print(line)