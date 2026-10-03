import os
import random
import time

if __name__ == '__main__':
    text = "As redes sociais deixaram os homens obcecados por mulheres que nem sequer conhecem, e as mulheres exigindo um estilo de vida que jamais vivenciaram de fato. Todos perseguem fantasias vazias, destruindo o que poderiam realmente ter em nome de algo passageiro."

    c_text = ""
    for i in text:
        os.system("cls")
        c_text += i
        time.sleep(random.uniform(0, 0.1))
        print(c_text)
