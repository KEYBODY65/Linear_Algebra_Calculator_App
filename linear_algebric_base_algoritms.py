class Linear_Bsk_Operations:
	def __init__(self, n:int, m:int):
		self.n = n
		self.m = m
		self.matrix = [[0] * m for i in range(n)]
		for i in range(n):
			for j in range(m):
				self.matrix[i][j] = int(input())
	def show(self):
		for i in range(self.n):
			for j in range(self.m):
				print(str(self.matrix[i][j]).ljust(1), end=' ')
			print()

	def transponse(self):
		for i in range(self.n):
			for j in range(i + 1, self.n):
				self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
		print('Транспонированная матрица')
		self.show()

	def main_diag(self):
		self.main = []
		c = 0
		for i in range(self.n):
			self.main.append(self.matrix[i][c])
			c += 1
		print('Главная диагональ')
		print(self.main)


n = int(input('n = '))
m = int(input('m = '))
a = Linear_Bsk_Operations(n, m)
a.transponse()
a.main_diag()
