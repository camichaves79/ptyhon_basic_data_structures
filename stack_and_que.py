
class Stack:
    def __init__(self):
        self.__stack_list = []
    
    def push(self, val):
        self.__stack_list.append(val)
        
    def pop(self):
        popped = self.__stack_list[-1]
        del self.__stack_list[-1]
        return popped
    
class Que:
    def __init__(self):
        self.__que_list = []
        
    def push(self, val):
        self.__que_list.append(val)
        
    def pop(self):
        popped = self.__que_list[0]
        del self.__que_list[0]
        return popped

# pacientes = Que()

# pacientes.push('primero')
# pacientes.push('segundo')
# pacientes.push('tercero')

# print (pacientes.pop())

# libros = Stack()

# libros.push("el de abajo")
# libros.push('el de la mitad')
# libros.push("el de arriba")

# print (libros.pop())