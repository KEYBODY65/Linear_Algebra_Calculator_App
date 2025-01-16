class Linear_Bsk_Operations:
	def __init__(self):
		self.arr_matrix = []

	def add_matrix(self, n:int, m:int):
		new_matrix = [[0] * m for _ in range(n)]
		print(f"Введите элементы матрицы размером {n}x{m}:")
		for i in range(n):
		    for j in range(m):
		        new_matrix[i][j] = int(input(f"Элемент [{i}][{j}]: "))
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
		print(self.	main)

	def my_matrix(self):
		for matrix in self.arr_matrix:
			self.show(matrix)
		



a = Linear_Bsk_Operations()
n = int(input('n = '))
m = int(input('m = '))
a.add_matrix(n, m)
n_2 = int(input('n_2 = '))
m_2 = int(input('m_2 = '))
a.add_matrix(n_2, m_2)
a.my_matrix()
# a.transponse()
a.main_diag()
# a.mul_matrix()
