players = ['mini','enzo','cajsa','loke']

print("This is the four available characters:")
for player in players:
    print(player.title())

weapon_type = ["sword", "maze", "staf", "wand"]
print("sword" in weapon_type)
print("magicwand" in weapon_type)

banned_players = ["joavi", "freddie", "yoshi"]
player = "maja-lisa"
if player not in banned_players:
    print(f"{player.title()}, stop talking to the banned players!")

if "sword" in weapon_type:
    print("You picked Sword")
if "wand" in weapon_type:
    print("You picked wand")

print("\n You have now picked you're weapon!!")





