from ollama import chat
import time
import random

all_init_choices = {
    "Weapons": {
        "Basic Axe": {"dmg": 4, "durability": 10,}, 
        "Basic Sword": {"dmg": 6, "durability": 6}, 
        "Basic Pickaxe": {"dmg": 2, "durability": 15}
    },
    "Artifacts": {
        "Shoes of Pheidippides": {"Health": -2, "Stamina": 4, "Defense": 0}, 
        "Shield of Lancelot": {"Health": 0, "Stamina": -3, "Defense": 3}, 
        "Subway Sandwich": {"Health": 5, "Stamina": -3, "Defense": 1}
    },
    "Maps": {
        "Dungeon 1 (Easy)",
        "Dungeon 2 (Medium)",
        "Dungeon 3 (Hard)"
    }
}

class Chatbot:
    def __init__(self, role: str):
        self.message_history = [{'role': 'assistant', 'content': f"{role}"}]

    def talk(self, msg: str, inventory: dict) -> str:
        self.message_history.append({"role": "user", "content": msg, "inventory": inventory})
        start = time.time()
        response = chat(
            model="gemma3:1b",
            messages=self.message_history
        )
        duration = time.time() - start
        print(f"{duration:.2f}s to reply")
        assistant_reply = response.message.content
        self.message_history.append({"role": "assistant", "content": assistant_reply})
        return assistant_reply

def get_random_kit(difficulty: str) -> dict:
    if difficulty == "easy":
        init_choices_dupe = all_init_choices.copy()
        init_choices_dupe["Weapons"].pop("Basic Pickaxe")
        weapon = random.choice(list(init_choices_dupe["Weapons"].items()))
        artifact = random.choice(list(init_choices_dupe["Artifacts"].items()))
        return {"Weapons": {weapon[0]: weapon[1]}, "Artifacts": {artifact[0]: artifact[1]}, "Maps": ["Dungeon 1 (Easy)"]}
    
    elif difficulty == "medium":
        weapon = random.choice(list(all_init_choices["Weapons"].items()))
        artifact = random.choice(list(all_init_choices["Artifacts"].items()))
        map = random.choice(list(all_init_choices["Maps"]))
        return {"Weapons": {weapon[0]: weapon[1]}, "Artifacts": {artifact[0]: artifact[1]}, "Maps": [map]}
    
    elif difficulty == "hard":
        return {"Weapons": {"Basic Pickaxe": all_init_choices["Weapons"]["Basic Pickaxe"]}, "Artifacts": {}, "Maps": ["Dungeon 3 (Hard)"]}
    
def get_user_input(expected: list, prompt: str, progress_on_empty: bool = False) -> str:
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in expected:
            return user_input
        elif progress_on_empty:
            return ""
        else:
            list_items = "`, `".join(expected)
            print(f"Invalid input. Please enter one of the following: '{list_items}'.")

def print_inventory(inventory: dict) -> str:
    num_times = 25
    print("\nInventory")
    print("="*num_times)

    for cat, content in inventory.items():
        print("-"*num_times)
        print(f"{cat}")
        if isinstance(content, dict):
            for item_name, attributes in content.items():
                print(f"• {item_name}:")
                for attr, val in attributes.items():
                    if attr == "dmg":
                        attr = "Damage"
                    print(f"  - {attr.title()}: {val}")
        elif isinstance(content, list):
            for item in content:
                print(f"• {item}")

    print("-"*num_times)
    print("="*num_times, "\n")

def print_status(status: dict) -> str:
    num_times = 25
    print("\nStatus")
    print("="*num_times)

    for cat, content in status.items():
        print(f"• {cat}: {content}")
    
    print("="*num_times)

def get_random_event_prob(difficulty: str, previous_outcome: float) -> tuple[bool, float]:
    dif_probs = {
        "easy": 0.25,
        "medium": 0.45,
        "hard": 0.80
    }
    current_prob = dif_probs[difficulty] + previous_outcome
    current_prob = min(current_prob, 1.0)

    triggered = random.random() < current_prob
    if triggered:
        return True, 0.0
    else: 
        return False, current_prob
    
