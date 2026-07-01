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

show_status()