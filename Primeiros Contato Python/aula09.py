


def escrever_arquivo(texto):
    arquivo = open('teste.txt','w')
    arquivo.write(texto)
    arquivo.close()

def atualiza_arquivo(nometexto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo , 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
   # escrever_arquivo('escrever uma linha \n')
    # atualiza_arquivo('quarta linha \n')
    ler_arquivo('teste.txt')