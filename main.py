print("Welcome to the streets of Republic City, Equalist Vigilante..")

player = {
    'name' : input("\nenter player name: ").capitalize(),
    'health' : 30,
    'yuans' : 10,
    'inventory' : ['laser pistol']
 }

def show_status():
     print("\n ---- CURRENT STATUS ----")
     print(f"Name: {player['name']}")
     print(f"Health: {player['health']}%")
     print(f"Yuans: {player['yuans']}")
     print(f"Inventory: {','.join(player['inventory'])}")
     print("-----------------------------")

def visit_underground_hideout():
    print("\n Slip into the Republic City underground tunnels... undetected.")
    remains = player["credits"]

    if remains < 15:
        raise ValueError("Not enough yuans!")
    player["yuans"] -= 15
    player["health"] += 40

    if player["health"] > 100:
        player["health"] = 100

    print(" Wounds patched up by Equalist medics! Cost: 15 Yuans.")

def hunt_down_benders():
    print("\n ^***^ Hunting down benders :) ^***^")
    if player["health"] < 20:
        raise ValueError("Too weak to hunt!! Visit the temple first..")
    player["health"] -= 20
    player["yuans"] += 40

    print("Shock gloves activated! You stripped a rogue bender of their elements. Amon is pleased.")

def visit_amon_portal():
    print("Welcome to Amon-Temple Hunter here is the gear. Choose your choice :). ")
    print("1. Smoke Bomb Pack - (30 Yuans) ")
    print("2. Sato-Corp Mech Blueprint - (50 Yuans) ")

    try:
        item_choice = int(input("\n What do you want to buy? (1-2): "))
        if item_choice == 1:
            if player["yuans"] < 30:
                raise ValueError(
                    "What you doing trying to get a weapon from my temple when you broke huhhhhh, get outtttt.")
            elif "Shield Booster" in player["inventory"]:
                print("You already have the weapon.")
            else:
                player["yuans"] -= 30
                player["inventory"].append("Smoke Bomb Pack")

                print("Yooo you just got yourself a useful tool to neutralize a bender!!")
                print("Now go through the dungeon before the cops come over.")

        elif item_choice == 2:
            if player["yuans"] < 50:
                raise ValueError
            elif "Neural Chip" in player["inventory"]:
                print("You already have the weapon.")

            else:
                player["yuans"] -= 50
                player["inventory"].append("Sato-Corp Mech Blueprint")

                print("Thanks for the purchase")

        else:
            print("The merchant glares at you. Invalid choice")

    except ValueError as err:
        print(f"Insufficient funds!!! {err}!!")