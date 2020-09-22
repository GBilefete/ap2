from No import No

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    # Insere um elemento na pilha
    def push(self, elem):
        no = No(elem)
        no.proximo = self.topo
        self.topo = no
        self.tamanho += 1

    # Remove o elemento do topo da pilha
    def pop(self):
        if self.tamanho > 0:
            no = self.topo
            self.topo = self.topo.proximo
            self.tamanho -= 1 
            return no.dado
        raise IndexError("A pilha está vazia!")

    # Retorna o topo da pilha sem remover
    def peek(self):
        if self.tamanho > 0:
            return self.topo.dado
        raise IndexError("A pilha está vazia!")

    # Retorna o tamanho da lista
    def __len__(self):
        return self.tamanho

    # Representa um objeto como uma string
    def __repr__(self):
        r = ""
        pointer = self.topo
        while(pointer):
            r = r + str(pointer.dado) + "\n"
            pointer = pointer.proximo
        return r
    
    def __str__(self):
        return self.__repr__()
