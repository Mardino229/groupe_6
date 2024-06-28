from typing import List, Union, Tuple

class Array:
    def __init__(self, data: Union[List[int], List[List[int]]]):
        self.data = data
        if isinstance(data[0], list):
            self.shape = (len(data), len(data[0]))  # Tableau 2D
        else:
            self.shape = (len(data),)  # Tableau 1D

    def __len__(self):
        return len(self.data)

    def __add__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les dimensions des tableaux ne correspondent pas")
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

    def __mul__(self, other: Union['Array', int, float])-> 'Array':
        if isinstance(other, Array):
            if len(self.shape) == 2:
                if len(self.data[0]) == len(other.data):
                    result = []
                    for i in range(self.shape[0]):
                        row = []
                        for j in range(other.shape[1]):
                            res = 0
                            for k in range (self.shape[1]):
                                res = res + self.data[i][k] * other.data[k][j]
                            row.append(res)
                        result.append(row)
                    return Array(result)
                else :
                   raise ValueError("La longueur des lignes et les colonnes  des tableaux ne correspondent pas pour la multiplication")
            else:
                if len(other.shape) == 2:
                    if len(self.data) == len(other.data):
                        result = []
                        for i in range(len(self.data)):
                            row = 0
                            for j in range(len(other.data)):
                                row = row + self.data[j] * other.data[j][i]
                                print(row)
                            result.append(row)
                        return Array(result)
                    else:
                        raise ValueError("La longueur des lignes et les colonnes  des tableaux ne correspondent pas pour la multiplication")

        elif isinstance(other, (int, float)):
            if len(self.shape) == 2:
                result = []
                for i in range(self.shape[0]):
                    row = []
                    for j in range(self.shape[1]):
                        row.append(self.data[i][j] * other)
                    result.append(row)
                return Array(result)
            else:
                result = []
                for i in range(self.shape[0]):
                    result.append(self.data[i] * other)
                return Array(result)
        else:
            raise TypeError("Type non supporté pour la multiplication")

    def __sub__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les dimensions des tableaux ne correspondent pas")
            if len(self.shape) == 2:
                result = []
                for i in range(self.shape[0]):
                    row = []
                    for j in range(self.shape[1]):
                        row.append(self.data[i][j] - other.data[i][j])
                    result.append(row)
                return Array(result)
            else:
                result = []
                for i in range(self.shape[0]):
                    result.append(self.data[i] - other.data[i])
                return Array(result)
        elif isinstance(other, (int, float)):
            if len(self.shape) == 2:
                result = []
                for i in range(self.shape[0]):
                    row = []
                    for j in range(self.shape[1]):
                        row.append(self.data[i][j] - other)
                    result.append(row)
                return Array(result)
            else:
                result = []
                for i in range(self.shape[0]):
                    result.append(self.data[i] - other)
                return Array(result)
        else:
            raise TypeError("Type non supporté pour la soustraction")

    def __truediv__(self, other: Union['Array', int, float]) -> 'Array':
        if isinstance(other, Array):
            if 0 in other:
                raise ZeroDivisionError("Division par zéro")
            if self.shape != other.shape:
                raise ValueError("Les dimensions des tableaux ne correspondent pas")
            if len(self.shape) == 2:
                result = []
                for i in range(self.shape[0]):
                    row = []
                    for j in range(self.shape[1]):
                        row.append(self.data[i][j] / other.data[i][j])
                    result.append(row)
                return Array(result)
            else:
                result = []
                for i in range(self.shape[0]):
                    result.append(self.data[i] / other.data[i])
                return Array(result)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division par zéro")
            if len(self.shape) == 2:
                result = []
                for i in range(self.shape[0]):
                    row = []
                    for j in range(self.shape[1]):
                        row.append(self.data[i][j] / other)
                    result.append(row)
                return Array(result)
            else:
                result = []
                for i in range(self.shape[0]):
                    result.append(self.data[i] / other)
                return Array(result)
        else:
            raise TypeError("Type non supporté pour la division")

    def __matmul__(self,other):
        if isinstance(other, Array):
            if len(self.shape) == 1 and len(other.shape) == 1:
                rs = self*other
                res = 0
                for i in range(len(rs.data)):
                    res = res + rs.data[i]
                return res
            else:
                raise TypeError("Les deux tableaux doivent être 1D et de même longueur pour le produit scalaire.")
        else:
            raise TypeError("Type non supporté pour le produit  scalaire")

    def __contains__(self, data):
        if isinstance(data, (int, float)):
            if len(self.shape) == 2:
                for row in self.data:
                    if data in row:
                        return True
            else:
                return data in self.data
        else: 
            raise TypeError("Type non supporté pour la recherche")
    
    def __getitem__(self, key):
        if isinstance(key, int):
            return self.data[key]
        elif isinstance(key, slice):
            return self.data[key.start : key.stop : key.step]
        elif isinstance(key, tuple):
            if len(key) == 2:
                row, col = key
                if isinstance(row, int) and isinstance(col, int):
                    return self.data[row][col]
                elif isinstance(row, slice) and isinstance(col, int):
                    return [row[col] for row in self.data[row]]
                elif isinstance(row, int) and isinstance(col, slice):
                    return self.data[row][col]
                elif isinstance(row, slice) and isinstance(col, slice):
                    return [[self.data[i][j] for j in range(*col.key(len(self.data[0])))]
                            for i in range(*row.key(len(self.data)))]  
                else:
                    raise ValueError("Nombre d'indices incorrect")      
        else:
            raise TypeError("Type d'index non pris en charge")

    def __repr__(self):
        return f"{self.data}"


