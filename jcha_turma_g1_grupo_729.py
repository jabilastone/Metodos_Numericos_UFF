######################################
######### Bibliotecas
######################################

import math
from decimal import Decimal

######################################
######### Variáveis
######################################

# Descrição das variáveis:
# func(x) : Lei da Função
# func_(x) : Derivada de func(x)
# [a, b] : Intervalo dos valores
a = 2.5
b = 3
# x0 : Aproximação Inicial
x0 = float(2.5)
# tol : tolerância
tol = float(0.001)
# nmax : Número máximo de interações
nmax = int(20)

######################################
######### Funções
######################################

#Função que retorna o valor de x para a Lei da Função.
def func(x):
    return x*math.log10(x)-1

#Função que retorna o valor de x para a derivada da Lei da Função.
def func_(x):
    return (math.log10(x)+1/math.log(10))

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
    #Faz o cálculo de x1 para metódo do ponto fixo.
    # a função math.log10 - reprense o log na base 10 de x.
    x1 = 1/math.log10(x0)
    #Enquanto n menor ou igual ao número máximo de interações(nmax) faça:
    while n<=nmax and True:
        #Se o valor em módulo(abs) do ponto x1 para a Lei da Função for menor que a tolerância:
        if abs(func(x1)) < tol: 
            #Se a interação não for a primeira(n=0) vamos conferir o critério de parada.
            if n>0:
                #Se o valor em módulo de (x1-x0)/x1) for menor que a tolerância iremos parar a execução.
                if abs((x1-x0)/x1) < tol:
                    #Interrompe as interações.
                    return (False,True)
            #Se a condição de parada for satisfeita na primeira interação iremos parar a execução.
            elif n==0:
                #Interrompe as interações.
                return (False,True)
        #Se a condição de parada não for satisfeita iremos continuar a interação.
        else:
            #Cálculo da próxima interação.
            x1 = 1/math.log10(x0)
            #Guardamos o valor da aproximação calculada para a próxima interação.
            x0 = x1
        lista_ponto = [x1,x0,x1]
        lista_ponto_str = ("{:.5e}".format(Decimal(item)) for item in lista_ponto)
        lista_n = [n]
        lista_n.extend(lista_ponto_str)
        file.write(";".join(map(str,lista_n)))
        file.write("\n")
        #Incrementamos o controlador da interação.
        n=n+1
    file.write("Aproximação: "+ str(lista_n[1]))
    file.write("\n")
    #Retornamos o valor da aproximação final para a a função principal.
    return (x1,False)

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
        #Se o valor da aproximação calculada menos o valor da aproximação iniciação for menor que que a tolerância
        # interrompe o código.
        if x1-x0 <tol:
#            Interrompe as interações.
            return (False,True)
        #Caso contrário continua o cálculo das interações para aproximar a raiz.
        else:
            #Guardamos o valor da aproximação calculada para a próxima interação.
            x0=x1
        lista_newton = [x1,x0,x1]
        lista_newton_str = ("{:.5e}".format(Decimal(item)) for item in lista_newton)
        lista_n = [n]
        lista_n.extend(lista_newton_str)
        file.write(";".join(map(str,lista_n)))
        file.write("\n")
        #Incrementamos o controlador da interação.
        n=n+1
    file.write("Aproximação: "+ str(lista_n[1]))
    file.write("\n")
    #Retornamos o valor da aproximação final para a a função principal.
    return (x1,False)

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
        #Calcula o valor da Lei da Função no ponto x que será usado para salvar na planilha de resultados.
        f_a = float(func(a))
        f_x1 = float(func(x1))
        f_b = float(func(b))
        f_d = float((b-a)/x1)
        #Se o valor em módulo(abs) do ponto x1 para a Lei da Função for menor que a tolerância:
        if abs(f_x1) < tol: 
            #Se a interação não for a primeira(n=0) vamos conferir o critério de parada.
            if n>0:
                #Se o valor absoluto de (b-a)/x1 for menor que a tolerância iremos interromper a execução
                # do código pelo critério de parada.
                if abs(f_d) < tol:
                    #Interrompe as interações.
                    return (False,True)
            #Se a condição de parada for satisfeita na primeira interação iremos parar a execução.
            elif n==0:
                #Interrompe as interações.
                return (False,True)
        #Caso contrário iremos prosseguir com o cálculo da aproximação para a funcão.
        else:
            #Realizamos a verificação para ver como iremos continuar com a interação e qual parâmetro
            # será usado para prosseguir a interação.
            if func(x1)*func(a) > 0:
                #Atribuímos o valor de x1 à a.
                a=x1
            #Se não:
            else:
                #Atribuímos o valor de x1 à b.
                b=x1
                
        lista_bisseccao = [a,b,x1,f_a,f_b,f_x1,abs(f_d)]
        lista_bisseccao_str = ("{:.10e}".format(Decimal(item)) for item in lista_bisseccao)
        lista_n = [n]
        lista_n.extend(lista_bisseccao_str)
        file.write(";".join(map(str,lista_n)))
        file.write("\n")
        n=n+1
    file.write("Aproximação: "+ str(lista_n[2]))
    file.write("\n")
    return (x1,False)

def escreve_linha(valor,quebra):
    valor_decimal = ("{:.10e}".format(valor))
    file.write(";".join(map(str,valor_decimal)))

######################################
######### Rotina
######################################

if __name__ == "__main__":
    
    file = open("resultados.csv","w")
    
    newtonraphson_res = newtonraphson(func,func_,x0,nmax,tol)
    print("newtonraphson_res: "+str(newtonraphson_res))
    if newtonraphson_res[1] == True:
        file.write("%s\n" % "Parada: Critério de parada.")
        file.write("%s\n" % "----------------------------------------------------------------------------------")
        file.write("\n")
    else:
        file.write("%s\n" % "Parada: Número máximo de interações.")
        file.write("%s\n" % "----------------------------------------------------------------------------------")
        file.write("\n")

    ponto_fixo_res = ponto_fixo(func,x0,nmax,tol)
    print("ponto_fixo_res: "+str(ponto_fixo_res))
    if ponto_fixo_res[1] == True:
        file.write("%s\n" % "Parada: Critério de parada.")
        file.write("%s\n" % "----------------------------------------------------------------------------------")
        file.write("\n")
    else:
        file.write("%s\n" % "Parada: Número máximo de interações.")
        file.write("%s\n" % "----------------------------------------------------------------------------------")
        file.write("\n")


    bisseccao_res = bisseccao(func,a,b,nmax,tol)
    print("bissecção_res: "+str(bisseccao_res))
    if bisseccao_res[1] == True:
        file.write("%s\n" % "Parada: Critério de parada.")
        file.write("%s\n" % "----------------------------------------------------------------------------------")
        file.write("\n")

    else:
        file.write("%s\n" % "Parada: Número máximo de interações.")
        file.write("%s\n" % "----------------------------------------------------------------------------------")
        file.write("\n")
        
    file.close()
