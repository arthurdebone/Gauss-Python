#------------------------------------------------------------------------------
#--Arthur de Bone
#--Processos estocásticos
#--Escalonação por Gauss e Jordan
#------------------------------------------------------------------------------

class Gauss:
    
    def teste(self):
        print("aquiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

    
    #Método para ler a matriz
    def lerMatriz(self,arq):
        return [[float(x) for x in line.split()] for line in arq]

    #Método para IMPRIMIR MATRIZ
    #   Variável i percorre as colunas
    #   Variável j percorre as linhas
    def mostraMat(self,mat):
        for i in range(len(mat)):
            for j in range (len (mat[i])):
                    print (" %3.5f", mat[i][j])
            print("\n")
        print("\n")
        print("\n")

    #Método para avaliar se a matriz pode ser resolvida
    #   Verifica o numero de equações e incognitas
    #   Se numEqua < incog, o sistema é SPI ou SI, retorna -1
    #   Senão o sistema é PD, retorna 1
    def avaliaMat(self,mat):
        numEqua = len(mat)
        incog = len(mat[0])-1
        if (numEqua < incog):
            return -1
        else:
            return 1

    #Método para achar o maior valor de uma coluna
    def maiorValCol(self,mat,i,j):
        maiorVal = 0
        maiorIndice = i
        while i < len(mat):  #len(mat) devolve o numero de linhas
            if abs(mat[i][j]) > maiorVal:
                maiorVal = mat[i][j]
                maiorIndice = i
            i+= 1
        return maiorIndice

    #Método para zerar abaixo do pivor
    def nuloSobPivo(self,mat, i, j, pivo):
        jAux = j
        while i < len(mat):
            while jAux < len(mat[0]):
                mat[i][jAux] -= mat[i][j]*pivo[jAux]

    #Método que faz escalonação
    def escalona(self,mat):
        for j in range(len(mat[0])-1): #j percorre a linha
            i = j
            maior = maiorValCol(mat, i, j)
            #TROCA DE LINHA (ex: l1 <-> l2)
            aux = mat[i] #Aux recebe a equação que está na linha i para fazer a troca de linha
            mat[i] = mat[maior]
            mat[maior] = aux
            #Agora é necessário dividir toda a linha principal pelo valor do termo principal
            jAux = j
            div = mat[i][j]
            while jAux < len(mat[i]):#Percorre a linha dividindo
                mat[i][jAux] = mat[i][jAux]/div
                jAux += 1
            pivo = mat[i]#Armazena a linha que tem o pivo
            i += 1 #vamos para a proxima equação
            nuloSobPivo(mat, i, j, pivo)#Coloca 0 abaixo do pivo
            print ("\nMatriz após escalonação\n")
            mostraMat(mat)      

    #============================================================================
    #PROGRAMA PRINCIPAL
    def main():
        nome_arq = input("Digite o nome do arquivo que esta a matriz: ")
        arq = open(nome_arq, "r")
        teste()
        mat = lerMatriz(arq.readlines())#coloca em uma matriz no programa

        print ("\nMATRIZ EXTENDIDA\n")
        mostraMat(mat)
        #Verificação se a matriz tem solução
        aval = avaliaMat(mat)
        if aval == -1:
            print("\nSISTEMA INDETERMINADO\n")
        else:
            r = escalona(mat)
    #===========================================================================
