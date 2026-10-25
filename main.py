import random
import time
import os

possible_thinks = [
    (
        "Social media has made men obsessed with women\n"
        "they have never even met, while women demand\n"
        "lifestyles they have never truly experienced.\n"
        "Everyone is chasing empty fantasies,\n"
        "destroying what they could actually have\n"
        "in pursuit of something temporary."
    ),
    (
        "The right to participate in collective\n"
        "decisions should depend on demonstrating\n"
        "a minimum level of civic competence."
    ),
    (
        "I've learned that being busy doesn't\n"
        "necessarily mean being indifferent.\n"
        "Silence doesn't always mean a lack of care.\n"
        "But when silence becomes a pattern,\n"
        "and effort only comes from one side,\n"
        "it's no longer about time.\n"
        "It's about priority."
    )
]

if __name__ == '__main__':
    text = str(possible_thinks[random.randint(0, len(possible_thinks))])

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[32m10/3/2026 5:41am")
    print("think about that...\n\033[m")

    for char in text:
        print(char, end="", flush=True)
        time.sleep(random.uniform(0.01, 0.1))

    print()