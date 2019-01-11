
from math import sqrt
from random import randint, shuffle

# NxN sudoku with K missing digits
def make_sudoku(N=9, K=0):
	sN = int(sqrt(N))
	mat = [[0] * N for x in range(0, N)]
	#Fill in diagonal boxes
	for x in range(0, sN):
		# Fill in sN x sN
		l = list(range(1, N+1))
		shuffle(l)
		for i in range(0, sN):
			for j in range(0, sN):
				mat[x * sN + i][x * sN + j] = l[i * sN + j]
	def checkSafe(x, y, num):
		if num in mat[x]:
			return False
		for i in range(0, N):
			if mat[i][y] == num:
				return False
		for i in range(0, sN):
			for j in range(0, sN):
				if mat[x//sN * sN + i][y//sN * sN + j] == num:
					return False
		return True
	def fillRemaining(x, y):
		# Fill in next line or end the procedure
		if y >= N:
			y = 0
			x += 1
			if x >= N:
				return True
		if mat[x][y] != 0:
			return fillRemaining(x, y+1)
		for num in range(1, N+1):
			if checkSafe(x, y, num):
				mat[x][y] = num
				if fillRemaining(x, y+1):
					return True
				mat[x][y] = 0
		return False
	def display():
		s = ""
		l = "+" + ("-" * (sN * 2 + 1) + "+") * sN + "\n"
		for (line, i) in zip(mat, range(len(mat))):
			if i % 3 == 0:
				s += l
			for (item, j) in zip(line, range(0, len(line))):
				if j % 3 == 0:
					s += "| "
				s += str(item) + " "
			s += "|\n"
		s += l
		return s.replace("0", "_")
	def trySolve(xy):
		if xy >= N*N:
			return 1
		x = xy // N
		y = xy % N
		if mat[x][y] != 0:
			return trySolve(xy + 1)
		res = 0
		for num in range(1, N+1):
			if checkSafe(x, y, num):
				mat[x][y] = num
				res += trySolve(xy + 1)
		mat[x][y] = 0
		return res
	def tryDelete(DelNum, TryTimes = N):
		if DelNum == 0:
			return True
		x = 0
		y = 0
		while True:
			xy = randint(0, N*N-1)
			x = xy // N
			y = xy % N
			if mat[x][y] != 0:
				break
		bkup = mat[x][y]
		mat[x][y] = 0
		if trySolve(0) == 1:
			return tryDelete(DelNum-1)
		mat[x][y] = bkup
		return tryDelete(DelNum, TryTimes - 1)

	if fillRemaining(0, 0):
		fst = mat[0][:]
		if tryDelete(K):
			return display(), fst
	return make_sudoku(N, K)


def sudoku_function(level_index, next_title, my_path):
	ll = list(next_title)
	mat, fst = make_sudoku(9, randint(30, 50))
	l = [0] * len(next_title)
	for i in range(0, len(next_title)):
		l[i] = ll[fst[i] - 1]
	s = "\n"
	for (item, i) in zip(l, range(0, len(next_title))):
		if i % 3 == 0:
			s += "  "
		s += str(item) + " "
	s += "\n"
	s += mat
	return "<pre>" + s + "</pre>"

if __name__ == '__main__':
	#mat, fst = make_sudoku(K=50)
	#print(mat)
	print(sudoku_function(0, "123456789", ""))
