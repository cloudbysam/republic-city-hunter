print("Welcome to the streets of Republic City, Equalist Vigilante..")

player = {
    'name' : input("\nenter player name: ").capitalize(),
    'health' : 30,
    'credits' : 10,
    'inventory' : ['laser pistol']
 }

def show_status():
     print("\n ---- CURRENT STATUS ----")
     print(f"Name: {player['name']}")
     print(f"Health: {player['health']}%")
     print(f"Credits: {player['credits']}")
     print(f"Inventory: {','.join(player['inventory'])}")
     print("-----------------------------")

def visit_underground_hideout():
    print("\n Slip into the Republic City underground tunnels... undetected.")
    remains = player["credits"]

    if remains < 15:
        raise ValueError("Not enough credits!")
    player["credits"] -= 15
    player["health"] += 40

    if player["health"] > 100:
        player["health"] = 100

    print(" Wounds patched up by Equalist medics! Cost: 15 Yuans.")