import os
import shutil
from ppfg_utils import *

from level0 import level0_body, level0_welcome, level0_goodbye
from level1 import level1_body, level1_welcome, level1_goodbye

level_funcs = [level0_body, level1_body]
welcome_funcs = [level0_welcome, level1_welcome]
goodbye_funcs = [level0_goodbye, level1_goodbye]

# create level in base_dir
def create_level(file_path, level_index, num):
	base_dir = "../" + level_names[level_index]
	if not os.path.exists(base_dir):
		os.mkdir(base_dir)
	file_path = create_file(file_path, level_index, welcome_funcs[level_index])
	for x in range(1, num):
		file_path = create_file(file_path, level_index, level_funcs[level_index])
	return create_file(file_path, level_index+1, goodbye_funcs[level_index])

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
