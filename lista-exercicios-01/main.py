from abc import ABC, abstractmethod


class ListADT(ABC):

    @abstractmethod
    def insert(self, indice, elemento):
        """Insere na posiÃ§Ã£o <indice> o valor <elemento>.
        Como se trata de uma lista, deve ser graratido que
        se houver valor em <indice> que ele nÃ£o seja apagado"""
        ...

    @abstractmethod
    def remove(self, elemento):
        """Remove primeira ocorrÃªncia de <elemento>"""
        ...

    @abstractmethod
    def count(self, elemento):
        """Conta a quantidade de <elemento> na lista"""
        ...

    @abstractmethod
    def clear(self):
        """Apaga a lista"""
        ...

    @abstractmethod
    def index(self, elemento):
        """Retorna o primeiro Ã­ndice de <elemento>"""
        ...

    @abstractmethod
    def length(self):
        """Retorna o tamanho da lista"""
        ...


class Node:

    def __init__(self, element=None, next=None):
        self.__element = element
        self.__next = next

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

    def get_element(self):
        return self.__element

    def set_element(self, element):
        self.__element = element

    def __str__(self):
        return '|' + self.__element.__str__() + '|'


class LinkedList(ListADT):

    def __init__(self, elem=None):
        if elem:
            self._head = Node(elem)  # AtenÃ§Ã£o ao manipular esta referÃªncia
            self._tail = self._head  # Facilita a inserÃ§Ã£o no fim da lista
            self._length = 1
        else:
            self._head = None  # AtenÃ§Ã£o ao manipular esta referÃªncia
            self._tail = None  # Facilita a inserÃ§Ã£o no fim da lista
            self._length = 0

    def insert(self, index, elem):
        # a inserÃ§Ã£o pode acontecer em trÃªs locais: inÃ­cio, meio e fim da lista
        # separei em mÃ©todos diferentes (privados) para facilitar o entendimento
        if index == 0:  # primeiro local de inserÃ§Ã£o Ã© no comeÃ§o da lista
            self.__insert_at_beginning(elem)
        elif index > self._length:  # segundo local de inserÃ§Ã£o Ã© no fim da lista
            self.__insert_at_end(elem)  # se o Ã­ndice passado foi maior que o tamanho da lista, insero no fim
        else:  # por fim, a inserÃ§Ã£o no meio da lista
            self.__insert_in_between(index, elem)

        self._length += 1  # apÃ³s inserido, o tamanho da lista Ã© modificado

    def __insert_at_beginning(self, elem):
        n = Node(elem)  # primeiro criamos o nÃ³ com o elemento a ser inserido
        if self.empty():  # caso particular da lista vazia
            self.__empty_list_insertion(n)
        else:  # se houver elemento na lista
            n.set_next(self._head)  # o head atual passa a ser o segundo elemento
            self._head = n  # e o novo nÃ³ criado passa a ser o novo head

    def __insert_at_end(self, elem):
        n = Node(elem)  # primeiro criamos o nÃ³ com o elemento a ser inserido
        if self.empty():  # caso particular da lista vazia
            self.__empty_list_insertion(n)
        else:
            self._tail.set_next(n)  # o Ãºltimo elemento da lista aponta para o nÃ³ criado
            self._tail = n  # o nÃ³ criado ...a a ser o Ãºltimo elemento

    def __empty_list_insertion(self, node):
        # na inserÃ§Ãµa na lista vazia, head e tail apontam para o nÃ³
        self._head = node
        self._tail = node

    def __insert_in_between(self, index, elem):  # 3
        n = Node(elem)  # primeiro criamos o nÃ³ com o elemento a ser inserido
        pos = 0  # a partir daqui vamos localizar a posiÃ§Ã£o de inserÃ§Ã£o
        aux = self._head  # variÃ¡vel auxiliar para nos ajudar na configuraÃ§Ã£o da posiÃ§Ã£o do novo nÃ³
        while pos < index - 1:  # precorre a lista atÃ© a posiÃ§Ã£o imediatamente anterior
            aux = aux.get_next()  # Ã  posiÃ§Ã£o onde o elemento serÃ¡ inserido
            pos += 1
        n.set_next(aux.get_next())  # quando a posiÃ§Ã£o correta tiver sido alcanÃ§ada, insere o nÃ³
        aux.set_next(n)

    def remove(self, elem):
        if not self.empty():  # SÃ³ pode remover se a lista nÃ£o estiver vazia, nÃ£o Ã©?!
            aux = self._head
            removed = False  # Flag que marca quando a remoÃ§Ã£o foi feita
            if aux.get_element() == elem:  # Caso especial: elemento a ser removido estÃ¡ no head
                self._head = aux.get_next()  # head passa a ser o segundo elemento da lista
            else:
                while aux.get_next() and not removed:  # verifico se estamos no fim da lista e nÃ£o foi removido elemento
                    prev = aux
                    aux = aux.get_next()  # passoo para o prÃ³ximo elemento
                    if aux.get_element() == elem:  # se for o elemento desejado, removo da lista
                        prev.set_next(aux.get_next())
                        removed = True  # marco que foi removido

            if removed:
                self._length -= 1

    def count(self, elem):
        counter = 0
        if not self.empty():  # Verifica se a lista nÃ£o estÃ¡ vazia (sÃ³ faz sentido contar em linear nÃ£o vazias!)
            aux = self._head  # Se a lista nÃ£o estiver vazia, percorre a lista contando as ocorrÃªncias
            if aux.get_element() is elem:
                counter += 1
            while aux.get_next():  # precorrendo a lista....
                aux = aux.get_next()
                if aux.get_element() is elem:
                    counter += 1
        return counter

    def clear(self):
        self._head = None  # todos os nÃ³s que compunham a lista serÃ£o removidos da memÃ³ria pelo coletor de lixo
        self._tail = None
        self._length = 0

    def index(self, elem):
        result = None
        pos = 0
        aux = self._head
        # Vamos percorrer a lista em busca de elem
        while not result and pos < self._length:  # lembrando que not None Ã© o mesmo que True
            if aux.get_element() is elem:
                result = pos
            aux = aux.get_next()
            pos += 1
        return result  # se o elemento nÃ£o estiver na lista, retorna None

    def length(self):
        return self._length

    def empty(self):
        result = False
        if not self._head:
            result = True
        return result



    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._head
            result += aux.__str__()
            while aux.get_next():
                aux = aux.get_next()
                result += aux.__str__()
            return result
        else:
            return '||'


