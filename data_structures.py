class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

class LinkedList:
    def __init__(self, head_node = None):
        self.head_node = head_node
    
    def __repr__(self):
        list_string = ''
        current_node = self.head_node
        while current_node:
            list_string += str(current_node.get_value()) + '\n'
            current_node = current_node.get_next_node()
        return list_string

    def __len__(self):
        current_node = self.head_node
        count = 0
        while current_node:
            count += 1
            current_node = current_node.get_next_node()
        return count
    
    def set_head_node(self, head_node):
        head_node.set_next_node(self.head_node)
        self.head_node = head_node
    
    def add_node(self, new_node):
        current_node = self.head_node
        while current_node.get_next_node():
            current_node = current_node.get_next_node()
        current_node.set_next_node(new_node)

    def remove_node_value(self, value):
        current_node = self.head_node
        while current_node:
            if current_node.get_next_node().get_value() == value:
                current_node.set_next_node(current_node.get_next_node().get_next_node())
                current_node = None
            else:
                current_node = current_node.get_next_node()

    def remove_node_position(self, position):
        if position == 0:
            self.head_node = self.head_node.get_next_node()
        elif position < self.__len__():
            current_node = self.head_node
            i = 0
            while current_node:
                if i + 1 == position:
                    current_node.set_next_node(current_node.get_next_node().get_next_node())                    
                    current_node = None
                else:
                    current_node = current_node.get_next_node()
                    i += 1
        else:
            print('Value out of range')


    def search(self, value):
        current_node = self.head_node
        while current_node:
            if current_node.get_value() == value:
                return True
            else:
                current_node = current_node.get_next_node()
        return False
    

li = LinkedList(Node('yo'))
li.add_node(Node(47))
li.add_node(Node(['bengals', 'dolphins', 'saints']))

# print(li.search(48))

# print(li)