# Este programa lista as dez palavras mais presentes num arquivo texto (.txt)

while True:
    lista = list()
    contagem = dict()
    try:
        arq = input("Entre com um arquivo (extensão .txt, e digite STOP para acabar o programa):\n>>> ")
        arq_aberto = open(arq)
    except:
    	if arq == "STOP" or "stop":
            print("FIM DE PROGRAMA")
            break
    for linha in arq_aberto:
    linha = linha.split()
    for palavra in linha:
            contagem[palavra] = contagem.get(palavra, 0) + 1
    contagem = sorted(((valor, chave) for chave, valor in contagem.items()), reverse=True)
    print(contagem, "\n")
    contador = 0
    for (a, b) in contagem:
        if contador >= 10:
            break
        print(a, b)
        contador += 1

