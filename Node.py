from random import *
OPERATORS = ['+', '-', '*', '/','**','%','sin','cos']



class Node:
    #type zero is operator, type 1 is number (either coefficient or variable)
    value = 0
    type = None
    right = None
    left = None
    depth = 0

    #type 0 is operator, type 1 is coefficient/variable (number)
    def __init__(self, type, depth):
        self.type = type
        self.depth = depth

        if type == 'num':
            rand = randint(0,1)
            if rand == 0:
                self.value = randint(-5, 5)
            elif rand == 1:
                self.value = 'x'
        elif type == 'op':
            self.value = OPERATORS[randint(0, len(OPERATORS) - 1)]
        else:
            print('neither op nor num')

    #changes the value of a node to a random operator
    def change_to_operator(self):
        self.type = 'op'
        self.value = OPERATORS[randint(0, len(OPERATORS) - 1)]

        #escape divide by zero error=> challenge
        if self.value == '/' and self.right == 0:
            self.value = OPERATORS[randint(0, 2)]


    #takes node input which should be a number, changes it to an operator, and
    #gives it two number children
    def add_children(self):
            if self.left is None and self.right is None :
                self.change_to_operator()
                if self.value in ['sin', 'cos']:  # Sine and Cosine are unary operations  
                    self.left = Node('num', self.depth + 1)  # Only one child for sine and cosine  
                    self.right = None  
                else:  
                    self.left = Node('num', self.depth + 1)  
                    self.right = Node('num', self.depth + 1)  
                return
            else:
                print('to add children the node must have none')
                return
                
    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # No child.
        if self.right is None and self.left is None:
            height = 1
            middle = len('%s' % self.value) // 2
            return ['%s' % self.value], len('%s' % self.value), height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + ('%s' % self.value)
            second_line = x * ' ' + '/' + (n - x - 1 + len('%s' % self.value)) * ' '
            shifted_lines = [line + len('%s' % self.value) * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + len('%s' % self.value), p + 2, n + len('%s' % self.value) // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()

            first_line = ('%s' % self.value) + x * '_' + (n - x) * ' '
            second_line = (len('%s' % self.value) + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [len('%s' % self.value) * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + len('%s' % self.value), p + 2, len('%s' % self.value) // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()

        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + ('%s' % self.value) + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + len('%s' % self.value) + y) * ' ' + '\\' + (m - y - 1) * ' '

        if q < p:
            right += [m * ' '] * (p - q)
        elif p < q:
            left += [n * ' '] * (q - p)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + len('%s' % self.value) * ' ' + b for a, b in zipped_lines]
        return lines, n + m + len('%s' % self.value), max(p, q) + 2, n + len('%s' % self.value) // 2


