import random
import time
import os

possible_thinks = [("As redes sociais deixaram os homens obcecados por mulheres que nem \n"
            "sequer conhecem, e as mulheres exigindo um estilo de vida que jamais\n "
            "vivenciaram de fato. Todos perseguem fantasias vazias, destruindo o \n"
            "que poderiam realmente ter em nome de algo passageiro."), "o direito de participar de decisões coletivas \ndeveria depender de uma demonstração\n mínima de competência cívica"]

if __name__ == '__main__':
    text = str(possible_thinks[random.randint(0, len(possible_thinks))])

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[32m10/3/2026 5:41am")
    print("think about that...\n\033[m")

    for char in text:
        print(char, end="", flush=True)
        time.sleep(random.uniform(0.01, 0.1))

    print()