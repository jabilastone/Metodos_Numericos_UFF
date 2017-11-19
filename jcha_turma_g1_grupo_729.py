######################################
######### Bibliotecas
######################################

import math

######################################
######### Variáveis
######################################

# Descrição das variáveis:
# func(x) : Lei da Função
# func_(x) : Derivada de func(x)
# [a, b] : Intervalo dos valores
a = 2
b = 3
# x0 : Aproximação Inicial
x0 = float(2.5)
# tol : tolerância
tol = float(0.0001)
# nmax : Número máximo de interações
nmax = int(20)

######################################
######### Funções
######################################

#Função que retorna o valor de x para a Lei da Função.
def func(x):
    return float(x*math.log10(x)-1)

#Função que retorna o valor de x para a derivada da Lei da Função.
def func_(x):
    return float((math.log10(x)+1/math.log(10)))

#Função para retornar o valor da aproximação pelo metódo do ponto fixo.
def ponto_fixo(func,x0,nmax,tol):
    #Define o controlador da interação como zero.
    n = 0
    #Escreve o cabeçalho do arquivo para o metódo da newton-raphson.
    file.write("%s\n" % "METÓDO DO PONTO FIXO - Parâmetros Iniciais")
    file.write("%s\n" % ("Aproximação inicial: "+str(x0)))
    file.write("%s\n" % ("Tolerância: "+str(tol)))
    file.write("%s\n" % ("Número máximo de interações: "+str(nmax)))
    file.write("\n")
    file.write("%s\n" % "Metódo ponto fixo")
    file.write("%s\n" % ("i;x1;|f(x1)|;|(x1-x0)|/|x1|"))
    #Enquanto n menor ou igual ao número máximo de interações(nmax) faça:
    while n<=nmax and True:
        #Cálculo da próxima interação.
        x1 = 1/math.log10(x0)
        #Cálcula os valores que serão usados ao longo do da interação para comparar com o critério de parada
        # e salvar no arquivo de resultado - assim poupamos custo computacional.
        f_b =abs(func(x1))
        f_a = abs((x1-x0)/x1)
        #Escreve os valores iniciais da interação.
        escreve_valor([n])
        #Se o valor em módulo(abs) do ponto x1 para a Lei da Função for menor que a tolerância:
        if f_b < tol and f_a < tol:
            #Escreve os resultados atuais antes de interromper a execução
            escreve_linha([x1,f_b,f_a],True)
            #Escrevemos os resultados caso os critérios de parada sejam satisfeitos.
            file.write("Aproximação: "+ str("{:.5e}".format(x1)))
            file.write("\n")
            file.write("%s\n" % "Parada: Tolerância.")
            file.write("%s\n" % "----------------------------------------------------------------------------------")
            file.write("\n")
            #Interrompe as interações caso os critérios de parada sejam satisfeitos.
            return (False)
        else:
            #Guardamos o valor da aproximação calculada para a próxima interação.
            x0 = x1
            #Incrementamos o controlador da interação.
            n=n+1
            #Escreve os valores iniciais da interação.
            escreve_linha([x1,f_b,f_a],True)
    #Escrevemos os resultados caso o número máximo de interações seja atingido e o critério de parada
    # não tenha sido satisfeito.
    file.write("Aproximação: "+ str("{:.5e}".format(x1)))
    file.write("\n")
    file.write("%s\n" % "Parada: Número máximo de interações.")
    file.write("%s\n" % "----------------------------------------------------------------------------------")
    file.write("\n")
    #Finalizamos a execução da função.
    return (False)

