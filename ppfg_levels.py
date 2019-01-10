import os
import shutil
from ppfg_utils import create_welcome, create_body, create_goodbye

from hyperlink import hyperlink_function
from naiveaddr import naiveaddr_function
from picaddr import picaddr_function
from asciiart import asciiart_function
from qrcodeaddr import qrcodeaddr_function
from mazeaddr import mazeaddr_function
from sudoku import sudoku_function
from hiddenelements import hiddenelements_function

level_funcs = [hyperlink_function, hiddenelements_function, sudoku_function, mazeaddr_function, qrcodeaddr_function, asciiart_function, naiveaddr_function, picaddr_function]

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
