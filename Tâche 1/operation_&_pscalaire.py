from typing import List, Union, Tuple

class Array:
    def __init__(self, data: Union[List[int], List[List[int]]]):
        self.data = data
        if isinstance(data[0], list):
            self.shape = (len(data), len(data[0]))  # Tableau 2D
        else:
            self.shape = (len(data),)  # Tableau 1D

    def __repr__(self):
        return f"Array({self.data})"

    def __add__(self, other: Union['Array', int, float]) -> 'Array':
        return self._element_wise_operation(other, lambda x, y: x + y)

    def __sub__(self, other: Union['Array', int, float]) -> 'Array':
        return self._element_wise_operation(other, lambda x, y: x - y)

    def __mul__(self, other: Union['Array', int, float]) -> 'Array':
        return self._element_wise_operation(other, lambda x, y: x * y)

    def __truediv__(self, other: Union['Array', int, float]) -> 'Array':
        return self._element_wise_operation(other, lambda x, y: x / y)

    def __matmul__(self, other: 'Array') -> float:
        if len(self.shape) != 1 or len(other.shape) != 1 or self.shape[0] != other.shape[0]:
            raise ValueError("Les deux tableaux doivent être 1D et de même longueur pour le produit scalaire.")
        return sum(x * y for x, y in zip(self.data, other.data))

    def _element_wise_operation(self, other: Union['Array', int, float], operation) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les formes des tableaux ne correspondent pas pour l'opération")
            if len(self.shape) == 2:
                result = [[operation(self.data[i][j], other.data[i][j]) for j in range(self.shape[1])] for i in range(self.shape[0])]
            else:
                result = [operation(self.data[i], other.data[i]) for i in range(self.shape[0])]
        elif isinstance(other, (int, float)):
            if len(self.shape) == 2:
                result = [[operation(self.data[i][j], other) for j in range(self.shape[1])] for i in range(self.shape[0])]
            else:
                result = [operation(self.data[i], other) for i in range(self.shape[0])]
        else:
            raise TypeError("Type non supporté pour l'opération")
        return Array(result)

def saisir_donnees() -> Union[List[int], List[List[int]]]:
    type_tableau = input("Entrez '1' pour un tableau 1D ou '2' pour un tableau 2D: ")
    if type_tableau == '1':
        return [int(x) for x in input("Entrez les éléments du tableau 1D séparés par des virgules: ").split(',')]
    elif type_tableau == '2':
        lignes = int(input("Entrez le nombre de lignes: "))
        return [[int(x) for x in input(f"Entrez les éléments de la ligne {i+1} séparés par des virgules: ").split(',')] for i in range(lignes)]
    else:
        raise ValueError("Choix non valide. Veuillez entrer '1' ou '2'.")

def menu():
    print("\nMenu des opérations :")
    print("1. Addition de deux tableaux")
    print("2. Soustraction de deux tableaux")
    print("3. Multiplication de deux tableaux")
    print("4. Division de deux tableaux")
    print("5. Produit scalaire de deux tableaux")
    print("6. Quitter")
    return input("Choisissez une opération (1-6) : ")

def main():
    operations = {
        '1': ('+', lambda x, y: x + y),
        '2': ('-', lambda x, y: x - y),
        '3': ('*', lambda x, y: x * y),
        '4': ('/', lambda x, y: x / y),
        '5': ('@', lambda x, y: x @ y)
    }
    
    while True:
        choix = menu()
        if choix == '6':
            print("Au revoir!")
            break
        
        if choix in operations:
            tableau1 = Array(saisir_donnees())
            tableau2 = Array(saisir_donnees())
            op_name, op_func = operations[choix]
            try:
                print(f"Résultat de l'opération {op_name} :")
                print(op_func(tableau1, tableau2))
            except ValueError as e:
                print(f"Erreur : {e}")

if __name__ == "__main__":
    main()