class DoublyLinkedList(ListADT):
    class _DoublyNode:
        def __init__(self, elem, prev, next):
            self._elem = elem
            self._prev = prev
            self._next = next

        def __str__(self):
            if self._elem is not None:
                return str(self._elem) + ' '
            else:
                return '|'

    def __init__(self):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._length = 0

    def insert(self, index, elem):
        if index >= self._length:  # se o indice se inserÃ§Ã£o passado for maior que a lista
            index = self._length  # atualiza para o Ãºltimo indice
        if self.empty():  # Caso da lista vazia
            new_node = self._DoublyNode(elem, self._header, self._trailer)
            self._header._next = new_node
            self._trailer._prev = new_node
        elif index == 0:  # caso da inserÃ§Ã£o na primeira posiÃ§Ã£o da lista
            new_node = self._DoublyNode(elem, self._header, self._header._next)
            self._header._next._prev = new_node
            self._header._next = new_node
        else:  # outros casos de inserÃ§Ã£o
            this = self._header._next
            successor = this._next
            pos = 0
            while pos < index - 1:
                this = successor
                successor = this._next
                pos += 1
            new_node = self._DoublyNode(elem, this, successor)
            this._next = new_node
            successor._prev = new_node

        self._length += 1

    def remove(self, elemento):
        if not self.empty():
            node = self._header._next
            pos = 0
            found = False
            while not found and pos < self._length:
                if node._elem == elemento:
                    found = True
                else:
                    node = node._next
                    pos += 1
            if found:
                node._prev._next = node._next
                node._next._prev = node._prev
                self._length -= 1

    def count(self, elem):
        result = 0
        this = self._header._next
        if self._length > 0:
            while this._next is not None:  # aqui a lista Ã© percorrida
                if this._elem == elem:
                    result += 1
                this = this._next
        return result

    def clear(self):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._length = 0

    def index(self, elem):
        result = None  # armazena a primeira posiÃ§Ã£o do elemento
        pos = 0
        this = self._header._next
        # Vamos percorrer a lista em busca de elem
        while not result and pos < self._length:  # lembrando que not None Ã© o mesmo que True
            if this._elem is elem:
                result = pos
            this = this._next
            pos += 1
        return result  # se o elemento nÃ£o estiver na lista, retorna None

    def length(self):
        return self._length

    def empty(self):
        return self._length == 0

    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._header
            result += aux.__str__()
            while aux._next:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'


if __name__ == '__main__':
    print('Linked List')
    lista = LinkedList()
    print(lista)

    print('inserÃ§Ã£o')
    lista.insert(0, 'teste')
    print(lista)

    lista.insert(20, 20)
    print(lista)

    lista.insert(0, 3.14)
    print(lista)

    lista.insert(1, 'no meio')
    print(lista)

    lista.insert(3, 'no meio')
    print(lista)

    lista.insert(10000, 'loooonge')
    print(lista)

    print('contagem')
    print(lista.count('no meio'))
    print(lista.count('oi'))
    print(lista.count(20))

    print('indices')
    print(lista.index('no meio'))
    print(lista.index('loooonge'))
    print(lista.index('bla'))
    print('remoÃ§Ã£o')

    print('lista inicial')
    print(lista)

    print('vamos remover...')
    lista.remove('no meio')
    print(lista)

    lista.remove('teste')
    print(lista)

    lista.remove(3.14)
    print(lista)
    print('-----------------------------')
    print()
    print('-----------------------------')
    print('Doubly Linked List')
    lista = DoublyLinkedList()
    lista.insert(0, 0)
    print(lista)
    lista.insert(1, 1)
    print(lista)
    lista.insert(2, 2)
    print(lista)
    lista.insert(0, 3)
    print(lista)
    lista.insert(1000, 4)
    print(lista)
    lista.insert(3, 5)
    print(lista)
    print(lista.index(1))
    print(lista.count(1))
    lista.insert(0, 1)
    print(lista.count(1))
    lista.remove(5)
    print(lista)