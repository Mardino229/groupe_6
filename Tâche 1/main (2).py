from typing import List, Union, Tuple

class Array:
    def __init__(self, data: Union[List[int], List[List[int]]]):
        self.data = data
        if isinstance(data[0], list):
            self.shape = (len(data), len(data[0]))  # Tableau 2D
        else:
            self.shape = (len(data),)  # Tableau 1D

    def __add__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les formes des tableaux ne correspondent pas pour l'addition")
            if len(self.shape) == 2:
                result = []
                for i in range(self.shape[0]):
                    row = []
                    for j in range(self.shape[1]):
                        row.append(self.data[i][j] + other.data[i][j])
                    result.append(row)
                return Array(result)
            else:
                result = []
                for i in range(self.shape[0]):
                    result.append(self.data[i] + other.data[i])
                return Array(result)
        elif isinstance(other, (int, float)):
            if len(self.shape) == 2:
                result = []
                for i in range(self.shape[0]):
                    row = []
                    for j in range(self.shape[1]):
                        row.append(self.data[i][j] + other)
                    result.append(row)
                return Array(result)
            else:
                result = []
                for i in range(self.shape[0]):
                    result.append(self.data[i] + other)
                return Array(result)
        else:
            raise TypeError("Type non supporté pour l'addition")
