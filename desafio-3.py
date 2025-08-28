'''
1. ler 2 números inteiros, sendo A e B. adicionar ao código para mostrar
duas linhas onde: a primeira linha contenha a soma entre os dois números.
a segunda contenha a diferença entre os dois e a terceira contenha o produto
entre os dois números.

A + B
A(_)B
A x B

'''

def Sum ():
    num1 = a
    num2 = b
    result = a + b
    print('Sum = {} ' .format(result))

def Difference ():
    num1 = a
    num2 = b
    result = a - b
    print('Difference = {}' .format(result))

def Product ():
    num1 = a
    num2 = b
    result = a * b
    print('Product = {}' .format(result))    

if __name__ == '__main__':
    a = int(input('Enter the number of A - ') .strip())
    b = int(input('Enter the number of B - ') .strip())

Sum()
Difference()
Product()