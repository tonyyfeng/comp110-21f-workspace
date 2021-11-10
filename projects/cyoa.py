"""This program is an adventure game that allows a player to slay a dragon to get its loot or steal from the dragon to get its loot."""
__author__ = "730410711"

import random
PERSON = "\U0001F600"
DRAGON = "\U0001F409"


def main() -> None:
    """This is the main function that starts the entire adventure."""
    global points
    global player
    greet()
    i: int = 0
    while i < 1:
        print(f"Now, {player}, you must decide how you will get the loot from the dragon. Will you, \n1. Attempt to slay the dragon?\n2. Attempt to sneak in and loot the gold without alerting the dragon?\n3. Run away with what you have now.")
        choice: str = input("Put only the number of your choice here: ")
        if choice == "1":
            slay_dragon()
        else:
            if choice == "2":
                points = steal(points)
            else:
                if choice == "3":
                    print(f"Congratulations {player}, you have earned {points} points!\nWe hope to see you again, goodbye!")
                    i = i + 1
                else:
                    print("Please choose a valid answer, 1, 2, or 3")


def slay_dragon() -> None:
    """This fucntion lets the player fight a dragon."""
    global points
    global player
    attack: int = 10
    health: float = 100
    dragon_health: float = 200
    dragon_damage: float = 15
    death: int = 0
    i: int = 0
    attack_type: str = ""
    did_they_attack: int = 0
    invulnerability: int = 0
    will_it_succeed: int = 0
    dragon_attack_type: int = 0
    while i == 0:
        weapon: str = input(f"Choose your weapon, {player}! \n1. A sword and shield\n2. Twin daggers\n3. A bow and arrow\nPut the number of your choice here: ")
        if weapon == "1":
            print("You have chosen the sword and shield! Fine choice!")
            attack = attack + 10
            health = health + 40
            i = i + 1
        else:
            if weapon == "2":
                print("Ah, the twin daggers, quite risky but with high reward for fighting so up close!")
                attack = attack + 20
                i = i + 1
            else:
                if weapon == "3":
                    print("A bow and arrow, handy for taking out targets at a distance and picking out weak points!")
                    attack = attack + 15
                    i = i + 1
                else:
                    print("Uh oh, you didn't choose a weapon, try inputing 1, 2, or 3 again to input a weapon!")
    points = points + 5
    print(f"Congratulations on choosing a weapon! You now have {points} points!")
    print("Now that you have obtained your weapon, you approach the dragon's lair, yelling obscenities at the dragon to lure it out.\n It worked! The dragon is now approaching you and initiates the battle!")
    while dragon_health > 0 and health > 0:
        print(f"{player}'s Health: {health}  {PERSON} ... {DRAGON}  {dragon_health} :Bob the Dragon's Health")
        did_they_attack = 0
        if weapon == "1":
            print("Choose your attack!")
            while did_they_attack == 0:
                attack_type = input("1. Slap the dragon with your sword\n2. Block all damage using your fat shield\n")
                if attack_type == "1":
                    print(f"The dragon took {attack} damage!")
                    dragon_health = dragon_health - attack
                    did_they_attack = 1
                else:
                    if attack_type == "2":
                        print("You decided to block all damage!")
                        invulnerability = 1
                        did_they_attack = 1
                    else:
                        print("You did not attack, please select a valid answer: 1, or 2")
        if weapon == "2":
            print("Choose your attack!")
            while did_they_attack == 0:
                attack_type = input("1. Stab the dragon\n2. Go super close and go all out, disregarding your safety\n")
                if attack_type == "1":
                    print(f"The dragon took {attack} damage!")
                    dragon_health = dragon_health - attack
                    did_they_attack = 1
                else:
                    if attack_type == "2":
                        print("You go beserk, attacking the dragon without regard for your safety!")
                        dragon_health = dragon_health - (attack * 1.5)
                        will_it_succeed = random.randint(1, 2)
                        if will_it_succeed == 1:
                            print(f"Even though you attacked recklessly, you didn't sustain damage!\nThe dragon took {attack * 1.5} damage!")
                            """This is supposed to be a successful attack"""
                        else:
                            health = health - dragon_damage
                            print(f"You attacked recklessly, but took some hits while doing so. \nThe dragon took {attack * 1.5} damage and you took {dragon_damage} damage.")
                        did_they_attack = 1
                    else:
                        print("You did not attack, please select a valid answer: 1, or 2")
        if weapon == "3":
            print("Choose your attack!")
            while did_they_attack == 0:
                attack_type = input("1. Shoot the dragon\n2. Aim to disable and lower its attack (1/3 chance)\n")
                if attack_type == "1":
                    print(f"The dragon took {attack} damage!")
                    dragon_health = dragon_health - attack
                    did_they_attack = 1
                else:
                    if attack_type == "2":
                        print("You aim carefully for critical areas.")
                        will_it_succeed = random.randint(1, 3)
                        if will_it_succeed == 1:
                            print("You successfully disabled the dragon!, it is now dealing half the damage it was before!")
                            dragon_damage = (dragon_damage / 2)
                        else:
                            print("Your shot completely missed lol.")
                        did_they_attack = 1
                    else:
                        print("You did not attack, please select a valid answer: 1, or 2")
        if dragon_health > 0:    
            if dragon_health < 180:    
                dragon_attack_type = random.randint(1, 5)
                if dragon_attack_type == 1:
                    print("The dragon tried to breathe fire on you, but completely missed because you dodged behind a rock just in time!")
                if dragon_attack_type == 2:
                    dragon_health = dragon_health + 20
                    print("The dragon licks its wounds, healing itself for 20 health!")
                if dragon_attack_type > 2:
                    if invulnerability == 1:
                        print("You blocked the dragon's attack!")
                    else:
                        print(f"The dragon successfully hits you, dealing {dragon_damage} damage")
                        health = health - dragon_damage
            else:
                dragon_attack_type = random.randint(1, 5)
                if dragon_attack_type == 1:
                    print("The dragon tried to breathe fire on you, but completely missed because you dodged behind a rock just in time!")
                if dragon_attack_type > 1:
                    if invulnerability == 1:
                        print("You blocked the dragon's attack!")
                    else:
                        print(f"The dragon successfully hits you, dealing {dragon_damage} damage")
                        health = health - dragon_damage
        invulnerability = 0
        if dragon_health <= 0:
            death = 1
        if health <= 0:
            death = 2
    if death == 1:
        print(f"The dragon, heavily wounded, flees from you as fast as possible. While you haven't killed it, you are now free to loot everything in its lair!\nYou take all you can hold, gaining {health + 200} points worth of stuff!")
        points = points + int(health) + 200
        print("However, another dragon soon takes over the lair again and the King, seeing your success, asks you to get this dragon's gold too.")
    if death == 2:
        points = points - 50
        print(f"You have been greviously wounded. You retreat, and it costs 50 points to heal. But you quickly heal, and soon the King asks you to try again.\nYou now have {points} points.")


