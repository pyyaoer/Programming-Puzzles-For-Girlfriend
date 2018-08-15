import os
import shutil
from ppfg_utils import *

from level0 import level0
from level1 import level1

level_funcs = [level0, level1]

# create level in base_dir
def create_level(file_path, level_index, num):
	base_dir = "../" + level_names[level_index]
	if not os.path.exists(base_dir):
		os.mkdir(base_dir)
	for x in range(1, num):
		file_path = create_file(file_path, level_index, level_funcs[level_index])
	return create_file(file_path, level_index+1, level_funcs[level_index])

def clear_levels():
	try:
		for level in level_names:
			shutil.rmtree("../" + level)
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
