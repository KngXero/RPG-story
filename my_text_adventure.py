# The following program creates a text adventure game
import random
def adventure():
    # Introduction
    print("\nOn your adventure searching for the sacred kingdom, you are halted by a forest of legend. ")
    print("Unfamiliar sounds flood your ears, alien smells flowing through your nose. "
          "Prepare to face trials unlike ever before to find the fabled paradise.")


    #Player choices
    print("1. Have COURAGE! and enter the sinister forest.")
    print("2.“NIGERUNDAYOOOO!!!!” Turn around and run.")
    player_choice = int(input("How do you advance? "))

    if player_choice == 1:
        print("\nStepping into the forest, you are overcome with an immense sense of dread. "
              "\nSuddenly the mysterious sounds have origins. You see new flora and fauna, previously unknown.")
    else:
        print("\nYou turn tail and run away to search for an alternate way to the kingdom.")
        return
#Continue on your journey
    print("\nYou walk through the gloomy forest, keeping your guard up every step."
          "\nContinuing to walk through, a large obscured figure dashes by. "
          "\nYou look past a few trees and see the mysterious being, rushing down a complex path. "
          "\nOn the other side you see another path, less tangled and complex but more perilous.")

    print("1.Take the complex path and follow the figure")
    print("2.Chose the alternate path, leaving the figure to go its own way.")
    player_choice = int(input("Which path do you take? "))

    if player_choice == 1: #CONTINUING
        print("\nAs you follow down the complex path, a grotesque hobgoblin drops from the trees and questions you:"
            "\nI speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?\"")
    else: #YOU DIED
        print("As you walk along the second path, the ground begins to crumble beneath you."
              "\nTrees and bushes tremble around you, and before you can react, you lose your balance—then the earth gives way."
              "\nYou take your last breath as you plunge downward with trees collapsing in on you")
        return
    #The Hobgoblins riddle
    print("1.An echo—it carries sound without having a physical form")
    print("2.A whispered secret—passed along like the wind, carried by voices but never seen.")
    player_choice = int(input("What is the answer to this riddle? "))

    if player_choice == 1: #CONTINUING
        print("The hobgoblin, surprised, lets you pass. "
              "\nYou ask if anyone passed before yourself to which the hobgoblin remarks “Nobody has passed through this forest in many years”."
              "\nAs you start to question the creature again, it scurries into the trees and you continue on the path following the mysterious footsteps.")
    else: #YOU DIED
        print("The hobgoblin thinks for a second then begins to erupt with cackling laughter. "
              "It is impressed with your creative answer but doesn’t allow you to pass. "
              "Suddenly, it begins to grow, shift, and crack. The hobgoblin mutates into something much more despicable. "
              "Drooling at the mouth, it chases you out of the forest.")
        return
    print("\nWith the hobgoblin gone into the canopy above, the forest falls eerily silent. "
          "\nThe path ahead winds sharply and narrows, marked by deep impressions in the soft earth—larger, heavier than human feet. "
          "\nYou follow the being shrouded in mystery with caution. The trees thin at last, revealing a massive clearing bathed in silver light."
          "\nAt its center lies the ruins of an ancient stone archway, half-swallowed by ivy and time. "
          "\nStepping forward, scanning the quiet ruin, you see it: "
          "\nAcross the clearing, just beyond the archway’s shadows, piercing gold eyes glare from the edge of the forest."
          "\nA tall silhouette cloaked in dark crimson, face obscured beneath a jagged hood. The air hums faintly around it, as if time itself bends in its presence.")
    print("1.Ignore the entity and press on")
    print("2.Call out to the enemy")
    player_choice = int(input("What do you do? "))

    if player_choice == 1:
        print("Heart racing, you pretend like you don’t notice the entity and continue through the erie clearing.")
    else:
        print("You call out to the mysterious being, telling it to reveal itself."
              "\nSlowly out of the shadows, the figure slips from behind the ancient archway."
              "\nSilently, without hesitation the entity rushes towards you. "
              "\nBefore you can react a flash of crimson streaks past you.")
        battle_outcome = random.choice(["win", "lose"])
        if battle_outcome == "win":
            print("\nYou manage to unsheathe your blade and counter the relentless attacks, retaliating with your own. "
                  "\nAs you’re in the midst of charging, the crimson being vanishes. "
                  "\nYou’re no longer being attacked and its quiet in the forest once more. "
                  "\nRelieved, you continue on your journey.")
        else:
            print("\nBefore your fingers can even curl around the hilt —SHING— a razor-thin flash of silver arcs through the air. "
                  "\nYou feel a sudden weightlessness where your fingers once were. No pain yet. Just shock. They’ve been severed, cleanly, at lightning speed."
                  "\nInstinct kicks in. You spin, reaching for your backup weapon with your off-hand—but SLASH—your wrist is intercepted mid-motion, the blade moving so fast it might as well be light itself. "
                  "\nSparks fly as steel meets steel—no, flesh—and a sharp sting tells you you’ve been hit again. This opponent doesn’t just counter. They predict."
                  "\nThe scent of scorched cloth and coppery blood mingles in the air. You stumble back, heart racing, mind scrambling. "
                  "\nYou look ahead, struggling to make out the being that overpowered you. Darkness creeps in, the warm embrace of death has taken you away.")
            return

adventure()