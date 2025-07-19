# The following program creates a text adventure game
import random


def adventure():
    # Introduction
    print("\nOn your adventure searching for the sacred kingdom, you are halted by a forest of legend. ")
    print("Unfamiliar sounds flood your ears, alien smells flowing through your nose. "
          "Prepare to face trials unlike ever before to find the fabled paradise.")

    # Player choices
    print("1. Have COURAGE! and enter the sinister forest.")
    print("2. “NIGERUNDAYOOOO!!!!” Turn around and run.")
    player_choice = int(input("How do you advance? "))

    if player_choice == 1:
        print("\nStepping into the forest, you are overcome with an immense sense of dread. "
              "\nSuddenly the mysterious sounds have origins. You see new flora and fauna, previously unknown.")
    else:
        print("\nYou turn tail and run away to search for an alternate way to the kingdom.")
        return  # Ends the game if the player runs away

    # Continue on your journey
    print("\nYou walk through the gloomy forest, keeping your guard up every step."
          "\nContinuing to walk through, a large obscured figure dashes by. "
          "\nYou look past a few trees and see the mysterious being, rushing down a complex path. "
          "\nOn the other side you see another path, less tangled and complex but more perilous.")

    print("1. Take the complex path and follow the figure")
    print("2. Choose the alternate path, leaving the figure to go its own way.")
    player_choice = int(input("Which path do you take? "))

    if player_choice == 1:  # CONTINUING
        print("\nAs you follow down the complex path, a grotesque hobgoblin drops from the trees and questions you:"
              "\nI speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?\"")
    else:  # YOU DIED
        print("As you walk along the second path, the ground begins to crumble beneath you."
              "\nTrees and bushes tremble around you, and before you can react, you lose your balance—then the earth gives way."
              "\nYou take your last breath as you plunge downward with trees collapsing in on you")
        return  # Ends the game if the player chooses the perilous path

    # The Hobgoblin's riddle
    print("1. An echo—it carries sound without having a physical form")
    print("2. A whispered secret—passed along like the wind, carried by voices but never seen.")
    player_choice = int(input("What is the answer to this riddle? "))

    if player_choice == 1:  # CONTINUING
        print("The hobgoblin, surprised, lets you pass. "
              "\nYou ask if anyone passed before yourself to which the hobgoblin remarks “Nobody has passed through this forest in many years”."
              "\nAs you start to question the creature again, it scurries into the trees and you continue on the path following the mysterious footsteps.")
    else:  # YOU DIED
        print("The hobgoblin thinks for a second then begins to erupt with cackling laughter. "
              "It is impressed with your creative answer but doesn’t allow you to pass. "
              "Suddenly, it begins to grow, shift, and crack. The hobgoblin mutates into something much more despicable. "
              "Drooling at the mouth, it chases you out of the forest.")
        return  # Ends the game if the player answers the riddle incorrectly

    print("\nWith the hobgoblin gone into the canopy above, the forest falls eerily silent. "
          "\nThe path ahead winds sharply and narrows, marked by deep impressions in the soft earth—larger, heavier than human feet. "
          "\nYou follow the being shrouded in mystery with caution. The trees thin at last, revealing a massive clearing bathed in silver light."
          "\nAt its center lies the ruins of an ancient stone archway, half-swallowed by ivy and time. "
          "\nStepping forward, scanning the quiet ruin, you see it: "
          "\nAcross the clearing, just beyond the archway’s shadows, piercing gold eyes glare from the edge of the forest."
          "\nA tall silhouette cloaked in dark crimson, face obscured beneath a jagged hood. The air hums faintly around it, as if time itself bends in its presence.")

    print("1. Ignore the entity and press on")
    print("2. Call out to the enemy")
    player_choice = int(input("What do you do? "))

    if player_choice == 1:
        print("Heart racing, you pretend like you don’t notice the entity and continue through the eerie clearing.")
        # If the player ignores the entity, you'd define their next steps here.
        # For now, let's have them continue, but you might want to add another scene for this branch.
        print(
            "\nYou carefully slip past the ominous figure, hoping it didn't notice you. The path ahead remains shrouded in mist, offering no easy answers.")
        # For the purpose of this instruction, we'll assume the main progression
        # comes from battling the enemy. You'd build out this alternative path next.
        return  # For now, let's end the game here if player avoids, or link to a future scene.
    else:  # Player chooses to battle
        print("You call out to the mysterious being, telling it to reveal itself."
              "\nSlowly out of the shadows, the figure slips from behind the ancient archway."
              "\nSilently, without hesitation the entity rushes towards you. "
              "\nBefore you can react a flash of crimson streaks past you.")
        battle_outcome = random.choice(["win", "win", "lose"])  # Randomly determine win or lose

        if battle_outcome == "win":
            print("\nYou manage to unsheathe your blade and counter the relentless attacks, retaliating with your own. "
                  "\nAs you’re in the midst of charging, the crimson being vanishes. "
                  "\nYou’re no longer being attacked and its quiet in the forest once more. "
                  "\nRelieved, you survey your surroundings.")

            # --- NEW SCENE: THE ANCIENT OAK TREE PUZZLE ---
            # This is where the player finds the pathway to the new scene
            print("\n---")  # Separator for clarity
            print(
                "As you catch your breath, the ground beneath you trembles violently. A section of the clearing's ancient ruins collapses with a groan, revealing a dark, spiraling staircase descending into the earth. A faint, ethereal glow emanates from its depths, beckoning you forward. This wasn't just a battle; it was a trigger.")
            print(
                "\nAs you continue on your path, the forest begins to shift. Trees twist into grotesque shapes, and the ground becomes uneven, almost as if the path itself is trying to confuse you. You come to a sudden halt before a massive, ancient oak tree, its trunk wider than a small house. Carved into its bark are three intricate symbols. A disembodied voice whispers from the leaves above: 'To proceed, choose the symbol that represents growth without end.'")

            # Player choices for the Oak Tree Puzzle
            print("\nWhat do you do?")
            print("1. Touch the spiral symbol.")
            print("2. Touch the circle symbol.")
            print("3. Attempt to climb the tree.")  # Adding a third, potentially less obvious choice

            puzzle_choice = input("Enter your choice (1, 2, or 3): ")

            if puzzle_choice == "1":  # Correct answer
                print(
                    "\nA low rumble shakes the ground as the tree's bark begins to peel back, revealing a hidden passage. "
                    "\nThe voice booms, 'You understand the endless cycle. Proceed, adventurer.' "
                    "\nThe path before you is now clear, leading deeper into the heart of the forest, closer to your destination.")
                # You would add the next part of your story here, perhaps a new function call
                print("\nYou feel a surge of hope. What new wonders (or dangers) await within the depths?")

                # --- NEW SCENE: THE ROYAL GUARDIAN ---
                print("\n---")  # Separator
                print(
                    "Emerging from the hidden passage, you find yourself in a shimmering cavern. Crystals of every color illuminate the path, casting a dreamlike glow. In the center of the cavern, a colossal, armored figure stands motionless, blocking the only exit. Its eyes, glowing with a soft blue light, track your every move. This must be a Royal Guardian, tasked with protecting the sacred kingdom.")
                print(
                    "\n'State your purpose, traveler,' a deep, resonant voice echoes through the cavern, seemingly coming from the Guardian itself. 'Only those pure of heart and strong of will may pass.'")

                print("\nWhat do you say?")
                print("1. 'I seek the sacred kingdom to bring peace to the lands!'")
                print("2. 'I wish to claim the kingdom's power for myself!'")
                print("3. 'I am merely lost, seeking refuge.'")

                guardian_choice = input("Enter your choice (1, 2, or 3): ")

                if guardian_choice == "1":
                    print(
                        "\nThe Royal Guardian's blue eyes soften. 'Your heart is true. Pass, adventurer. The sacred kingdom awaits.'")
                    print("\n--- VICTORY! ---")
                    print(
                        "You have successfully navigated the trials and reached the sacred kingdom! Your legend will be sung for generations.")
                elif guardian_choice == "2":
                    print(
                        "\nThe Royal Guardian's eyes narrow, and its armor begins to glow fiercely. 'Your ambition is corrupt. You shall not defile this sacred place!'")
                    print(
                        "\nWith a mighty roar, the Guardian lunges. You are overwhelmed by its power. Your quest ends here.")
                    print("\n--- DEATH ---")
                    return
                elif guardian_choice == "3":
                    print(
                        "\nThe Royal Guardian's voice hardens. 'Deception will not serve you. Only those with a clear purpose may approach the kingdom.'")
                    print(
                        "\nThe Guardian raises its massive sword, and you realize your mistake. It strikes with swift, undeniable force. Your journey is over.")
                    print("\n--- DEATH ---")
                    return
                else:
                    print(
                        "Invalid choice. The Royal Guardian stares impassively, waiting for a clear answer. As you hesitate, it deems you unworthy.")
                    print("\n--- DEATH ---")
                    return


            elif puzzle_choice == "2":  # Incorrect answer (Game Over)
                print("\nThe voice lets out a disappointed sigh. 'A symbol of wholeness, yes, but not of growth.' "
                      "\nThe ground beneath you churns, and roots erupt from the earth, ensnaring your legs. "
                      "\nYou struggle, but the grip tightens, pulling you deeper into the earth. The light fades, and the whispers become a mournful dirge. "
                      "\nYou're consumed by the forest, your quest ending here.")
                print("\n--- DEATH ---")
                return  # Ends the game

            elif puzzle_choice == "3":  # Creative/Risky choice (Setback)
                print(
                    "\nYou decide against the cryptic symbols, opting for a direct approach. The ancient bark is rough, offering purchase, and you begin to ascend. "
                    "\nHowever, as you climb higher, the branches twist into thorny cages, and luminous, stinging insects swarm from hidden nests, forcing you back down, injured and unsuccessful. "
                    "\nYou fall to the base, disoriented. The voice from the tree scoffs, 'Impatience is a fool's path.'")

                # --- SECOND CHANCE FOR THE OAK TREE PUZZLE ---
                print("\n---")  # Separator
                print(
                    "Bruised and frustrated, you find yourself back at the base of the ancient oak. The three symbols still glow faintly, beckoning you. The disembodied voice returns, its tone a little sharper: 'Choose wisely this time, adventurer. The forest's patience wears thin.'")

                print("\nWhat do you do now?")
                print("1. Touch the spiral symbol.")
                print("2. Touch the circle symbol.")
                print("3. Try to find another way around the tree.")  # A new option for this retry

                second_chance_choice = input("Enter your choice (1, 2, or 3): ")

                if second_chance_choice == "1":  # Correct answer
                    print(
                        "\nA low rumble shakes the ground as the tree's bark begins to peel back, revealing a hidden passage. "
                        "\nThe voice booms, 'You understand the endless cycle. Proceed, adventurer.' "
                        "\nThe path before you is now clear, leading deeper into the heart of the forest, closer to your destination.")
                    print("\nYou feel a surge of hope. What new wonders (or dangers) await within the depths?")
                    # Continue to the Royal Guardian scene
                    print("\n---")  # Separator
                    print(
                        "Emerging from the hidden passage, you find yourself in a shimmering cavern. Crystals of every color illuminate the path, casting a dreamlike glow. "
                        ""
                        "\nIn the center of the cavern, a colossal, armored figure stands motionless, blocking the only exit. Its eyes, glowing with a soft blue light, track your every move. "
                        "\nThis must one of the Ancient Guardians, tasked with protecting the sacred kingdom.")
                    print(
                        "\n'State your purpose, traveler,' a deep, resonant voice echoes through the cavern, seemingly coming from the Guardian itself. 'Only those pure of heart and strong of will may pass.'")

                    print("\nWhat do you say?")
                    print("1. 'I seek the sacred kingdom to return the world to its proper state.'")
                    print("2. 'I wish to claim the kingdom's power for myself!'")
                    print("3. 'I am merely lost, seeking refuge.'")

                    guardian_choice = input("Enter your choice (1, 2, or 3): ")

                    if guardian_choice == "1":
                        print(
                            "\nThe Ancient Guardian's red eyes soften to a pure blue. 'Your heart is true. Pass, adventurer. The sacred kingdom awaits.'")
                        print("\n--- VICTORY! ---")
                        print(
                            "You have successfully navigated the trials and reached the sacred kingdom! Your legend will be sung for generations.")
                    elif guardian_choice == "2":
                        print(
                            "\nThe Ancient Guardian's eyes narrow, and its armor begins to glow fiercely. 'Your ambition is corrupt. You shall not defile this sacred place!'")
                        print(
                            "\nWith a mighty roar, the Guardian lunges. You are overwhelmed by its power. Your quest ends here.")
                        print("\n--- DEATH ---")
                        return
                    elif guardian_choice == "3":
                        print(
                            "\nThe Ancient Guardian's voice hardens. 'Deception will not serve you. Only those with a clear purpose may approach the kingdom.'")
                        print(
                            "\nThe Guardian raises its massive sword, and you realize your mistake. It strikes with swift, undeniable force. Your journey is over.")
                        print("\n--- DEATH ---")
                        return
                    else:
                        print(
                            "Invalid choice. The Ancient Guardian stares impassively, waiting for a clear answer. As you hesitate, it deems you unworthy.")
                        print("\n--- DEATH ---")
                        return

                else:  # Any other choice leads to consumption
                    print(
                        "\nThe voice from the tree booms, filled with finality. 'Your indecision seals your fate. The forest claims what it is owed.'")
                    print(
                        "\nThe roots beneath you surge, wrapping around your body with crushing force. "
                        "\nThe ancient bark closes in, slowly absorbing you into the tree's very being. "
                        "\nYour last sight is the fading light, your last thought a lament for the adventure cut short.")
                    print("\n--- DEATH ---")
                    return  # Ends the game

            else:
                print("Invalid choice. The forest watches as you hesitate.")
                # In a full game, you might want to re-prompt the input or have a consequence.

        else:  # Player loses the battle
            print(
                "\nBefore your fingers can even curl around the hilt —SHING— a razor-thin flash of silver arcs through the air. "
                "\nYou feel a sudden weightlessness where your fingers once were. No pain yet. Just shock. They’ve been severed, cleanly, at lightning speed."
                "\nInstinct kicks in. You spin, reaching for your backup weapon with your off-hand—but SLASH—your wrist is intercepted mid-motion, the blade moving so fast it might as well be light itself. "
                "\nSparks fly as steel meets steel—no, flesh—and a sharp sting tells you’ve been hit again. This opponent doesn’t just counter. They predict."
                "\nThe scent of scorched cloth and coppery blood mingles in the air. You stumble back, heart racing, mind scrambling. "
                "\nYou look ahead, struggling to make out the being that overpowered you. "
                "\nDarkness creeps in, the warm embrace of death has taken you away.")
            print("\n--- DEATH ---")
            return  # Ends the game if the player loses the battle


adventure()