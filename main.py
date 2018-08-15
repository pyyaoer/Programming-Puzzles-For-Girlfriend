import os
from ppfg_levels import *

level_nums = [2, 2]

if __name__ == '__main__':
	start_file = "index.html"
	clear_levels()
	for x in range(0,2):
		start_file = create_level(start_file, x, level_nums[x])
	create_congratulations(start_file)