#Função para retornar o valor da aproximação pelo metódo de Newton-Raphson.
def newtonraphson(func,func_,x0,nmax,tol):
    #Define o controlador da interação como zero.
    n=0
    #Escreve o cabeçalho do arquivo para o metódo da newton-raphson.
    file.write("%s\n" % "METÓDO DE NEWTON-RAPHSON - Parâmetros Iniciais")
    file.write("%s\n" % ("Aproximação inicial: "+str(x0)))
    file.write("%s\n" % ("Tolerância: "+str(tol)))
    file.write("%s\n" % ("Número máximo de interações: "+str(nmax)))
    file.write("\n")
    file.write("%s\n" % "Metódo newton-raphson")
    file.write("%s\n" % ("i;x1;|f(x1)|;|(x1-x0)|/|x1|"))
    #Enquanto n menor ou igual ao número máximo de interações(nmax) faça:
    while n<=nmax and True:
        #Cálcula o valor da aproximação com base na aproximação inicial menos a função no ponto da aproximação
        # inicial sobre a derivada da função na aproximação inicial.
        x1 = x0 - (func(x0)/func_(x0))
        #Cálcula os valores que serão usados ao longo do da interação para comparar com o critério de parada
        # e salvar no arquivo de resultado - assim poupamos custo computacional.
        f_a = (abs((x1-x0))/abs(x1))
        f_b = abs (func(x1))
        #Escreve o valor de n na linha da interação.
        escreve_valor([n])
        #Se o critério de parada for satisfeito interrompemos a execução do código.
        if (f_a < tol) and (f_b < tol):
            #Escreve os resultados atuais antes de interromper a execução
            escreve_linha([x1,f_b,f_a],True)
            #Escrevemos os resultados caso os critérios de parada sejam satisfeitos.
            file.write("Aproximação: "+ str("{:.5e}".format(x1)))
            file.write("\n")
            file.write("%s\n" % "Parada: Tolerância.")
            file.write("%s\n" % "----------------------------------------------------------------------------------")
            file.write("\n")
            #Interrompe as interações caso os critérios de parada sejam satisfeitos.
            return (False)
        #Caso contrário continuamos o cálculo das interações para aproximar a raiz.
        else:
            #Guardamos o valor da aproximação calculada para a próxima interação.
            x0=x1
        #Escreve a linhas com os valores das interações atuais.
        escreve_linha([x1,f_b,f_a],True)
        #Incrementamos o controlador da interação.
        n=n+1
    #Escrevemos os resultados caso o número máximo de interações seja atingido e o critério de parada
    # não tenha sido satisfeito.
    file.write("Aproximação: "+ str("{:.5e}".format(x1)))
    file.write("\n")
    file.write("%s\n" % "Parada: Número máximo de interações.")
    file.write("%s\n" % "----------------------------------------------------------------------------------")
    file.write("\n")
    #Finalizamos a execução da função.
    return (False)

