from random import randint
computador = randint(0,10)
print("=-"*20)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-"*20)
cont = 0
while True:
    n = int(input("Diga um valor: "))
    par_impar = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
    soma = n + computador
    if par_impar == "P":
        if soma %2 == 0:
            print("=-"*20)
            print(f"Voce jogou {n} e o computador {computador}. Total de {soma} DEU PAR")
            print("=-"*20)
            print("Voce VENCEU!")
            cont += 1
            print("Vamos jogar novamente...")
            print("=-"*20)
        else:
            print("=-"*20)
            print(f"Voce jogou {n} e o computador {computador}. Total de {soma} DEU IMPAR")
            print("=-"*20)
            print("Voce PERDEU!") 
            print("=-"*20)   
            break        
    elif par_impar == "I":
        if soma %3 == 0:
            print("=-"*20)
            print(f"Voce jogou {n} e o computador {computador}. Total de {soma} DEU IMPAR")
            print("=-"*20)
            print("Voce VENCEU!")
            cont += 1
            print("Vamos jogar novamente...")
            print("=-"*20)
        else:
            print("=-"*20)
            print(f"Voce jogou {n} e o computador {computador}. Total de {soma} DEU PAR")
            print("=-"*20)
            print("Voce PERDEU!")
            print("=-"*20)
            break
print(f"GAME OVER! Voce venceu {cont} vezes.")    