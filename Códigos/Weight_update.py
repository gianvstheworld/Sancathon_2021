# Imports
import pandas as pd
from tensorflow import *
import numpy as np

'''
class NeuralNetwork():

    def __init__(self, learning_rate):
        # gerando pesos aleatórios de acordo com uma distribuição normal em uma matriz 
        self.weights = np.array([np.random.randn(), np.random.randn()])  
        # viés aleatório de acordo com uma distribuição normal 
        self.bias = np.random.randn()
        # setando a taxa de aprendizagem da rede 
        self.learning_rate = learning_rate

    def softplus(self, x):
        # aplicando a função softplus
        return np.log1p(np.exp(-np.abs(x))) + np.maximum(x, 0)

    def softplus_derivative(self, x):
        # aplicando a derivada da função softplus
        return np.exp((-np.abs(x)))/(1 + np.exp((-np.abs(x)))) 

    def predict(self, input_vet):
        layer_1 = np.dot(input_vet, self.weights) + self.bias
        layer_2 = self.softplus(layer_1)
        prediction = layer_2

        return prediction

    def gradient(self, input_vet, target_prediction):
        layer_1 = np.dot(input_vet, self.weights) + self.bias
        layer_2 = self.softplus(layer_1)
        prediction = layer_2
        
        error_prediction = 2 * (prediction - target_prediction)
        prediction_layer1 = self.softplus_derivative(layer_1)
        layer1_bias = 1
        layer1_weights = (0 * self.weights) + (1 * input_vet)

        error_bias = (error_prediction * prediction_layer1 * layer1_bias)
        error_weights = (error_prediction * prediction_layer1 * layer1_weights)

        return error_bias, error_weights

    def update_parameters(self, error_bias, error_weights):
        self.bias = self.bias - (error_bias * self.learning_rate)
        self.weights = self.weights - (error_weights * self.learning_rate)

    def train(self, input_vet, targets, iterations):
        cumulative_errors = []
        for current_iteration in range(iterations):
            # pegando os dados aleatórios
            random_data_index = np.random.randint(len(input_vet))

            input_vet = input_vet[random_data_index]
            target_prediction = targets[random_data_index]

            error_bias, error_weights = self.gradient(input_vet, target_prediction)

            self.update_parameters(error_bias, error_weights)

            if current_iteration % 100 == 0:
                cumulative_error = 0

                for data_instance_index in range(len(input_vet)):
                    data_point = input_vet[data_instance_index]
                    target_prediction = targets[data_instance_index]

                    target_prediction = self.predict(data_point)
                    error = np.square(prediction - target_prediction)

                    cumulative_error += error

                cumulative_errors.append(cumulative_error)
'''

def main():
    model = keras.Sequential([
        tf.keras.layers.RNN(cell, return_sequences = False, return_state = False, go_backward = False,
        stateful = False, unroll = False, time_major = False, **kwargs)

    ])

# Criando tabela
hd1 = pd.Series({'weight': 0.4, 'people flow/bus': 40, 'people flow/time': 10})
hd2 = pd.Series({'weight': 0.5, 'people flow/bus': 35, 'people flow/time': 36})
hd3 = pd.Series({'weight': 0.6, 'people flow/bus': 10, 'people flow/time': 9})
hd4 = pd.Series({'weight': 0.55, 'people flow/bus': 30, 'people flow/time': 7})

df = pd.DataFrame([hd1, hd2, hd3, hd4])

# A, B: Constantes a serem otimizadas pelo algoritmo
dw = 0.3*(sqrt(abs(dpdt - Mdpdt))) - 0.1*(sqrt(abs(dpdb - Mdpdb)))

''' aqui a ideia é atualiar o peso de uma certa linha ao longo do HD (horarios do dia),
só precisa ver se realmente a funcao ta fncionando suave pra atualizar os pesos, 
nesse caso é só fazer que o novo peso (nw) = peso atual (w) + dw, naquela hora do dia
Acho que da pra fazer uma tabela cheia de valores aleatorios mesmo e boa, mas é melhor 
fazer em pandas mesmo
'''

''' Caso o peso em alguma hora do dia antinja um valor critico ou se eles esteja perto disso
, guardar ele em um txt ou algo do genero sei la, acho que pra começar é melhor só pegar uns
valor criticos aleatorios normal mesmo e fazer o machine learning. 
No ML a gente tinha escolhido usar rede nerual (NN) pra fazer uma predição através de 
regressão. Pra fazer uma rede de regressão vamo usar poucas camadas escondidas so pro teste,
acho que umas 3 já dá suave com uns 10 neuronios cada? sla
mas de funcao de ativação é a SOFTPLUS a boa, de otimizar ADAM, e tem que pesquisar se a rede
vai ser RNN ou nao. Pra implementar isso só puxar um tensor flow e usar tf.keras pra fazer 
praticamente tdo.
'''