#Função para retornar o valor da aproximação pelo metódo da Bissecção.
def bisseccao(f,a,b,nmax,tol):
    #Define o controlador da interação como zero.
    n=0
    #Escreve o cabeçalho do arquivo para o metódo da bissecção.
    file.write("%s\n" % "METÓDO DA BISSECÇÃO - Parâmetros Iniciais")
    file.write("%s\n" % ("Intervalos Iniciais: ["+str(a)+","+str(b)+"]"))
    file.write("%s\n" % ("Tolerância: "+str(tol)))
    file.write("%s\n" % ("Número máximo de interações: "+str(nmax)))
    file.write("\n")
    file.write("%s\n" % "Metódo bissecção")
    file.write("%s\n" % ("i;a;b;c;f(a);f(b);f(c);|((b-a)/c)|"))
    #Enquanto n menor ou igual ao número máximo de interações(nmax) faça:
    while n<=nmax and True:
        # Faz o cálculo de x1 com base nos valores de a e b.
        x1 = (a+b)/2.0
        #Cálcula os valores que serão usados ao longo do da interação para comparar com o critério de parada
        # e salvar no arquivo de resultado - assim poupamos custo computacional.
        f_a = float(func(a))
        f_x1 = float(func(x1))
        f_b = float(func(b))
        f_d = float((b-a)/x1)
        #Escreve o valor de n e algumas variáveis antes que elas sofram mudanças devido a interação.
        escreve_valor([n])
        escreve_linha([a,b],False)
        #Se o valor em módulo(abs) do ponto x1 para a Lei da Função for menor que a tolerância:
        if abs(f_x1) < tol:
            #Se a interação não for a primeira(n=0) vamos conferir o critério de parada.
            if n>0:
                #Se o valor absoluto de (b-a)/x1 for menor que a tolerância iremos interromper a execução
                # do código pelo critério de parada.
                if abs(f_d) < tol:
                    #Escrevemos a linha que possui a última interação e seus respectivos valores.
                    escreve_linha([x1,f_a,f_b,f_x1,abs(f_d)],True)
                    #Escrevemos os resultados caso os critérios de parada sejam satisfeitos.
                    file.write("Aproximação: "+ str("{:.5e}".format(x1)))
                    file.write("\n")
                    file.write("%s\n" % "Parada: Tolerância.")
                    file.write("%s\n" % "----------------------------------------------------------------------------------")
                    file.write("\n")
                    #Interrompe as interações.
                    return (False)
            #Se a condição de parada for satisfeita na primeira interação iremos parar a execução.
            elif n==0:
                #Escrevemos a linha que possui a última interação e seus respectivos valores.
                escreve_linha([x1,f_a,f_b,f_x1,abs(f_d)],True)
                #Escrevemos os resultados caso os critérios de parada sejam satisfeitos.
                file.write("Aproximação: "+ str("{:.5e}".format(x1)))
                file.write("\n")
                file.write("%s\n" % "Parada: Tolerância.")
                file.write("%s\n" % "----------------------------------------------------------------------------------")
                file.write("\n")
                #Interrompe as interações.
                return (False)
        #Caso o critério de parada não seja satisfeito iremos continuar com o processo de interação.
        if func(x1)*func(a) > 0:
            #Atribuímos o valor de x1 à a.
            a=x1
        #Se não:
        else:
            #Atribuímos o valor de x1 à b.
            b=x1
        #Incrementamos o controlador da interação.
        n=n+1
        #Escreve a linhas com os valores das interações atuais.
        escreve_linha([x1,f_a,f_b,f_x1,abs(f_d)],True)
    #Escrevemos os resultados caso o número máximo de interações seja atingido e o critério de parada
    # não tenha sido satisfeito.
    file.write("Aproximação: "+ str("{:.5e}".format(x1)))
    file.write("\n")
    file.write("%s\n" % "Parada: Número máximo de interações.")
    file.write("%s\n" % "----------------------------------------------------------------------------------")
    file.write("\n")
    #Finalizamos a execução da função.
    return (False)

#Função para escrever os valores no arquivos de resultados.
def escreve_linha(valor,quebra):
    #Para cada item na lista valor.
    for item in valor:
        #Convertemos item por item da lista para o formato decimal com x casas de precisão.
        valor_decimal = ("{:.5e}".format(item))
        #Se o item for o último da lista não iremos inserir o ;
        if valor.index(item) == len(valor)-1:
            file.write((valor_decimal))
        #Caso contrário inserimos ; - usado como separador no momento de ler o arquivo.
        else:
            file.write((valor_decimal+";"))
    #Se o critério de quebra de linha for verdadeiro inserimos o \n responsável por quebrar a linha.
    if quebra==True:
        file.write("\n")

#Função para escrever o valores que não necessitam de notação cientifica.
def escreve_valor(n):
    for item in n:
        file.write(str(item)+";")

######################################
######### Rotina
######################################

#Chama o programa principal.
if __name__ == "__main__":
    
    #Abre um arquivo com no formato .csv com a propriedade de escrita.
    file = open("resultados.csv","w")
    
    #Chamamos a função para o calculo do zero da função pelo metódo de Newton-Raphson.
    newtonraphson(func,func_,x0,nmax,tol)

    #Chamamos a função para o calculo do zero da função pelo metódo do Ponto Fixo.
    ponto_fixo(func,x0,nmax,tol)
    
    #Chamamos a função para o calculo do zero da função pelo metódo do Ponto Fixo.
    bisseccao(func,a,b,nmax,tol)
    
    #Fechamos o arquivos de resultados.
    file.close()
