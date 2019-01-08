# Modify the maze generation algorithm used in
# https://rosettacode.org/wiki/Maze_generation#Python

from random import shuffle, sample, randint
from string import ascii_letters, digits

start = []
end = []

def make_maze(w = 16, h = 8, msg = "!@#$%^&*()"):
	vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
	ver = [["|   "] * w + ['|'] for _ in range(h)] + [[]]
	hor = [["+---"] * w + ['+'] for _ in range(h + 1)]


	def walk(x, y):
		global start, end
		vis[y][x] = 1

		d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
		shuffle(d)
		isstart = (x == 0 and y == 0)
		isend = (x == w-1 and y == 0)
		for (xx, yy) in d:
			if vis[yy][xx]: continue
			if xx == x: hor[max(y, yy)][x] = "+   "
			if yy == y: ver[y][max(x, xx)] = "    "
			ret = walk(xx, yy)
			if ret == 1: isstart = True
			if ret == 2: isend = True
		if isstart and isend:
			start += [(x, y)]
			return 0
		if isstart:
			start += [(x, y)]
			return 1
		if isend:
			end += [(x, y)]
			return 2
		return 0

	walk(w-1, h-1)
	ver[0][0] = "    "
	ver[0][-1] = "  ->"

	# fill the answer along the way
	end.reverse()
	ls = len(start)
	le = len(end)
	charpos = sample(range(0, ls + le), 10)
	lmsg = list(msg)
	j = 0
	for (i, (a, b)) in zip(range(0, ls + le), start + end):
		ss = list(ver[b][a])
		#ss[2] = "."
		if i in charpos:
			ss[2] = lmsg[j]
			j += 1
		ver[b][a] = "".join(ss)

	# fill in characters randomly
	succ = 0
	while succ < w*h * 10 / (ls + le):
		rx = randint(0, w-1)
		ry = randint(0, h-1)
		if (rx, ry) in start+end:
			continue
		ss = list(ver[ry][rx])
		ss[2] = sample(ascii_letters + digits, 1)[0]
		ver[ry][rx] = "".join(ss)
		succ += 1

	s = []
	hasin = False
	for (a, b) in zip(hor, ver):
		if hasin:
			s += [' ']*3 + a + ['\n'] + [' ']*3 + b + ['\n']
		else:
			s += [' ']*3 + a + ['\n'] + ['-> '] + b + ['\n']
			hasin = True
	return ''.join(s)

def mazeaddr_function(level_index, next_title, my_path):
	content = "\n" + make_maze(msg=next_title)
	return "<pre>" + content + "</pre>"
