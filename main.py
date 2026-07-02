import random

print("Welcome to the streets of Republic City, Equalist Vigilante..")

def action_logger(func):
    def wrapper(*args, **kwargs):
        print(f"\n [EQUALIST NETWORK]: Initiating {func.__name__.replace('_', ' ').title()}...")
        result = func(*args, **kwargs)
        print(f"\n [EQUALIST NETWORK]: {func.__name__.replace('_', ' ').title()} completed.")
        return result
    return wrapper

player = {
    'name' : input("enter player name: ").capitalize(),
    'health' : 30,
    'yuans' : 10,
    'inventory' : ['electric shock gloves']
 }

def show_status():
     print("\n ---- CURRENT STATUS ----")
     print(f"Name: {player['name']}")
     print(f"Health: {player['health']}%")
     print(f"Yuans: {player['yuans']}")
     print(f"Inventory: {','.join(player['inventory'])}")
     print("-----------------------------")

@action_logger
def visit_underground_hideout():
    print("\n Slip into the Republic City underground tunnels... undetected.")
    remains = player["yuans"]

    if remains < 15:
        raise ValueError("Not enough yuans!")
    player["yuans"] -= 15
    player["health"] += 40

    if player["health"] > 100:
        player["health"] = 100

    print(" Wounds patched up by Equalist medics! Cost: 15 Yuans.")

@action_logger
def hunt_down_benders():
    print("\n >***> Hunting down benders :) >***>")
    if player["health"] < 20:
        raise ValueError("Too weak to hunt!! Visit the temple first..")

    roll = random.randint(1, 100)

    if roll <= 70:
        player["health"] -= 20
        player["yuans"] += 10

        print("Shock gloves activated! You stripped a rogue bender of their elements. Amon is pleased.")

    else:
            ambush_scenarios = [

                                {"bender_type": "earth_bender",
                                "lore_text": "Cabbage Merchant: 'MY CABBAGES!!! This place is worse than Omashu! You savages will pay for this!"},

                                {"bender_type": "fire_bender",
                                "lore_text": "Random citizen nearby: *Uncontrollable screaming while foaming at the mouth and fainting backwards*"},

                                {"bender_type": "fire_bender",
                                "lore_text": "Uncle Iroh: *I know you’re not supposed to cry over spilled tea, but it’s just so sad!a*"},

                                {"bender_type": "air_bender",
                                "lore_text": "Tenzin in the distance: Is anyone going to explain why my peaceful acolytes are street-brawling again?!"}

                                ]

            current_ambush = random.choice(ambush_scenarios)

            print(f"Huhhhhh you got ambushed by the {current_ambush['bender_type']}")
            print(f"{current_ambush['lore_text']}")

            if len(player["inventory"]) > 0:
                smashed_gear = random.choice(player["inventory"])
                player["inventory"].remove(smashed_gear)

                print(f"\nhaha your precious '{smashed_gear} weapon' has been destroyed by elemental bending lolzzzzz")
            print("\n ---- Republic City Holding Cell ----")
            print("Guard: Yooo my man the judge is planning on sending you to the Boiling Rock prison!\n "
                    "But i can help you break out if you have 10 yuan to spare for my pregnant wife. ")

            if player["yuans"] >=10:
                player["yuans"] -= 10
                print("\nGuard: He was a shadow in the night no one could explain how he escaped the cell.")

            else:
                print("\nGuard: Well my friend get ready to be sent to the Boiling Rock prison where your eyes will be boiled out!")
                exit()

@action_logger
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

while True:
    show_status() # not yet defined
    print(f"\n what do you want to do? {player["name"]}")
    print("1. visit_underground_hideout (Heal). ")
    print("2. Hunt down benders (Earn yuans). ")
    print("3. visit_amon_portal (illegal shop). ")
    print("4. If you are scared to challenge the Avatar....QUIT.")

    try:
        choice = int(input("\n Enter Choice (1-4): "))

        if choice == 1:
            visit_underground_hideout()

        elif choice == 2:
            hunt_down_benders()

        elif choice == 3:
            visit_amon_portal()

        elif choice == 4:
            print("\n You fled the city on a Sato-Corp airship. The Avatar wins this round...")
            break
        else:
            print("Invalid sector code: Pick 1,2,3 or 4.")

    except ValueError as error:
        if "invalid literal" in str(error):
            print("system error: You must enter a digit (number) !!!")
        else:
            print(f"system error: {error}")
