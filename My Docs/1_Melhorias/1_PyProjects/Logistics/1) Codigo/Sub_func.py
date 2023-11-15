#Estrutura do codigo
    #o codigo e estruturado em 'Familia', 'Parentes' e 'Filhos' ou seja,
    #cada codigo tem uma biblioteca import pandas as pd (familia)
    #depois temos o pd.ALGUMACOISA (que faz ref a um mudulo dentro da 'familia')
    #por fim, se tiver pd.ALGUMACOISA.OUTRACOISA e a funcao que ela exerce
    #quando pensamos dentro do framework a sequencia e a seguinte
        #Frame Work(Mundo) > Biblioteca (Continente)
        #Assim dentro da Biblioteca/FrameWork, a gente chama o modulo e depois a funcao
            #pd.OpenExcel > no caso, Biblioteca, depois modulo ou Modulo e funcao



x = 3

def func_x(x):
    x = x + 4
    print('Deu certo dentro da funcao ', x)

x = func_x(x)

print (x)

# do jeito que a funcao esta, o ultimo print nao traz nada pois falta o return x no final, 
    # assim ele aloca o valor do calculo (valor novo), na variavel x
    # sem o return a func_x(x) permanece vazia, ja q o calculo e feito depois dela


x = 3 

def func_x(x):
    x = x + 4
    print('Deu certo dentro da funcao ', x)
    return x

x = func_x(x)

print (x)

if __name__ == "__main__":
    print ('hi otario')

# valor atribuido para o x, com o valor novo do calculo


# para importacao de funcoes criadas, 
    # a pasta do arquivo tem que estar no mesmo local onde o codigo primario esta
    # alem disso, quando se invoca a funcao "secundaria", ele exclui tudo o que esta dentro do arquivo
    # para se evitar isso, basta inserir um if __name__ == "__main__"
    # assim o codigo nao e executado em sua totalidade