def equip_item(d: dict, artifact_choice: bool =False) -> str:
    valid_items = {name.lower(): name for name in d.keys()}
    while True:
        display_list = []
        for name, stats in d.items():
            display_list.append(f"{name} (Stats: {stats})")
        if artifact_choice == True:
            display_list.append("None")
        options = ", ".join(display_list)            
        print(f"\nAvailable items: {options}")
        user_input = input("Please type the name of the weapon you would like to equip: ").strip().lower()
        if user_input == "none":
            print("Very well, no artifact has been applied.")
            return None
        
        if user_input in valid_items:
            equipped_item_name = valid_items[user_input]

            print(f"You have equipped: {equipped_item_name}")
            return equipped_item_name
        else: 
            print("\nThat is not a valid ")

def get_effective_stats(player_state: dict, equipped: dict, all_items: dict) -> dict:
    current_stats = player_state.copy()
    for slot, item_name in equipped.items():
        if not item_name: continue
        item_stats = None
        if slot == "artifact":
            item_stats = all_items["Artifacts"].get(item_name)
        
        if item_stats:
            for stat, val in item_stats.items():
                current_stats[stat] += int(val)
    return current_stats

def process_purchase(user_input: str, inventory: dict, player_state: dict) -> tuple[dict, str]:
    parts = [part.strip() for part in user_input.split(',')]
    name, type, cost_str = parts
    cost = int(cost_str)
    player_state["Gold Pieces"] -= cost    

    if type == "Weapons":
        new_stats = {
            "dmg": random.randint(1,12),
            "durability": random.randint(5,30)
        }
    elif type == "Artifacts":
        new_stats = {
            "Health": random.randint(-5, 10),
            "Stamina": random.randint(-5, 10),
            "Defense": random.randint(-2, 5)
        }
    
    inventory[type][name] = new_stats
    return f"\nYou bought {name} for {cost} Gold! These are the stats for your new item: {new_stats}, and you have: {player_state['Gold Pieces']} remaining gold.\n"




