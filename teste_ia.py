import math
#inpt = input/entrada
inpt = 0

#saida desejada
output_desire = 0

#peso da entrada (impotância de cada informação)
input_weigth = 0.5

#taxa de aprendizagem (velocidade da aprendizagem)
learning_rate = 0.01

#Criando neuronio virtual para impedir que sempre retorne 0 ( bias sempre é igual a 1)
bias = 1
bias_weigth = 0.5


n_interacao = 0
def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0


print(F"entrada: {inpt}\ndesejado: {output_desire}")

#O erro é infinito pois qualquer valor é menor que o infinito
error = math.inf

while not error  == 0:
    print(F'PESO: {input_weigth}')
    n_interacao = n_interacao + 1
    print("numero de interações", n_interacao)


    sum = (inpt * input_weigth) + (bias * bias_weigth)
    output = activation(sum)

    print(f"saida: {output}")

    #Erro = valor desejado - valor real [E = D-R]
    error = output_desire - output

    print(f"erro: {error}")

    if not error == 0 :
        #Peso atual = Peso anterior + Taxa de apredizagem * Entrada * Erro [ Wt = Wt^-1 + (Ta*I*E) ]
        input_weigth = input_weigth + (learning_rate * inpt * error)
        bias_weigth = bias_weigth + (learning_rate * bias * error)