import os
import shutil
from ppfg_utils import create_welcome, create_body, create_goodbye

from levels.hyperlink import *
from levels.naiveaddr import *
from levels.picaddr import *
from levels.asciiart import *
from levels.qrcodeaddr import *
from levels.mazeaddr import *
from levels.sudoku import *
from levels.hiddenelements import *

level_funcs = [(hyperlink_function, hyperlink_hint),\
		(naiveaddr_function, naiveaddr_hint),\
		(qrcodeaddr_function, qrcodeaddr_hint),\
		(hiddenelements_function, hiddenelements_hint),\
		(asciiart_function, asciiart_hint),\
		(sudoku_function, sudoku_hint),\
		(mazeaddr_function, mazeaddr_hint),\
		(picaddr_function, picaddr_hint)]

# create level in base_dir
def create_level(file_path, level_index, num):
	base_dir = "../level" + str(level_index)
	if not os.path.exists(base_dir):
		os.mkdir(base_dir)
	file_path = create_welcome(file_path, level_index, level_funcs[level_index])
	for x in range(1, num):
		file_path = create_body(file_path, level_index, level_funcs[level_index])
	return create_goodbye(file_path, level_index, level_funcs[level_index])

def clear_levels(level_num):
	try:
		for x in range(0, level_num+1):
			shutil.rmtree("../level" + str(x))
	except Exception as e:
		pass

def create_congratulations(file_path):
	#TODO: create dir when needs
	file_dir = "../" + "/".join(file_path.split('/')[0:-1])
	if not os.path.exists(file_dir):
		os.mkdir(file_dir)
	file = open("../" + file_path, 'w')
	content = "Congratulations!"
	file.write(content)
	file.close()
