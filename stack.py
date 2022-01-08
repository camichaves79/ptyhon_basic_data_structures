
class Stack:
    def __init__(self):
        self.__stack_list = []
    
    def push(self, val):
        self.__stack_list.append(val)
        
    def pop(self):
        popped = self.__stack_list[-1]
        del self.__stack_list[-1]
        return popped
    
