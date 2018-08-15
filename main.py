import os
from ppfg_levels import *

level_nums = [1, 1]

if __name__ == '__main__':
	clear_levels()
	start_file = "index.html"
	for x in range(0,2):
		start_file = create_level(start_file, x, level_nums[x])
	create_congratulations(start_file)