def main():
    entry_line = get_user_input(["q"], "\nYou are an explorer who is destined to become the most legendary explorer in the world.\nYou will plunge into the depths of the most dangerous dungeons, and conquer the fiercest of foes.\nDo you wish to embark on this journey? Press <Enter> to begin, or type `q` to quit.\n\nYou> ", progress_on_empty=True)

    # debug
    # entry_line = ""

    if entry_line == "":
        talking = True
    else: 
        talking = False
    print("\n" + "="*50 + "\n")

    num_spaces = 4

    print(f"Welcome, brave explorer! Before you can begin your adventure, there is some ancient wisdom that I must impart with you.\nIn this adventure, you have access to an inventory that houses your weapons, artifacts, and maps to terrifying dungeons!\nThese items have base stats that you can use in the dungeons:\n{" "*num_spaces}• Damage: how much health you take from an enemy,\n{" "*num_spaces}• Durability: how many times you can hit an enemy (some enemies take more durability than others!).\nThe types of items that your initially receive are based on the difficulty that you choose, so choose wisely!\n\nIn addition to your inventory, you also have a status that tells you how many Gold Pieces you have,\nand your current Health, Stamina, and Defense. Like the items in your inventory, these are all crucial to your time in the dungeon.\nEach stat corresponds to a specific function:\n{" "*num_spaces}• Health: your remaining hit points before you die,\n{" "*num_spaces}• Stamina: used to determine if you can attack or if you must rest,\n{" "*num_spaces}• Defense: multiplier used to dampen how much damage you take.\nThese stats can be affected by equipping artifacts; just note that some items are better than others!")

    print("\n" + "="*50 + "\n")
    print("Please choose your difficulty level. This will determine the challenges you face and the rewards you earn.")
    difficulty = get_user_input(["easy", "medium", "hard"], "Choose your difficulty (`easy`, `medium`, `hard`)\n\nYou> ")
    inventory = get_random_kit(difficulty)

    # Debug
    # difficulty = 'medium'
    # inventory = get_random_kit(difficulty)
    print(inventory)

    player_state = {"Gold Pieces": 20, "Health": 10, "Stamina": 10, "Defense": 10}
    player_equipped = {"weapon": None, "artifact": None}

    previous_outcome = 0
    checked_inventory = False

    while talking:
        if player_state["Health"] <= 0:
            print("You died! Better luck next time, explorer!")
            break
        num_dungeons = len(inventory["Maps"])
        print("\n" + "="*50 + "\n")
        line = get_user_input(['q','inv','status','market','equip','dungeon'], f"Type `q` to quit, `inv` to view your inventory, `status` to view your status, `market` to visit the market, `equip` to use artifacts or change weapons, or `dungeon` ({num_dungeons} available) to travel to a dungeon.\n\nYou> ")
        match line:
            case 'q':
                print("Farewell, brave explorer!")
                talking = False
            case 'inv':
                checked_inventory = True
                print_inventory(inventory)
            case 'status':
                print_status(player_state)
            case 'market':
                if not checked_inventory: 
                    print("This is your inventory:")
                    print_inventory(inventory)
                merchant_bot = Chatbot(f"You are a merchant that is tasked with selling weapons and artifacts. You should generate new, unique names for weapons and artifacts that have prices below 20 gold. Keep all of the item prices below 20. You can say that these items are extremely rare or that they come from a distant land.")
                print("You may access your inventory at any time by typing `inv`. If you would like to leave, type `q`. If you purchase an item, type `p`: this will prompt you to enter what item you bought, what type it is, and for how much gold. Otherwise, type anything else to begin conversing with the merchant.\n")
                while True:
                    inner_line = input("You> ")
                    if inner_line == "inv":
                        print_inventory(inventory)
                    elif inner_line == "q":
                        break
                    elif inner_line == 'p':
                        purchased_item = input("Please type what the name of the item was. (e.g., `Legendary Broadsword, Weapons, 15`, or `Lebron's Buckethat, Artifacts, 10`)\n\nYou> ")
                        output = process_purchase(purchased_item, inventory, player_state)
                        print(output)
                    else:
                        start = time.time()
                        print(merchant_bot.talk(inner_line, inventory))
                        print(f"Duration: {time.time() - start:.2f}s")
            case 'equip':
                # I would add a conditional here to guard against maxing out stats, but this is already way too complicated.
                total_weapons, total_artifacts = len(inventory["Weapons"]), len(inventory["Artifacts"])
                to_equip = get_user_input(["a", "w", "b"], f"What item would you like to equip? You have {total_weapons} weapon(s), and {total_artifacts} artifact(s). Type `w`, `a`, or `b` to enter a dialogue (you can press <Enter> to exit this menu).\n\nYou> ", progress_on_empty=True)
                e_weapon, e_artifact = None, None
                if to_equip == "a":
                    e_artifact = equip_item(inventory["Artifacts"], artifact_choice=True)
                elif to_equip == "w":
                    e_weapon = equip_item(inventory["Weapons"])
                elif to_equip == "b":
                    e_artifact = equip_item(inventory["Artifacts"], artifact_choice=True)
                    e_weapon = equip_item(inventory["Weapons"])
                player_equipped = {"weapon": e_weapon, "artifact": e_artifact}
                player_state = get_effective_stats(player_state, player_equipped, inventory)
            case 'dungeon':
                trigger_event, previous_outcome = get_random_event_prob(difficulty, previous_outcome)
                trigger_event = True
                if trigger_event:
                    unexpected_encounter_bot = Chatbot(f"You are a bridge troll that is keen on making a twisted riddle for the user to answer. You will determine if the user solves the riddle.")
                    print("Oh no! You have stumbled across a bridge troll on your way to the dungeon! Type `q` to quit (and continue onto the dungeon), or press <Enter> to begin the battle of wits!\n")
                    while True:
                        inner_line = input("You> ")
                        if inner_line == "q":
                            break
                        else:
                            start = time.time()
                            print(unexpected_encounter_bot.talk(inner_line, inventory))
                            print(f"Duration: {time.time() - start:.2f}s")

                dungeon_bot = Chatbot(f"You tell the story of a dungeon that is capable of pitting monsters against the user. You should set up battles so the user is challenged based on the difficulty of the dungeon. This has difficulty: `{inventory['Maps'][0]}`. The user should take damage, and you should report how much damage they took like `The player takes 5 damage!`. The user's current stats are: {player_state}`.")
                print("After a long journey, you have finally made it to the dungeon! If you take damage at any point, you can type `d` to adjust how much damage you have taken. Type `q` to quit, or type a message to tempt the fate of the dungeon if you so dare!\n")
                while True:
                    inner_line = input("You> ")
                    if inner_line == "q":
                        break
                    if inner_line == 'd':
                        damage = input("Please enter how much damage you have taken. (e.g., '5')\n\nYou> ")
                        player_state["Health"] -= int(damage)
                        if player_state["Health"] <= 0:
                            return "Oh no, you died! Well, better luck next time..."
                        else: 
                            print(f"\nThis is your current health: {player_state["Health"]}. Be more careful next time!\n")
                    else:
                        start = time.time()
                        print(dungeon_bot.talk(inner_line, inventory))
                        print(f"Duration: {time.time() - start:.2f}s")



if __name__ == '__main__':
    main()