from abc import ABC, abstractmethod
import time, copy, datetime
import numpy as np

class PrototypeNN(ABC):
    # Абстрактный класс слоя нейронной сети
    def __init__(self):
        # Сымитируем долгое исполнение инита (ведь это как раз и является причиной использования данного паттерна)
        time.sleep(10)

        self.weights = None
        self.biases = None

    # Метод для клонирования
    @abstractmethod
    def clone(self):
        pass


class LinearLayer(PrototypeNN):
    def __init__(self, weights, biases):
        super().__init__()
        time.sleep(3)

        self.weights = weights
        self.biases  = biases

    # переопределим метод клонирования
    def clone(self):
        return copy.deepcopy(self)


class ConvLayer(PrototypeNN):
    def __init__(self, weights, biases, kernel_size, stride, padding):
        super().__init__()
        time.sleep(3)

        self.weights = weights
        self.biases  = biases
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

    # переопределим метод клонирования
    def clone(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    print('Starting to create a LinearLayer: ', datetime.datetime.now().time())
    fc = LinearLayer(np.random.randn(5, 5), np.random.randn(5, 1))
    print('Finished creating a LinearLayer: ', datetime.datetime.now().time())

    # Для создания линейного слоя (допустим он большой и расчёты занимают много времени) понадобилось 13 секунд
    # Теперь чтобы создать нейронную сеть из нескольких слоёв мы будем пользоваться паттерном прототипа и просто клонировать слои
    # Так нам не придётся ждать 13 секунд для каждого слоя (при условии что все слои одинаковые) - однако
    # при любом случае после клонирования можно поменять некоторые атрибуты

    nn = []

    print('Initiating neural network: ', datetime.datetime.now().time())
    fc_template = LinearLayer(np.random.randn(5, 5), np.random.randn(5, 1))
    for i in range(5):
        nn.append(fc_template.clone())
        print(f'Finished creating a LinearLayer clone {i} at: ', datetime.datetime.now().time())
    print('Finished neural network initialization: ', datetime.datetime.now().time())

    # Соответственно, можно повторить то же самое с несколькими классами и, например, создать свёрточную нейросеть
    conv_nn = {"conv layers" : [], "linear layers": []}
    print('Initiating convolutional neural network: ', datetime.datetime.now().time())
    fc_template = LinearLayer(np.random.randn(5, 5), np.random.randn(5, 1))
    conv_template = ConvLayer(np.random.randn(10, 6), np.random.randn(6, 1), 3, 1, 0)
    for i in range(3):
        conv_nn["linear layers"].append(fc_template.clone())
        print(f'Finished creating a LinearLayer clone {i} at: ', datetime.datetime.now().time())
        conv_nn["conv layers"].append(conv_template.clone())
        print(f'Finished creating a ConvLayer clone {i} at: ', datetime.datetime.now().time())
    print('Finished neural network initialization: ', datetime.datetime.now().time())
