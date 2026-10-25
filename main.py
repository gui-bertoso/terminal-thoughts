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
    ),
    (
        "It's strange how the same people who preach\n"
        "equality, tolerance, and acceptance can become\n"
        "the worst ones the moment you show even\n"
        "the slightest difference in opinion.\n"
        "They talk about respect, but many of them\n"
        "only seem to respect you as long as\n"
        "you think exactly like them."
    ),
    (
        "Why are people always trying to divide\n"
        "themselves into groups, labels, and opposing sides?\n"
        "We are all human.\n"
        "Your skin color, gender, sexuality, or beliefs\n"
        "should not define your worth.\n"
        "In the end, people constantly ask for acceptance,\n"
        "yet so few truly know how to accept each other."
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