print("ola!Eu sou IAgamer portatil.)
prit("Digit 'sair' para encerrar.\n")

while True::
pergunta = input("Qual e sua duvida sobre jogos?)

if pergunta.lower() == "sair":
   print("Ate logo! Continue jogando e aprendendo!")
   break

elif "melhor jogo" in pergunta.lower():
    print("Depende do estilo! Para ação, recomendo Apex Legends.")
elif"lançamento" in pergunta.lower():
    print("O novo jogo da série Horizon sai esteano!")
else:
    print("Ainda estou aprendendo sobre isso, mas posso pesquisar depois!")

input("\nPrograma finalizado. Pressione ENTER para fechar...")