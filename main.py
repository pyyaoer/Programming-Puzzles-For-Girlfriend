import os
from ppfg_levels import *

level_num = 8
nums = [1] * level_num

if __name__ == '__main__':
	clear_levels(level_num)
	start_file = "index.html"
	for x in range(0, level_num):
		start_file = create_level(start_file, x, nums[x])
	create_congratulations(start_file)