def steal(points: int) -> int:
    """This function allows the player to try and steal loot from the dragon."""
    global player
    initial: int = points
    decision: str = ""
    health: int = 100
    looper: int = 0
    chance: int = 0
    luck_for_loot: int = 4
    print(f"You decide that instead of fighting, you will steal gold right from the careful watch of Bob the Dragon.\nBe careful, some decisions you make will matter and you only have {health} health!")
    while looper == 0:
        decision = input(f"Now, {player} will you: \n1. Enter the front door of the lair\nor\n2. Sneak through the back?\n")
        if decision == "1":
            looper = 1
            print("You decide to enter through the front. Exeedingly risky with no real benefit!")
            chance = random.randint(1, 2)
            if chance == 1:
                print("Luckily, you make it through the front door safely and continue unnoticed!")
            else:
                print("Uh oh, you were noticed by the dragon!")
                health = health - 40
                print(f"Although you eventually escape, you are heavily wounded, and lost 40 health. You now have {health} health.")
        else:
            if decision == "2":
                looper = 1
                print("You decide to enter through the back. A wise choice, as it is not as heavily defended!")
                chance = random.randint(1, 5)
                if chance < 5:
                    print("Luckily, you make it through the back door safely and continue unnoticed!")
                else:
                    print("Uh oh, you were somehow still noticed by the dragon! (A 1/5 chance!)")
                    health = health - 40
                    print(f"Although you eventually escape, you are heavily wounded, and lost 40 health. You now have {health} health.")
            else:
                print("Please choose a valid answer, 1 or 2.")
    looper = 0
    decision = ""
    print("Now that you have successfully made it into the lair, you can choose to steal from the dragon's hoarde.")
    luck_for_loot = 4
    while looper == 0 and health > 0:
        decision = input("Now, will you:\n1. Attempt to loot the dragon's hoarde\nor\n2. Retreat with what you have now?\n")
        if decision == "1":
            print("You attempt to steal from the dragon!")
            chance = random.randint(1, luck_for_loot)
            if chance <= 4:
                points = points + 20
                print(f"You successfully loot the dragon's hoarde! You grabbed one item worth 20 points!\nYou now have {points} points!")
                luck_for_loot = luck_for_loot + 1
                print("You were successful this time, but next time, you may not be so lucky, as each time you attempt to loot the dragon, it gets tougher and tougher to loot the dragon.")
            else:
                health = health - 30
                if health > 0:
                    print(f"You stumble over a trap and were caught by the dragon! You get away, but not before losing 30 health! You now have {health} health and {points} points!")
                    luck_for_loot = luck_for_loot + 1
                else:
                    print(f"You stumble over a trap and were caught by the dragon! You get away, but not before losing 30 health! Unfortunately, you have now been wounded.\nAs you flee frantically, you forget to bring anything you have taken so far, which means you have gained 0 points from this adventure.\nAdditionally, it costs you 50 points to heal. You have {points} points. However, the king soon asks you to try again.")
                    return (initial - 50)
        else:
            if decision == "2":
                looper = 2
                points = points + health
                print(f"You run away with what you have now. In total, you now have {health} health and {points} points and gained {points - initial} points from this adventure! \nThe king, however, greedy for more, asks you to loot the dragon again! Will you take up his offer?")
                return points
            else:
                print("Please choose a valid choice, 1 or 2")
    return 0
        

def greet() -> None:
    """This function greets the player, gets their name, and tells them the gist of the story."""
    global player
    print("You are now entering the world of Desmeth, a mystical land ruled by the fair king Fahrier, who has tasked you with a mission, \nwhich is to get back the stolen gold from the hoard of the Dragon Bob")
    player = input("Welcome to the greatest challenge of your life!\nNow what is your name, traveler? ")
    print("What a wonderful name!")
    

player: str = ""
points: int = 0
if __name__ == "__main__":
    main()