class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_element(self, row, col, value):
        self.matrix[row][col] = value

    def get_element(self, row, col):
        return self.matrix[row][col]

    def transpose(self):
        transposed_matrix = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                transposed_matrix[j][i] = self.matrix[i][j]
        
        self.matrix = transposed_matrix
        self.rows, self.cols = self.cols, self.rows

    def matrix_multiply(self, other_matrix):
        if self.cols != other_matrix.rows:
            return None

        result = [[0 for _ in range(other_matrix.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(other_matrix.cols):
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]

        return result

    def apply_transformation(self, transformation_func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = transformation_func(self.matrix[i][j])


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  
print(stack.peek())  


queue = Queue()
queue.push(1)
queue.push(2)
print(queue.pop())  
print(queue.peek())  


matrix = Matrix(2, 2)
matrix.set_element(0, 0, 1)
matrix.set_element(0, 1, 2)
matrix.set_element(1, 0, 3)
matrix.set_element(1, 1, 4)
print(matrix.get_element(1, 1))  
matrix.transpose()
print(matrix.get_element(0, 1))  
matrix.apply_transformation(lambda x: x * 2)
print(matrix.get_element(1, 1))  

matrix1 = Matrix(2, 3)
matrix1.set_element(0, 0, 1)
matrix1.set_element(0, 1, 2)
matrix1.set_element(0, 2, 3)
matrix1.set_element(1, 0, 4)
matrix1.set_element(1, 1, 5)
matrix1.set_element(1, 2, 6)

matrix2 = Matrix(3, 2)
matrix2.set_element(0, 0, 7)
matrix2.set_element(0, 1, 8)
matrix2.set_element(1, 0, 9)
matrix2.set_element(1, 1, 10)
matrix2.set_element(2, 0, 11)
matrix2.set_element(2, 1, 12)


result_matrix = matrix1.matrix_multiply(matrix2)

for row in result_matrix:
    print(row)
