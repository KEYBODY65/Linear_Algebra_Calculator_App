class Linear_Bsk_Operations:
	def __init__(self):
		self.n = 0
		self.m = 0
		self.arr_matrix = []

	def add_matrix(self, n:int, m:int):
		self.n = n
		self.m = m
		new_matrix = [[0] * self.m for _ in range(self.n)]
		print(f"Введите элементы матрицы размером {self.n}x{self.m}:")
		for i in range(self.n):
		    for j in range(self.m):
		        new_matrix[i][j] = int(input(f"Элемент [{i + 1}][{j + 1}]: "))
		self.arr_matrix.append(new_matrix) 

	def show(self, matrix):
		for row in matrix:
			print(' '.join(map(str, row)))
		print()

	def transponse(self):
		for matr in self.arr_matrix:
			for i in range(len(matr)):
				for j in range(i + 1, len(matr)):
					matr[i][j], matr[j][i] = matr[j][i], matr[i][j]
		print('Транспонированная матрица:')
		self.show(matr)

	def main_diag(self):
		self.main = []
		for matr in self.arr_matrix:
			c = 0
			h = []
			for i in range(len(matr)):
				h.append(matr[i][c])
				c += 1
			self.main.append(h)
		print(self.main)

	def my_matrix(self):
		for matrix in self.arr_matrix:
			self.show(matrix)

	def matrix_summation(self):
		summa_matr = [[0] * self.m for _ in range(self.n)]
		for col in range(len(self.arr_matrix) - 1):
			for i in range(len(self.arr_matrix[col])):
				for j in range(len(self.arr_matrix[col + 1])):
					summa_matr[i][j] = self.arr_matrix[col][i][j] + self.arr_matrix[col + 1][i][j]

		self.show(summa_matr)

	def mull_matrix(self):
		pass
		



# a = Linear_Bsk_Operations()
# n = int(input('n = '))
# m = int(input('m = '))
# a.add_matrix(n, m)
# n_2 = int(input('n_2 = '))
# m_2 = int(input('m_2 = '))
# a.add_matrix(n_2, m_2)
# a.mull_to_scal()
# a.my_matrix()
# a.transponse()
# a.main_diag()
# a.mul_matrix()
# a.matrix_summation()